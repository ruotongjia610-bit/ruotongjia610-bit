# Model artifact

Model weights are not distributed in this repository. The public training entry point accepts a separately supplied compatible checkpoint through `--model_name_or_path`.

The repository contains the tokenizer-independent data pipeline, training configuration, evaluation script, and inference interface so the workflow can be inspected without downloading the checkpoint.
