import argparse, json
from pathlib import Path

REQUIRED = {"id", "category", "question", "answer", "refusal", "provenance", "reconstructed_example"}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    args=ap.parse_args()
    rows=[]; ids=set()
    for n,line in enumerate(Path(args.input).read_text(encoding="utf-8").splitlines(),1):
        if not line.strip(): continue
        row=json.loads(line); missing=REQUIRED-set(row)
        if missing: raise ValueError(f"line {n}: missing {sorted(missing)}")
        if row["id"] in ids: raise ValueError(f"duplicate id: {row['id']}")
        if not row["question"].strip() or not row["answer"].strip(): raise ValueError(f"line {n}: empty text")
        if row["provenance"] != "public_reconstruction" or row["reconstructed_example"] is not True:
            raise ValueError(f"line {n}: reconstructed provenance marker missing")
        ids.add(row["id"]); rows.append(row)
    print(f"validated {len(rows)} records; refusal={sum(r['refusal'] for r in rows)}")

if __name__ == "__main__": main()
