import argparse, json
from pathlib import Path

SYSTEM = "You answer AGV field-survey questions using only supported evidence. If the question asks for private information or the evidence is insufficient, refuse clearly."

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--input",required=True); ap.add_argument("--output",required=True); args=ap.parse_args()
    out=Path(args.output); out.parent.mkdir(parents=True,exist_ok=True)
    count=0
    with out.open("w",encoding="utf-8") as w:
        for line in Path(args.input).read_text(encoding="utf-8").splitlines():
            if not line.strip(): continue
            r=json.loads(line)
            rec={"id":r["id"],"messages":[{"role":"system","content":SYSTEM},{"role":"user","content":r["question"]},{"role":"assistant","content":r["answer"]}],"metadata":{"category":r["category"],"refusal":r["refusal"],"provenance":r["provenance"]}}
            w.write(json.dumps(rec,ensure_ascii=False)+"\n"); count+=1
    print(f"wrote {count} chat records to {out}")

if __name__ == "__main__": main()
