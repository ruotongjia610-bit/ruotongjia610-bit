# Model artifact

The local project directory contains a merged Qwen2 float16 checkpoint used for internal inference. The weight file is several gigabytes and is not committed to this repository. The public training entry point accepts a local or separately hosted checkpoint through `--model_name_or_path`.

The repository contains the tokenizer-independent data pipeline, training configuration, evaluation script, and inference interface so the workflow can be inspected without downloading the checkpoint.
