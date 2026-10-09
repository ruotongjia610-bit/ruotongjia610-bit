import argparse, json
from pathlib import Path

def norm(x): return " ".join(x.lower().strip().split())

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--gold",required=True); ap.add_argument("--pred",required=True); args=ap.parse_args()
    gold={r["id"]:r for r in map(json.loads,Path(args.gold).read_text(encoding="utf-8").splitlines()) if r.strip()}
    pred={r["id"]:r for r in map(json.loads,Path(args.pred).read_text(encoding="utf-8").splitlines()) if r.strip()}
    ids=sorted(set(gold)&set(pred)); exact=sum(norm(gold[i]["answer"])==norm(pred[i]["answer"]) for i in ids)/max(1,len(ids))
    refusal_ids=[i for i in ids if gold[i]["refusal"]]; refusal_ok=sum(any(t in pred[i]["answer"] for t in ("不能","无法","证据不足")) for i in refusal_ids)/max(1,len(refusal_ids))
    print(json.dumps({"n":len(ids),"exact_match":exact,"refusal_recall":refusal_ok,"provenance":"public_reconstruction"},ensure_ascii=False,indent=2))

if __name__ == "__main__": main()
