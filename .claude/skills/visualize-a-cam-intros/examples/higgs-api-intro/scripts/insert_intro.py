import json, sys, time, os
S="/private/tmp/claude-501/-Users-saminyasar-decisons/a713d4d8-8655-45e8-b154-c6c3bd2f3d17/scratchpad"; I=S+"/intro"
sys.path.insert(0,os.path.expanduser("~/.claude/skills/visualize-a-cam-intros/scripts")); os.environ["BORUMI_SESS_DIR"]=S+"/borumi_sess"
import borumi_mcp_session as B
OPEN=[None]
def fail(msg):
    if OPEN[0]:
        try: B.call("abort_project_edit",{"tx_id":OPEN[0]},60); print("aborted",OPEN[0])
        except Exception: pass
    raise SystemExit(msg)
def call(tool,args,timeout=300):
    r=B.call(tool,args,timeout); resp=r.get("response",{})
    if "error" in resp: fail(f"{tool} ERROR: {json.dumps(resp['error'])[:600]}")
    out=resp.get("result",{})
    if out.get("isError"): fail(f"{tool} TOOL ERROR: "+"\n".join(c.get("text","") for c in out.get("content",[]))[:700])
    if out.get("structuredContent") is not None: return out["structuredContent"]
    for c in out.get("content",[]):
        try: return json.loads(c.get("text",""))
        except Exception: pass
    return {}
mode=sys.argv[1] if len(sys.argv)>1 else "stage"
SCENE="8c2b"; FILE=I+"/scene1-screen.mp4"
plan=json.load(open(I+"/plan.json"))
acam=[(s["start_ms"],s["end_ms"]) for s in plan["slots"] if s["kind"]=="black"]
cam=[s for s in json.load(open(I+"/borumi/custom-layout-props.json"))["sources"] if s["layer_id"]=="camera_1"][0]
custom={"kind":"custom","transition":{"kind":"instant"},"sources":[
   {"layer_id":"screen_1","x_ratio":0.0,"y_ratio":0.0,"width_ratio":1.0,"height_ratio":1.0,"border_radius_ratio":0.0,"corner_shape":"regular","lock_aspect_ratio":False,"overflow":False,"face_tracking_mode_override":"disabled"},
   dict({k:v for k,v in cam.items() if k not in ("video_background_override","face_tracking_mode_override","hide_on_cursor_overlap","stroke")}, x_ratio=0.775, y_ratio=0.715, width_ratio=0.21, height_ratio=0.25, border_radius_ratio=0.0284, corner_shape="squircle_v2")]}
tx=call("begin_project_edit",{"project_id":"f961"})["tx_id"]; OPEN[0]=tx
sc=call("get_scenes",{"tx_id":tx}); me=[s for s in sc["scenes"] if s["id"]==SCENE][0]; assert me["start_ms"]==0
end=me["end_ms"]; print("scene 1",0,end)
tl=call("get_timeline",{"tx_id":tx,"range":{"start_ms":0,"end_ms":end},"detail":"segments"}); h=tl["timeline_hash"]
screen=[s["id"] for l in tl["layers"] for s in l.get("segments",[]) if l["id"]=="screen_1"]
lay=[s["id"] for l in tl["layers"] for s in l.get("segments",[]) if l["id"]=="layout" and s["start_ms"]>=0 and s["end_ms"]<=end]
print("deleting screen segs",screen,"layouts",lay)
# 1 remove the tldraw screen segments (members only) and scene-1 layouts
call("delete_segments",{"tx_id":tx,"timeline_hash":h,"segment_ids":screen,"expand_groups":False,"ripple":False})
tl=call("get_timeline",{"tx_id":tx,"range":{"start_ms":0,"end_ms":end},"detail":"summary"}); h=tl["timeline_hash"]
for lid in lay:
    r=B.call("delete_segments",{"tx_id":tx,"timeline_hash":h,"segment_ids":[lid],"expand_groups":False,"ripple":False},120)["response"]
    tl=call("get_timeline",{"tx_id":tx,"range":{"start_ms":0,"end_ms":end},"detail":"summary"}); h=tl["timeline_hash"]
sc=call("get_scenes",{"tx_id":tx}); me=[s for s in sc["scenes"] if s["id"]==SCENE][0]; print("after delete scene end",me["end_ms"])
if me["end_ms"]!=end: fail("scene length changed by deletion")
# 2 import + place the composed proof layer
im=call("import_media",{"tx_id":tx,"file_path":FILE}); st=im.get("status"); mid=(im.get("media") or {}).get("id")
while st in ("queued","running"):
    time.sleep(max(1,im.get("poll_after_ms",2000)/1000)); im=call("get_media_import_status",{"import_id":im["import_id"]}); st=im.get("status"); mid=(im.get("media") or {}).get("id") or mid
if st!="completed": fail("import "+json.dumps(im)[:300])
print("media",mid,(im.get("media") or {}).get("duration_ms"))
tl=call("get_timeline",{"tx_id":tx,"range":{"start_ms":0,"end_ms":end},"detail":"summary"}); h=tl["timeline_hash"]
call("add_segments",{"tx_id":tx,"timeline_hash":h,"additions":[{"type":"take","placement":{"at_ms":0},"content":{"media_id":mid,"video_kind":"screen"}}]})
sc=call("get_scenes",{"tx_id":tx}); me=[s for s in sc["scenes"] if s["id"]==SCENE][0]; nxt=sc["scenes"][1]; print("after add: scene",me["start_ms"],me["end_ms"],"next",nxt["display_name"],nxt["start_ms"])
tl=call("get_timeline",{"tx_id":tx,"range":{"start_ms":0,"end_ms":me["end_ms"]},"detail":"segments"}); h=tl["timeline_hash"]
new=[s for l in tl["layers"] for s in l.get("segments",[]) if (s.get("media") or {}).get("media_id")==mid]
if not new: fail("composed take not found")
print("new screen segment",new[0]["id"],new[0]["start_ms"],new[0]["end_ms"],new[0].get("properties"))
call("update_segments",{"tx_id":tx,"timeline_hash":h,"updates":[{"type":"video","segment_id":new[0]["id"],"properties":{"face_tracking_mode":"disabled"}}]})
# 3 layouts: custom (screen full + camera pip) over the proof ranges, fullscreen camera over the A-cam resets
adds=[]; cur=0
for a,b in acam:
    if a>cur: adds.append({"type":"layout","placement":{"range":[cur,a]},"properties":custom})
    adds.append({"type":"layout","placement":{"range":[a,b]},"properties":{"kind":"fullscreen","layer_id":"camera_1","fit":"cover","transition":{"kind":"instant"}}}); cur=b
if cur<end: adds.append({"type":"layout","placement":{"range":[cur,end]},"properties":custom})
tl=call("get_timeline",{"tx_id":tx,"range":{"start_ms":0,"end_ms":end},"detail":"summary"}); h=tl["timeline_hash"]
call("add_segments",{"tx_id":tx,"timeline_hash":h,"additions":adds})
tl=call("get_timeline",{"tx_id":tx,"range":{"start_ms":0,"end_ms":end+2000},"detail":"segments","layers":["layout","screen_1"]})
print("layouts:",[(s["start_ms"],s["end_ms"],s["properties"].get("kind")) for l in tl["layers"] if l["id"]=="layout" for s in l.get("segments",[])])
print("screen:",[(s["start_ms"],s["end_ms"],(s.get("media") or {}).get("media_id")) for l in tl["layers"] if l["id"]=="screen_1" for s in l.get("segments",[])])
# 4 inspect the render: one frame per slot midpoint + boundary frames
mids=[int((s["start_ms"]+s["end_ms"])/2) for s in plan["slots"]]
paths=[]
for t in mids:
    ins=call("inspect_timeline",{"tx_id":tx,"range":{"start_ms":max(0,t-40),"end_ms":t+40},"presentation":"frames","quality":"low","sampling":{"type":"uniform","max_frames":1},"save":True,"view":{"type":"render"}},240)
    paths+=[f["path"] for f in ins.get("frames",[])]
json.dump(paths,open(I+"/stage-frames.txt","w"))
print("frames",len(paths))
if mode=="commit":
    print("COMMITTED",call("commit_project_edit",{"tx_id":tx,"change_summary":"Scene 1 intro: replace the tldraw screen layer with a composed proof layer (16 beats of later footage, generated outputs and graphics), pin the camera bottom-right, and cut to full camera for two resets."}))
else:
    print("TX LEFT OPEN",tx)
