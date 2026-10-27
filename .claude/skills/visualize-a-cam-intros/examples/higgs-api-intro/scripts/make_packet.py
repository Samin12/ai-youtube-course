"""Critic packet from an actual export: contact sheet (1 frame / 2 s) + a 3-frame strip per slot (start+50ms, mid, end-80ms)."""
import json, subprocess, sys, os
from PIL import Image, ImageDraw
I="/private/tmp/claude-501/-Users-saminyasar-decisons/a713d4d8-8655-45e8-b154-c6c3bd2f3d17/scratchpad/intro"
export=sys.argv[1]; tag=sys.argv[2] if len(sys.argv)>2 else "v1"
out=f"{I}/qa/{tag}"; os.makedirs(out,exist_ok=True)
bm=json.load(open(I+"/beat-map.json"))["beats"]
def frame(t_ms,path,w=640):
    subprocess.run(["ffmpeg","-loglevel","error","-y","-ss",f"{t_ms/1000:.3f}","-i",export,"-frames:v","1","-vf",f"scale={w}:-1",path],check=True)
# contact sheet
subprocess.run(["ffmpeg","-loglevel","error","-y","-i",export,"-vf","fps=0.5,scale=384:-1,tile=6x7","-frames:v","1",f"{out}/contact-sheet.jpg"],check=True)
# strips
strips=[]
for i,b in enumerate(bm):
    ts=[b["start_ms"]+50,(b["start_ms"]+b["end_ms"])//2,b["end_ms"]-80]
    ims=[]
    for k,t in enumerate(ts):
        p=f"{out}/b{i+1:02d}-{k}.jpg"; frame(t,p); ims.append((t,Image.open(p).convert("RGB")))
    W=640;H=360; strip=Image.new("RGB",(3*W,H+22),"black"); d=ImageDraw.Draw(strip)
    for k,(t,im) in enumerate(ims): strip.paste(im.resize((W,H)),(k*W,22)); d.text((k*W+4,4),f"beat {i+1}  {t/1000:.2f}s  [{['start','mid','end'][k]}]",fill="white")
    sp=f"{out}/strip-{i+1:02d}.jpg"; strip.save(sp,quality=82); strips.append(sp)
json.dump({"export":export,"contact_sheet":f"{out}/contact-sheet.jpg","strips":strips},open(f"{out}/packet.json","w"),indent=1)
print(out, len(strips), "strips")
