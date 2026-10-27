import json, sys, time, os
S="/private/tmp/claude-501/-Users-saminyasar-decisons/a713d4d8-8655-45e8-b154-c6c3bd2f3d17/scratchpad"
sys.path.insert(0,os.path.expanduser("~/.claude/skills/visualize-a-cam-intros/scripts")); os.environ["BORUMI_SESS_DIR"]=S+"/borumi_sess"
import borumi_mcp_session as B
OUT=S+"/intro/broll"; RC=S+"/intro/borumi"
def call(tool,args,timeout=300):
    r=B.call(tool,args,timeout)["response"]; out=r.get("result") or r.get("error") or {}
    if isinstance(out,dict) and out.get("isError"): raise SystemExit(tool+" TOOL ERROR "+"\n".join(c.get("text","") for c in out.get("content",[]))[:600])
    if isinstance(out,dict) and "code" in out and "message" in out: raise SystemExit(tool+" ERROR "+json.dumps(out)[:400])
    if isinstance(out,dict) and out.get("structuredContent") is not None: return out["structuredContent"]
    for c in (out.get("content",[]) if isinstance(out,dict) else []):
        try: return json.loads(c.get("text",""))
        except Exception: pass
    return out
RANGES={
 "buffet":(88000,104500),"suborapi":(124000,134000),"savings":(172000,184000),"table":(224000,262000),
 "breakeven":(300000,345000),"apikeys":(388000,422000),"codex_ready":(428000,460000),"readme":(466000,492000),
 "chatgpt_prompt":(492000,530000),"storm_cost":(596000,642000),"storm_full":(650000,695000),"workflow_useful":(704000,722000),
 "which_model":(728000,772000),"skill_slide":(876000,892000),"openhf_github":(976000,992000),"studio":(1056000,1100000),
 "avatar":(1100000,1160000),"hoodie":(1165000,1215000),
}
json.dump(RANGES,open(RC+"/export-ranges.json","w"),indent=1)
# --- transaction A: temporary fullscreen screen layouts
tx=call("begin_project_edit",{"project_id":"f961"})["tx_id"]
tl=call("get_timeline",{"tx_id":tx,"range":{"start_ms":0,"end_ms":1262666},"detail":"summary","layers":["layout"]}); h=tl["timeline_hash"]
adds=[{"type":"layout","placement":{"range":[a,b]},"properties":{"kind":"fullscreen","layer_id":"screen_1","fit":"cover","transition":{"kind":"instant"}}} for a,b in RANGES.values()]
call("add_segments",{"tx_id":tx,"timeline_hash":h,"additions":adds})
tl=call("get_timeline",{"tx_id":tx,"range":{"start_ms":0,"end_ms":1262666},"detail":"segments","layers":["layout"]})
temp=[s["id"] for l in tl["layers"] for s in l.get("segments",[]) if s["properties"].get("kind")=="fullscreen" and any(s["start_ms"]==a and s["end_ms"]==b for a,b in RANGES.values())]
print("temp layouts",len(temp),temp)
assert len(temp)==len(RANGES), "unexpected temp layout count"
json.dump(temp,open(RC+"/temp-layout-ids.json","w"))
c=call("commit_project_edit",{"tx_id":tx,"change_summary":"TEMPORARY: fullscreen screen layouts over 18 ranges to export cursor-baked screen b-roll for the intro; removed in the next commit."})
print("commit A",c)
# --- exports
jobs={}
for name,(a,b) in RANGES.items():
    e=call("export_video",{"project_id":"f961","range":{"type":"time","start_ms":a,"end_ms":b},"settings":{"type":"custom","width_px":1920,"height_px":1080,"fps":30},"output_path":f"{OUT}/{name}.mp4"})
    jobs[name]=e["export_id"]
    while True:
        time.sleep(max(2,(e.get("poll_after_ms") or 3000)/1000)); st=call("get_export_status",{"export_id":e["export_id"]})
        if st.get("status") in ("completed","failed","canceled"): print(name,st.get("status"),(st.get("artifact") or {}).get("path")); break
json.dump(jobs,open(RC+"/export-jobs.json","w"),indent=1)
# --- transaction B: remove the temporary layouts
tx=call("begin_project_edit",{"project_id":"f961"})["tx_id"]
tl=call("get_timeline",{"tx_id":tx,"range":{"start_ms":0,"end_ms":1262666},"detail":"segments","layers":["layout"]}); h=tl["timeline_hash"]
present=[s["id"] for l in tl["layers"] for s in l.get("segments",[]) if s["id"] in temp]
call("delete_segments",{"tx_id":tx,"timeline_hash":h,"segment_ids":present,"expand_groups":False,"ripple":False})
tl=call("get_timeline",{"tx_id":tx,"range":{"start_ms":0,"end_ms":1262666},"detail":"segments","layers":["layout"]})
left=[(s["start_ms"],s["end_ms"]) for l in tl["layers"] for s in l.get("segments",[]) if s["properties"].get("kind")=="fullscreen"]
print("fullscreen layouts left (should be the 7 cards):",left)
c=call("commit_project_edit",{"tx_id":tx,"change_summary":"Remove the 18 temporary fullscreen export layouts; project layouts back to their previous coverage."})
print("commit B",c); print("ALLDONE")
