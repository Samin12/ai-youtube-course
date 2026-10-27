"""Render every slot of a plan through compose_screen_source.py with a content-hash cache, then concat them into one
scene-length layer with frame-accurate slot boundaries (every boundary lands on round(end_ms * fps / 1000)).

Usage: python3 assemble_scene_layer.py plan.json [--cache DIR] [--out FILE] [--fps 60] [--contact sheet.jpg]

The plan is the compose_screen_source.py slot plan (slots with start_ms/end_ms, kinds broll|clip|raw|tweet|still|pan|black|seq).
Slots that render a frame short are padded by cloning their last frame (tpad), so a short clip never shifts later beats.
"""
import json, hashlib, os, sys, subprocess, shutil, argparse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import compose_screen_source as C

ap = argparse.ArgumentParser(); ap.add_argument("plan"); ap.add_argument("--cache", default="v-cache"); ap.add_argument("--out"); ap.add_argument("--fps", type=int, default=60); ap.add_argument("--contact")
a = ap.parse_args()
plan = json.load(open(a.plan)); fps = a.fps; os.makedirs(a.cache, exist_ok=True)
comp = C.Composer(dict(plan, workdir=plan.get("workdir", "v-out"))); files = []
for i, s in enumerate(plan["slots"]):
    key = hashlib.md5(json.dumps({k: v for k, v in s.items() if k not in ("start_ms", "end_ms")}, sort_keys=True).encode() + f"{s['end_ms']-s['start_ms']}".encode()).hexdigest()[:12]
    dst = f"{a.cache}/{key}.mp4"
    if not os.path.exists(dst):
        src = comp.render(s, (s["end_ms"] - s["start_ms"]) / 1000); shutil.copy(src, dst); print("rendered slot", i + 1, key)
    else:
        print("cached slot", i + 1, key)
    files.append(dst)
bounds = [0] + [round(s["end_ms"] * fps / 1000) for s in plan["slots"]]
total = bounds[-1]; ins = []; fc = []
for i, f in enumerate(files):
    nf = bounds[i + 1] - bounds[i]; ins += ["-i", f]
    fc.append(f"[{i}:v]fps={fps},setpts=PTS-STARTPTS,tpad=stop_mode=clone:stop_duration=1,trim=end_frame={nf},setpts=PTS-STARTPTS,setsar=1,format=yuv420p[v{i}]")
fc.append("".join(f"[v{i}]" for i in range(len(files))) + f"concat=n={len(files)}:v=1:a=0[out]")
out = a.out or plan.get("out", "scene-screen.mp4")
subprocess.run(["ffmpeg", "-loglevel", "error", "-y"] + ins + ["-filter_complex", ";".join(fc), "-map", "[out]", "-frames:v", str(total), "-c:v", "libx264", "-preset", "medium", "-crf", "17", "-pix_fmt", "yuv420p", "-an", "-movflags", "+faststart", out], check=True)
if a.contact:
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", out, "-vf", "fps=1/2,scale=384:-1,tile=6x7", "-frames:v", "1", a.contact], check=True)
n = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v", "-count_frames", "-show_entries", "stream=nb_read_frames", "-of", "csv=p=0", out], capture_output=True, text=True).stdout.strip()
print(out, "frames", n, "expected", total, "OK" if n == str(total) else "MISMATCH")
