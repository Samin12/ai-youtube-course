"""Render slots with a content-hash cache, then concat to the scene-length layer."""
import json, hashlib, os, sys, subprocess, shutil
I="/private/tmp/claude-501/-Users-saminyasar-decisons/a713d4d8-8655-45e8-b154-c6c3bd2f3d17/scratchpad/intro"
sys.path.insert(0,I); import compose_intro as C
plan=json.load(open(I+"/plan.json")); cache=I+"/v-cache"; os.makedirs(cache,exist_ok=True)
comp=C.Composer(dict(plan,workdir=I+"/v-out")); files=[]
for i,s in enumerate(plan["slots"]):
    key=hashlib.md5(json.dumps({k:v for k,v in s.items() if k not in ("start_ms","end_ms")},sort_keys=True).encode()+f"{s['end_ms']-s['start_ms']}".encode()).hexdigest()[:12]
    dst=f"{cache}/{key}.mp4"
    if not os.path.exists(dst):
        dur=(s["end_ms"]-s["start_ms"])/1000; src=comp.render(s,dur); shutil.copy(src,dst); print("rendered slot",i+1,key)
    else: print("cached slot",i+1,key)
    files.append((dst,(s["end_ms"]-s["start_ms"])/1000))
ins=[];fc=[]
bounds=[0]+[round(s["end_ms"]*60/1000) for s in plan["slots"]]
for i,(f,d) in enumerate(files):
    nf=bounds[i+1]-bounds[i]; ins+=["-i",f]; fc.append(f"[{i}:v]fps=60,setpts=PTS-STARTPTS,tpad=stop_mode=clone:stop_duration=1,trim=end_frame={nf},setpts=PTS-STARTPTS,setsar=1,format=yuv420p[v{i}]")
fc.append("".join(f"[v{i}]" for i in range(len(files)))+f"concat=n={len(files)}:v=1:a=0[out]")
out=plan["out"]; subprocess.run(["ffmpeg","-loglevel","error","-y"]+ins+["-filter_complex",";".join(fc),"-map","[out]","-frames:v","5001","-c:v","libx264","-preset","medium","-crf","17","-pix_fmt","yuv420p","-an","-movflags","+faststart",out],check=True)
subprocess.run(["ffmpeg","-loglevel","error","-y","-i",out,"-vf","fps=1/2,scale=384:-1,tile=6x7","-frames:v","1",I+"/compose-contact.jpg"],check=True)
print(out, C.probe(out))
