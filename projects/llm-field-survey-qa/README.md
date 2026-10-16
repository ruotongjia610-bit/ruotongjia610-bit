# AGV Field-Survey QA — Public Reproducible Reconstruction

This directory is a public reconstruction of Ruotong Jia's AGV field-survey question-answering project, prepared to demonstrate the data, training, evaluation and inference workflow.

**It is not the original company source code, training dataset, model checkpoint, private deployment log, or internal validation split.** My work included domain QA preparation, Qwen-7B adaptation with QLoRA, Wi-Fi/5G confusion cases, refusal examples and inference integration. Internal evaluation figures are not reported in this public documentation.

[Project portfolio](../../portfolio/README.md)

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

The script saves the adapter and tokenizer. Training this reconstruction requires a separately supplied compatible model and an appropriate GPU environment. No trained-model performance result is claimed by the mock tests.

## Validation scope

The dataset and mock tests demonstrate a reproducible software path. They do not reproduce historical company training or deployment. Generalized example records are not the original company data, and mock-service logs are not evidence of a trained model's answer quality.
