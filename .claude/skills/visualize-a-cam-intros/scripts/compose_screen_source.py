#!/usr/bin/env python3
"""Compose one 1920x1080 screen-source video for a scene from a JSON slot plan (Samin's treatment).

  python3 compose_screen_source.py plan.json

plan.json:
{
  "out": "scene1-screen.mp4",            # composed video, exactly scene_ms long
  "scene_ms": 49320,
  "fps": 60,                             # slot clips at 60 fps so re-cut boundaries do not drift
  "lead_ms": 120,                        # every cut leads the spoken word by this much (applied by the planner; kept here for the record)
  "workdir": "v-out",                    # per-slot clips + contact sheet land here
  "slots": [
    {"start_ms": 0,     "end_ms": 3080,  "kind": "still",  "src": "podium.png", "zoom": 1.15, "fx": 0.5, "fy": 0.55},
    {"start_ms": 3080,  "end_ms": 8561,  "kind": "broll",  "src": "broll/benchmark.mp4", "ss": 0.0, "crop": "1500:844:60:60", "zoom": 1.04},
    {"start_ms": 8561,  "end_ms": 14870, "kind": "seq", "parts": [
        {"kind": "broll", "src": "broll/agents.mp4", "ss": 3.05, "dur": 3.30},
        {"kind": "still", "src": "roster.png", "zoom": 1.06, "fx": 0.5, "fy": 0.4}]},
    {"start_ms": 14870, "end_ms": 19420, "kind": "seq", "parts": [
        {"kind": "tweet", "src": "tweet.png", "width": 1450, "zoom": 1.06, "fy": 0.5, "dur": 2.10},
        {"kind": "pan",   "src": "youtube-results.png", "pan_px": 900}]}
  ]
}

kinds:
  broll  later-footage screen export (cursor baked in): fill frame, optional crop "w:h:x:y", slow push, vignette + bottom line
  tweet  text card: centered on near-black at `width` px, slow push anchored at fy, vignette, no line
  still  a still with one motivated push (zoom, fx, fy anchor), no vignette
  pan    tall page: scale to 1920 wide and slide down `pan_px` over the slot, vignette
  seq    ordered parts; a part without `dur` takes the remaining slot time
"""
import json, os, subprocess, sys

VIG = "vignette=angle=PI/8:mode=forward"                          # slight: corners ~78% of center
LINE = "drawbox=x=0:y=1052:w=1920:h=3:color=white@0.35:t=fill"     # thin "this is from later" line, below the camera window
BG = "0x0f0d0b"

def smoothzoom(zoom, dur, fx=0.5, fy=0.5, fps=60):
    """True sub-pixel push: a perspective remap with cubic interpolation, evaluated per frame on `in`, on a 3840x2160 frame.
    Do NOT use zoompan (integer crop offsets shimmer every frame) or a stepped scale (motion lands on alternate frames)."""
    N = int(round(dur * fps)); z = f"(1+({zoom}-1)*in/{N})"
    return (f"perspective=x0='(W-W/{z})*{fx}':y0='(H-H/{z})*{fy}':x1='(W-W/{z})*{fx}+W/{z}':y1='(H-H/{z})*{fy}':"
            f"x2='(W-W/{z})*{fx}':y2='(H-H/{z})*{fy}+H/{z}':x3='(W-W/{z})*{fx}+W/{z}':y3='(H-H/{z})*{fy}+H/{z}':interpolation=cubic:eval=frame,")

def run(args):
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y"] + args, check=True)

def probe(path):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path], capture_output=True, text=True).stdout.strip())

class Composer:
    def __init__(self, plan):
        self.p = plan; self.fps = int(plan.get("fps", 60)); self.wd = plan.get("workdir", "compose-out"); os.makedirs(self.wd, exist_ok=True)
        self.enc = ["-c:v", "libx264", "-preset", "medium", "-crf", "17", "-pix_fmt", "yuv420p", "-an", "-movflags", "+faststart"]
        self.n = 0
    def tmp(self, tag):
        self.n += 1; return os.path.join(self.wd, f"{self.n:02d}-{tag}.mp4")
    def broll(self, s, dur):
        out = self.tmp("broll"); z = float(s.get("zoom", 1.0)); crop = s.get("crop")
        pre = f"fps={self.fps},setpts=PTS-STARTPTS," + (f"crop={crop}," if crop else "") + "scale=1920:1080:flags=lanczos,"
        zp = ("scale=3840:2160:flags=lanczos," + smoothzoom(z, dur, 0.5, 0.5, self.fps) + "scale=1920:1080:flags=lanczos,") if z != 1.0 else ""
        vf = pre + zp + f"tpad=stop_mode=clone:stop_duration=2,trim=duration={dur:.3f},setpts=PTS-STARTPTS,{VIG},{LINE},format=yuv420p"
        run(["-ss", str(s.get("ss", 0.0)), "-i", s["src"], "-vf", vf] + self.enc + [out]); return out
    def clip(self, s, dur):
        out = self.tmp("clip"); z = float(s.get("zoom", 1.0)); crop = s.get("crop")
        sp = float(s.get("speed", 1.0))
        pre = (f"setpts=PTS/{sp:.4f}," if sp != 1.0 else "") + f"fps={self.fps},setpts=PTS-STARTPTS," + (f"crop={crop}," if crop else "") + "scale=1920:1080:flags=lanczos,"
        zp = ("scale=3840:2160:flags=lanczos," + smoothzoom(z, dur, float(s.get("fx",0.5)), float(s.get("fy",0.5)), self.fps) + "scale=1920:1080:flags=lanczos,") if z != 1.0 else ""
        vf = pre + zp + f"tpad=stop_mode=clone:stop_duration=2,trim=duration={dur:.3f},setpts=PTS-STARTPTS,{VIG},format=yuv420p"
        run(["-ss", str(s.get("ss", 0.0)), "-i", s["src"], "-vf", vf] + self.enc + [out]); return out
    def raw(self, s, dur):
        out = self.tmp("raw"); crop = s.get("crop")
        vf = f"fps={self.fps},setpts=PTS-STARTPTS," + (f"crop={crop}," if crop else "") + f"scale=1920:1080:flags=lanczos,tpad=stop_mode=clone:stop_duration=2,trim=duration={dur:.3f},setpts=PTS-STARTPTS,format=yuv420p"
        run(["-ss", str(s.get("ss", 0.0)), "-i", s["src"], "-vf", vf] + self.enc + [out]); return out
    def black(self, s, dur):
        out = self.tmp("black")
        run(["-f", "lavfi", "-i", f"color=c={BG}:s=1920x1080:r={self.fps}", "-t", f"{dur:.3f}", "-vf", "format=yuv420p"] + self.enc + [out]); return out
    def tweet(self, s, dur):
        out = self.tmp("tweet"); w = int(s.get("width", 1400)); z = float(s.get("zoom", 1.06)); fy = float(s.get("fy", 0.5))
        vf = (f"scale={w*2}:-1:flags=lanczos,pad=3840:2160:(ow-iw)/2:(oh-ih)/2:color={BG},fps={self.fps},setpts=PTS-STARTPTS,"
              + smoothzoom(z, dur, 0.5, fy, self.fps) + f"scale=1920:1080:flags=lanczos,trim=duration={dur:.3f},setpts=PTS-STARTPTS,{VIG},format=yuv420p")
        run(["-framerate", str(self.fps), "-loop", "1", "-t", str(dur + 0.5), "-i", s["src"], "-vf", vf] + self.enc + [out]); return out
    def still(self, s, dur):
        out = self.tmp("still"); z = float(s.get("zoom", 1.15)); fx = float(s.get("fx", 0.5)); fy = float(s.get("fy", 0.55)); crop = s.get("crop")
        vf = ((f"crop={crop}," if crop else "") + f"scale=3840:2160:force_original_aspect_ratio=increase:flags=lanczos,crop=3840:2160,fps={self.fps},setpts=PTS-STARTPTS,"
              + smoothzoom(z, dur, fx, fy, self.fps) + f"scale=1920:1080:flags=lanczos,trim=duration={dur:.3f},setpts=PTS-STARTPTS,format=yuv420p")
        run(["-framerate", str(self.fps), "-loop", "1", "-t", str(dur + 0.5), "-i", s["src"], "-vf", vf] + self.enc + [out]); return out
    def pan(self, s, dur):
        out = self.tmp("pan"); px = int(s.get("pan_px", 900))
        vf = f"scale=1920:-1:flags=lanczos,fps={self.fps},crop=1920:1080:0:'min({px},{px}*t/{dur:.3f})',trim=duration={dur:.3f},setpts=PTS-STARTPTS,{VIG},format=yuv420p"
        run(["-framerate", str(self.fps), "-loop", "1", "-t", str(dur + 0.5), "-i", s["src"], "-vf", vf] + self.enc + [out]); return out
    def concat(self, parts, dur, out, durs=None):
        ins = []; fc = []
        for i, p in enumerate(parts):
            ins += ["-i", p]
            nf = f",trim=end_frame={int(round(durs[i]*self.fps))},setpts=PTS-STARTPTS" if durs else ""
            fc.append(f"[{i}:v]fps={self.fps},setpts=PTS-STARTPTS{nf},setsar=1[v{i}]")
        fc.append("".join(f"[v{i}]" for i in range(len(parts))) + f"concat=n={len(parts)}:v=1:a=0,trim=duration={dur:.3f}[o]")
        run(ins + ["-filter_complex", ";".join(fc), "-map", "[o]"] + self.enc + [out]); return out
    def render(self, s, dur):
        k = s["kind"]
        if k == "seq":
            parts = []; durs = []; left = dur
            for i, part in enumerate(s["parts"]):
                d = float(part["dur"]) if "dur" in part and i < len(s["parts"]) - 1 else left
                parts.append(self.render(part, d)); durs.append(d); left -= d
            return self.concat(parts, dur, self.tmp("seq"), durs)
        return getattr(self, k)(s, dur + 0.15 if k != "seq" else dur)  # +150 ms pad, trimmed at concat
    def build(self):
        clips = []
        for s in self.p["slots"]:
            dur = (s["end_ms"] - s["start_ms"]) / 1000.0; clips.append((self.render(s, dur), dur))
        ins = []; fc = []
        for i, (c, d) in enumerate(clips): ins += ["-i", c]; fc.append(f"[{i}:v]trim=duration={d:.3f},setpts=PTS-STARTPTS,fps={self.fps},setsar=1,format=yuv420p[v{i}]")
        fc.append("".join(f"[v{i}]" for i in range(len(clips))) + f"concat=n={len(clips)}:v=1:a=0[out]")
        out = self.p["out"]; scene = self.p["scene_ms"] / 1000.0
        run(ins + ["-filter_complex", ";".join(fc), "-map", "[out]", "-t", f"{scene:.3f}"] + self.enc + [out])
        run(["-i", out, "-vf", "fps=1/2,scale=480:-1,tile=5x5", "-frames:v", "1", os.path.join(self.wd, "contact.png")])
        print(out, f"{probe(out):.3f}s (scene {scene:.3f}s)")

if __name__ == "__main__":
    Composer(json.load(open(sys.argv[1]))).build()
