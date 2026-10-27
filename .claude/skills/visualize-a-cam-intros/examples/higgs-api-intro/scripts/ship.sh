#!/bin/zsh
# usage: ship.sh v8  -> assemble, commit to Borumi, export, analyze, packet, 720p
V=$1; S=/private/tmp/claude-501/-Users-saminyasar-decisons/a713d4d8-8655-45e8-b154-c6c3bd2f3d17/scratchpad; I=$S/intro
cd $I && python3 assemble.py 2>&1 | grep -E "rendered|rror" ; ffprobe -v error -select_streams v -count_frames -show_entries stream=nb_read_frames -of csv=p=0 $I/scene1-screen.mp4
$S/bc list_open_projects '{}' 60 | head -c 120; echo
python3 $I/insert_intro.py commit 2>&1 | tail -1
python3 - "$V" <<'PY'
import json,sys,os,time
V=sys.argv[1]; S="/private/tmp/claude-501/-Users-saminyasar-decisons/a713d4d8-8655-45e8-b154-c6c3bd2f3d17/scratchpad"; I=S+"/intro"
sys.path.insert(0,os.path.expanduser("~/.claude/skills/visualize-a-cam-intros/scripts")); os.environ["BORUMI_SESS_DIR"]=S+"/borumi_sess"
import borumi_mcp_session as B
def call(tool,args,timeout=300):
    r=B.call(tool,args,timeout)["response"]; out=r.get("result") or r.get("error") or {}
    if isinstance(out,dict) and out.get("structuredContent") is not None: return out["structuredContent"]
    for c in (out.get("content",[]) if isinstance(out,dict) else []):
        try: return json.loads(c.get("text",""))
        except Exception: pass
    return out
e=call("export_video",{"project_id":"f961","range":{"type":"scene","scene_id":"8c2b"},"settings":{"type":"preset","preset":"balanced"},"output_path":f"{I}/renders/intro-{V}.mp4"})
print("export started",e.get("export_id"))
for i in range(300):
    time.sleep(max(3,(e.get("poll_after_ms") or 5000)/1000)); st=call("get_export_status",{"export_id":e["export_id"]})
    if st.get("status") in ("completed","failed","canceled"): print("EXPORT",st.get("status")); break
sc=call("get_scenes",{"project_id":"f961"}); print("scene1",sc["scenes"][0]["start_ms"],sc["scenes"][0]["end_ms"],"next",sc["scenes"][1]["start_ms"],"total",sc["scenes"][-1]["end_ms"])
PY
python3 ~/.claude/skills/visualize-a-cam-intros/scripts/analyze_intro.py $I/renders/intro-$V.mp4 --out $I/qa/$V/analysis --interval 2 >/dev/null 2>&1
python3 -c "
import json; d=json.load(open('$I/qa/$V/analysis/analysis.json')); print('black',d['black_segments'],'freeze',d['freeze_segments'],'cuts',len(d['scene_cuts_seconds']))"
python3 $I/make_packet.py $I/renders/intro-$V.mp4 $V && ffmpeg -loglevel error -y -i $I/renders/intro-$V.mp4 -vf "scale=1280:720" -c:v libx264 -preset fast -crf 23 -c:a aac -b:a 128k -movflags +faststart $I/renders/intro-$V-720p.mp4 && echo $V-DONE
