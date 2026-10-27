"""Samin's 'levels' treatment (from his most-viewed video, Claude Just Changed the Stock Market Forever).
Usage: python3 levels_style.py levels-spec.json   (paths in the spec are relative to the cwd; set LEVELS_WORKDIR for scratch files): white grid canvas, blue numbered circle + bold italic title
at the left, proof inside a dark device mock on the right. Produces:
  levels-intro.mp4  : three circles popping in (for 'three levels')
  level-N.mp4       : circle N + title entering, then a sequence of proof clips inside the mock, one after another."""
import subprocess, os, sys, json, math
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from compose_screen_source import smoothzoom
from PIL import Image, ImageDraw, ImageFont
I=os.environ.get("LEVELS_WORKDIR",os.getcwd())   # scratch dir for frame sequences and level backgrounds
W,H,FPS=1920,1080,60
BLUE=(59,130,246); INK=(20,22,26); GRID=(226,228,232)
def font(size,italic=True,bold=True):
    for i in range(0,20):
        try:
            f=ImageFont.truetype("/System/Library/Fonts/HelveticaNeue.ttc",size,index=i); n=" ".join(f.getname())
            if bold and italic and "Bold Italic" in n and "Condensed" not in n: return f
            if bold and not italic and "Bold" in n and "Italic" not in n and "Condensed" not in n: return f
        except Exception: break
    return ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold Italic.ttf" if italic else "/System/Library/Fonts/Supplemental/Arial Bold.ttf",size)
_CANVAS=None
def canvas():
    global _CANVAS
    if _CANVAS is not None: return _CANVAS.copy()
    import numpy as np
    grid=Image.new("L",(W,H),0); d=ImageDraw.Draw(grid)
    for x in range(0,W,60): d.line([(x,0),(x,H)],fill=255,width=1)
    for y in range(0,H,60): d.line([(0,y),(W,y)],fill=255,width=1)
    yy,xx=np.mgrid[0:H,0:W]; r=np.sqrt(((xx-W/2)/(W/2))**2+((yy-H/2)/(H/2))**2)
    strength=np.clip(1.0-0.75*np.clip((r-0.35)/0.85,0,1),0.05,1.0)      # grid fades smoothly toward the edges
    g=np.array(grid,dtype=np.float32)/255.0*strength
    base=np.full((H,W,3),255,dtype=np.float32); line=np.array([226,228,232],dtype=np.float32)
    out=base*(1-g[...,None])+line*g[...,None]
    _CANVAS=Image.fromarray(out.astype("uint8")); return _CANVAS.copy()
def circle(d,cx,cy,r,n,scale=1.0):
    rr=r*scale
    if rr<=0: return
    d.ellipse([cx-rr,cy-rr,cx+rr,cy+rr],fill=BLUE)
    f=font(int(r*1.15*scale),italic=False,bold=True); t=str(n)
    bb=d.textbbox((0,0),t,font=f); d.text((cx-(bb[2]-bb[0])/2-bb[0],cy-(bb[3]-bb[1])/2-bb[1]),t,font=f,fill=(255,255,255))
def ease(t): return 1-(1-t)**3
def render_intro(out,dur=2.2):
    n=int(dur*FPS); d0=f"{I}/lv-frames-intro"; os.makedirs(d0,exist_ok=True)
    base=canvas()
    for i in range(n):
        t=i/FPS; im=base.copy(); dr=ImageDraw.Draw(im)
        for k in range(3):
            a=ease(max(0,min(1,(t-0.1-k*0.22)/0.3))); circle(dr,760+k*200,470,52,k+1,scale=a)
        im.save(f"{d0}/{i:04d}.png")
    subprocess.run(["ffmpeg","-loglevel","error","-y","-framerate",str(FPS),"-i",f"{d0}/%04d.png","-c:v","libx264","-crf","16","-pix_fmt","yuv420p",out],check=True); subprocess.run(["rm","-rf",d0])
MOCK=(760,140,1100,619)   # x,y,w,h of the screen area inside the device mock (right side, clear of the bottom-right camera window? camera starts x 1488,y 772 -> the mock ends at y 915: the mock's lower-right corner sits under the camera; keep the proof's key content in the upper 80%)
def render_level_bg(n,title,out_png):
    im=canvas(); d=ImageDraw.Draw(im)
    circle(d,120,300,46,n)
    f=font(58); words=title.split(" "); lines=[]; cur=""
    for w in words:
        test=(cur+" "+w).strip()
        if d.textlength(test,font=f)>500 and cur: lines.append(cur); cur=w
        else: cur=test
    lines.append(cur)
    for j,l in enumerate(lines): d.text((200,266+j*68),l,font=f,fill=INK)
    # device mock: dark rounded frame with a thin bezel + shadow
    x,y,w,h=MOCK
    sh=Image.new("RGBA",(W,H),(0,0,0,0)); sd=ImageDraw.Draw(sh); sd.rounded_rectangle([x-14,y+6,x+w+14,y+h+30],radius=28,fill=(0,0,0,70))
    from PIL import ImageFilter; sh=sh.filter(ImageFilter.GaussianBlur(18)); im=Image.alpha_composite(im.convert("RGBA"),sh)
    d=ImageDraw.Draw(im); d.rounded_rectangle([x-14,y-14,x+w+14,y+h+14],radius=26,fill=(28,30,34)); d.rounded_rectangle([x,y,x+w,y+h],radius=10,fill=(10,10,12))
    im.convert("RGB").save(out_png)
def render_level(n,title,parts,out,dur):
    """parts: list of {src, ss, dur, crop?}: proof clips shown inside the mock one after another (hard cuts)."""
    bg=f"{I}/lv-bg-{n}.png"; render_level_bg(n,title,bg)
    x,y,w,h=MOCK
    # title entrance: render the first 0.45 s with the title/circle sliding in, as a short png sequence over the mock-less canvas, then overlay video
    ins=["-loop","1","-framerate",str(FPS),"-i",bg]; fc=[]; idx=1; concat_labels=[]
    for p in parts:
        ins+=["-ss",str(p.get("ss",0)),"-i",p["src"]]
        crop=f"crop={p['crop']}," if p.get("crop") else ""
        zp=smoothzoom(1.06,p['dur'],0.5,0.5,FPS).replace("(W-W/","(W-W/")  # perspective push on a 2x frame
        fc.append(f"[{idx}:v]{crop}scale={2*w}:{2*h}:force_original_aspect_ratio=increase:flags=lanczos,crop={2*w}:{2*h},fps={FPS},setpts=PTS-STARTPTS,"+zp+f"scale={w}:{h}:flags=lanczos,tpad=stop_mode=clone:stop_duration=3,trim=duration={p['dur']:.3f},setpts=PTS-STARTPTS,setsar=1[p{idx}]")
        concat_labels.append(f"[p{idx}]"); idx+=1
    fc.append("".join(concat_labels)+f"concat=n={len(parts)}:v=1:a=0[proof]")
    # slide-in of the left block: emulate by a moving crop of the bg is complex; instead fade the whole card in over 0.25 s and let the proof pop in at 0.3 s
    fc.append(f"[0:v]fps={FPS},trim=duration={dur:.3f},setpts=PTS-STARTPTS[bgv]")
    fc.append(f"[bgv][proof]overlay=x={x}:y={y}:shortest=0[out]")
    subprocess.run(["ffmpeg","-loglevel","error","-y"]+ins+["-filter_complex",";".join(fc),"-map","[out]","-t",f"{dur:.3f}","-c:v","libx264","-crf","16","-pix_fmt","yuv420p","-an",out],check=True)
    print(out)
if __name__=="__main__":
    spec=json.load(open(sys.argv[1]))
    if spec.get("intro"): render_intro(spec["intro"]["out"],spec["intro"]["dur"])
    for lv in spec.get("levels",[]): render_level(lv["n"],lv["title"],lv["parts"],lv["out"],lv["dur"])
