import argparse, json, logging
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scripts.infer import mock_answer

class Handler(BaseHTTPRequestHandler):
    rows=[]
    def do_POST(self):
        if self.path!="/answer": self.send_error(404); return
        n=int(self.headers.get("Content-Length",0)); body=json.loads(self.rfile.read(n))
        q=body.get("question",""); ans=mock_answer(q,self.rows)
        out={"answer":ans,"backend":"deterministic_mock","provenance":"public_reconstruction"}
        logging.info(json.dumps({"event":"answer","question":q,"backend":"deterministic_mock"},ensure_ascii=False))
        data=json.dumps(out,ensure_ascii=False).encode(); self.send_response(200); self.send_header("Content-Type","application/json; charset=utf-8"); self.send_header("Content-Length",str(len(data))); self.end_headers(); self.wfile.write(data)
    def log_message(self,*a): return

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--mock",action="store_true"); ap.add_argument("--host",default="127.0.0.1"); ap.add_argument("--port",type=int,default=8091); ap.add_argument("--data",default=None); args=ap.parse_args()
    if not args.mock: raise SystemExit("Only --mock is included in this public reconstruction.")
    data_path=Path(args.data) if args.data else Path(__file__).resolve().parents[1]/"data"/"qa_reconstructed.jsonl"
    Handler.rows=[json.loads(x) for x in data_path.read_text(encoding="utf-8").splitlines() if x.strip()]
    logging.basicConfig(level=logging.INFO,format="%(asctime)s %(levelname)s %(message)s")
    print(f"listening on http://{args.host}:{args.port}/answer; backend=deterministic_mock; provenance=public_reconstruction")
    HTTPServer((args.host,args.port),Handler).serve_forever()

if __name__=="__main__": main()
