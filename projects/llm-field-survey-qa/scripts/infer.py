import argparse, json, re
from pathlib import Path

REFUSAL_TERMS=("不能提供","无法提供","不应提供","不能保证","证据不足")

def mock_answer(q, rows):
    ql=q.lower(); best=None; score=-1
    for r in rows:
        score_now=sum(1 for token in re.findall(r"[\w]+|[一-龥]", r["question"].lower()) if token in ql)
        if score_now>score: score,best=score_now,r
    if any(x in q for x in ("源代码","密钥","客户工厂地图","内部资料","部署日志")):
        return "我不能提供公司内部源代码、密钥、客户地图或未公开部署日志。"
    return best["answer"] if best and score>0 else "证据不足，我不会根据猜测给出结论。"

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--question",required=True); ap.add_argument("--data",default=None); ap.add_argument("--mock",action="store_true"); args=ap.parse_args()
    data_path=Path(args.data) if args.data else Path(__file__).resolve().parents[1]/"data"/"qa_reconstructed.jsonl"
    rows=[json.loads(x) for x in data_path.read_text(encoding="utf-8").splitlines() if x.strip()]
    if not args.mock: raise SystemExit("This public reconstruction supports --mock unless a model adapter is added explicitly.")
    answer=mock_answer(args.question,rows); print(json.dumps({"question":args.question,"answer":answer,"backend":"deterministic_mock","provenance":"public_reconstruction"},ensure_ascii=False))

if __name__ == "__main__": main()
