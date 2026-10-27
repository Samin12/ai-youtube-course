"""Export the end of the recording screen-only (temporary fullscreen layout), then restore the original layouts exactly."""
import json, sys, time, os
S="/private/tmp/claude-501/-Users-saminyasar-decisons/a713d4d8-8655-45e8-b154-c6c3bd2f3d17/scratchpad"
sys.path.insert(0,os.path.expanduser("~/.claude/skills/visualize-a-cam-intros/scripts")); os.environ["BORUMI_SESS_DIR"]=S+"/borumi_sess"
import borumi_mcp_session as B
OUT=S+"/intro/broll"; A,Bm=int(sys.argv[1]),int(sys.argv[2]); NAME=sys.argv[3]
def call(tool,args,timeout=300):
    r=B.call(tool,args,timeout)["response"]; out=r.get("result") or r.get("error") or {}
    if isinstance(out,dict) and out.get("isError"): raise SystemExit(tool+" TOOL ERROR "+"\n".join(c.get("text","") for c in out.get("content",[]))[:600])
    if isinstance(out,dict) and "code" in out and "message" in out: raise SystemExit(tool+" ERROR "+json.dumps(out)[:400])
    if isinstance(out,dict) and out.get("structuredContent") is not None: return out["structuredContent"]
    for c in (out.get("content",[]) if isinstance(out,dict) else []):
        try: return json.loads(c.get("text",""))
        except Exception: pass
    return out
END=1262873
def layouts(tx):
    tl=call("get_timeline",{"tx_id":tx,"range":{"start_ms":0,"end_ms":END},"detail":"segments","layers":["layout"]})
    return tl["timeline_hash"],[s for l in tl["layers"] for s in l.get("segments",[])]
tx=call("begin_project_edit",{"project_id":"f961"})["tx_id"]
h,segs=layouts(tx)
orig=[(s["start_ms"],s["end_ms"],s["properties"]) for s in segs if s["end_ms"]>A and s["start_ms"]<Bm]
print("original layouts overlapping range:",[(a,b,p.get("kind")) for a,b,p in orig])
call("add_segments",{"tx_id":tx,"timeline_hash":h,"additions":[{"type":"layout","placement":{"range":[A,Bm]},"properties":{"kind":"fullscreen","layer_id":"screen_1","fit":"cover","transition":{"kind":"instant"}}}]})
h,segs=layouts(tx); temp=[s["id"] for s in segs if s["start_ms"]==A and s["end_ms"]==Bm and s["properties"].get("kind")=="fullscreen"]
assert len(temp)==1, temp
c=call("commit_project_edit",{"tx_id":tx,"change_summary":"TEMPORARY fullscreen screen layout over the end of the video to export screen b-roll; removed in the next commit."}); print("commit A",c["commit_id"])
e=call("export_video",{"project_id":"f961","range":{"type":"time","start_ms":A,"end_ms":Bm},"settings":{"type":"custom","width_px":1920,"height_px":1080,"fps":30},"output_path":f"{OUT}/{NAME}.mp4"})
while True:
    time.sleep(max(2,(e.get("poll_after_ms") or 3000)/1000)); st=call("get_export_status",{"export_id":e["export_id"]})
    if st.get("status") in ("completed","failed","canceled"): print("export",st.get("status")); break
tx=call("begin_project_edit",{"project_id":"f961"})["tx_id"]
h,segs=layouts(tx); present=[s["id"] for s in segs if s["id"] in temp]
call("delete_segments",{"tx_id":tx,"timeline_hash":h,"segment_ids":present,"expand_groups":False,"ripple":False})
h,segs=layouts(tx)
# refill: any original range piece not covered now gets its original properties back
cov=sorted((s["start_ms"],s["end_ms"]) for s in segs)
def covered(a,b): return any(x<=a and y>=b for x,y in cov)
adds=[]
for a,b,p in orig:
    a2,b2=max(a,A),min(b,Bm)
    if not covered(a2,b2): adds.append({"type":"layout","placement":{"range":[a2,b2]},"properties":p})
if adds:
    call("add_segments",{"tx_id":tx,"timeline_hash":h,"additions":adds}); print("refilled",[(x["placement"]["range"],x["properties"].get("kind")) for x in adds])
h,segs=layouts(tx)
print("layouts now in range:",[(s["start_ms"],s["end_ms"],s["properties"].get("kind")) for s in segs if s["end_ms"]>A and s["start_ms"]<Bm])
fs=[(s["start_ms"],s["end_ms"]) for s in segs if s["properties"].get("kind")=="fullscreen"]; print("fullscreen layouts (7 cards expected):",len(fs))
c=call("commit_project_edit",{"tx_id":tx,"change_summary":"Remove the temporary export layout; layouts restored."}); print("commit B",c["commit_id"]); print("ALLDONE")
