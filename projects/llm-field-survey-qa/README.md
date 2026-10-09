# AGV Field-Survey QA — Public Reproducible Reconstruction

This directory is a public-safe reconstruction of Jia Ruotong's AGV field-survey question-answering project. It is prepared for interview explanation and reproducibility practice.

**It is not the original company source code, training dataset, model checkpoint, private deployment log, or internal validation split.** The original project facts are recorded in the CV and interview notes: Qwen-7B, QLoRA adaptation, domain QA preparation, Wi-Fi/5G confusion handling, refusal examples, an internal inference tool, and a reported 97.6% exact match on an internal validation set. That internal result is not reproduced by this package.

## What is included

- `data/qa_reconstructed.jsonl`: rewritten public-safe examples covering AGV field questions, Wi-Fi/5G distinction, and out-of-scope refusal.
- `data/qa_derived_from_deidentified_workbook.jsonl`: generalized QA summaries derived from the user-provided de-identified survey workbook.
- `data/source_workbook_profile.md`: structure, provenance, and public-use boundary for that workbook.
- `scripts/validate_dataset.py`: schema and label checks.
- `scripts/prepare_dataset.py`: converts the JSONL records to chat-training records.
- `train_qlora.py`: complete Hugging Face + PEFT QLoRA training entry point.
- `scripts/evaluate.py`: exact-match and refusal evaluation.
- `scripts/infer.py`: command-line inference with a model adapter or a deterministic mock backend.
- `scripts/derive_from_workbook.py`: checks a local workbook and writes generalized public-safe QA summaries without copying raw values.
- `deployment/service.py`: small HTTP inference service with JSON logs.
- `tests/test_reconstruction.py`: tests that run without downloading a model.
- `logs/reconstruction_smoke_test.log`: generated mock-service run; it is explicitly labelled as a reconstruction smoke test.
- `requirements-qlora.txt`: dependencies for an optional real QLoRA run.

## Run the public reconstruction

```bash
python scripts/validate_dataset.py --input data/qa_reconstructed.jsonl
python scripts/prepare_dataset.py --input data/qa_reconstructed.jsonl --output results/chat_records.jsonl
python scripts/derive_from_workbook.py --input "<local-path-to-AGV-project-survey.xlsx>" --output results/qa_from_workbook.jsonl
python -m unittest discover -s tests -p 'test_*.py'
python scripts/infer.py --mock --question "现场巡检时 Wi-Fi 信号变差，应该先检查什么？"
python deployment/service.py --mock --host 127.0.0.1 --port 8091
```

## Optional real QLoRA run

The training script is runnable when the user supplies a model checkpoint and a GPU environment. The exact checkpoint used in the historical project is not available in this directory, so the model path must be provided explicitly.

```bash
python train_qlora.py \
  --model_name_or_path <exact-or-compatible-qwen-checkpoint> \
  --train_file results/chat_records.jsonl \
  --output_dir results/qlora_adapter \
  --use_4bit
```

The script saves the adapter and tokenizer. It does not claim that this reconstruction produces the historical 97.6% result.

## How to describe it in an interview

Say that the historical project used Qwen-7B with QLoRA for AGV field-survey QA, including domain-data preparation, Wi-Fi/5G confusion cases, refusal cases, internal inference integration, and an internal validation result. Use this package only to explain the pipeline and to demonstrate a public-safe reproduction structure. Do not call the reconstruction data the company's original data, and do not claim that the mock log is a historical deployment log.
