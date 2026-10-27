#!/usr/bin/env python3
"""Persistent Borumi MCP session (stdio JSON-RPC) for agents that cannot add an MCP server mid-session.

  python3 borumi_mcp_session.py start                      # daemon: initialize + get_guides once, then serve a FIFO
  python3 borumi_mcp_session.py call <tool> '<json args>' [timeout_s]
  MCP_OUT=/path/out.json python3 borumi_mcp_session.py call ...   # also save the raw response

Borumi must be open. Guides gate tools per connection: after start, fetch each guide you need one id at a time,
e.g. call get_guides '{"guide_ids":["project_edits"]}'. State lives next to this file in ./borumi_sess/."""
import json, subprocess, sys, threading, queue, time, os, uuid
BASE=os.environ.get("BORUMI_SESS_DIR") or os.path.dirname(os.path.abspath(__file__))+"/borumi_sess"
FIFO=BASE+"/req.fifo"; RESP=BASE+"/resp"; LOG=BASE+"/daemon.log"
CMD=["/Applications/Borumi.app/Contents/MacOS/borumi","mcp"]
def daemon():
    os.makedirs(RESP,exist_ok=True)
    if os.path.exists(FIFO): os.remove(FIFO)
    os.mkfifo(FIFO)
    p=subprocess.Popen(CMD,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=open(LOG,"a"),text=True,bufsize=1)
    q=queue.Queue()
    def reader():
        for line in p.stdout:
            line=line.strip()
            if not line: continue
            try: q.put(json.loads(line))
            except Exception: q.put({"raw":line})
    threading.Thread(target=reader,daemon=True).start()
    seq=[0]
    def rpc(method,params,timeout=120):
        seq[0]+=1; i=seq[0]
        p.stdin.write(json.dumps({"jsonrpc":"2.0","id":i,"method":method,"params":params})+"\n"); p.stdin.flush()
        t0=time.time(); notes=[]
        while time.time()-t0<timeout:
            try: m=q.get(timeout=1)
            except queue.Empty: continue
            if m.get("id")==i: return m,notes
            notes.append(m)
        return {"error":{"message":"timeout"}},notes
    rpc("initialize",{"protocolVersion":"2025-06-18","capabilities":{},"clientInfo":{"name":"jarvis","version":"1.0"}})
    p.stdin.write(json.dumps({"jsonrpc":"2.0","method":"notifications/initialized"})+"\n"); p.stdin.flush()
    rpc("tools/call",{"name":"get_guides","arguments":{}})
    open(BASE+"/ready","w").write("ok")
    while True:
        with open(FIFO) as f:
            for line in f:
                line=line.strip()
                if not line: continue
                try: req=json.loads(line)
                except Exception: continue
                rid=req["rid"]
                if req.get("tool")=="__quit__":
                    open(RESP+"/"+rid+".json","w").write("{}"); p.terminate(); return
                m,notes=rpc("tools/call",{"name":req["tool"],"arguments":req.get("args",{})},req.get("timeout",120))
                open(RESP+"/"+rid+".json.tmp","w").write(json.dumps({"response":m,"notifications":notes}))
                os.rename(RESP+"/"+rid+".json.tmp",RESP+"/"+rid+".json")
def call(tool,args,timeout=120):
    rid=uuid.uuid4().hex
    with open(FIFO,"w") as f: f.write(json.dumps({"rid":rid,"tool":tool,"args":args,"timeout":timeout})+"\n")
    path=RESP+"/"+rid+".json"; t0=time.time()
    while not os.path.exists(path):
        time.sleep(0.2)
        if time.time()-t0>timeout+10: return {"error":"client timeout"}
    return json.load(open(path))
if __name__=="__main__":
    if sys.argv[1]=="start": daemon()
    else:
        tool=sys.argv[2]; args=json.loads(sys.argv[3]) if len(sys.argv)>3 else {}
        to=int(sys.argv[4]) if len(sys.argv)>4 else 120
        r=call(tool,args,to)
        resp=r.get("response",{})
        out=resp.get("result",resp.get("error"))
        if isinstance(out,dict) and "content" in out:
            txt="\n".join(c.get("text","") for c in out["content"] if c.get("type")=="text")
            sc=out.get("structuredContent")
            print(txt if txt else json.dumps(sc,indent=1))
            if sc and txt and os.environ.get("MCP_SC"): print("\n[structuredContent]\n"+json.dumps(sc,indent=1))
        else: print(json.dumps(out,indent=1))
        if os.environ.get("MCP_OUT"): open(os.environ["MCP_OUT"],"w").write(json.dumps(r,indent=1))
