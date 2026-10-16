# Source workbook profile

The public QA reconstruction uses generalized field-survey topics. The original workbook is not distributed here.

## Topic coverage

Examples cover site conditions, operating environment, route constraints, load interfaces, network coverage, system integration, safety and follow-up questions.

## What it supports

This is a field-survey source form rather than a ready-to-train JSONL dataset. It supports the project description that the model was intended to answer practical AGV deployment questions, including:

- operating conditions and floor/route constraints;
- 5G and Wi-Fi coverage, latency, handover and packet-loss checks;
- WMS/MES/PLC/WCS and other system-interface questions;
- obstacle, mixed-traffic and safety checks;
- recording open items and follow-up ownership.

## Public-use rule

The original workbook remains outside the public reconstruction package. The package contains only `qa_derived_from_deidentified_workbook.jsonl`, which rewrites the source into general engineering questions and removes customer, project, person, exact site, and internal deployment identifiers. The derived file is evidence of the data-preparation pipeline; it is not a copy of the company workbook.

The historical work included Qwen-7B adaptation with QLoRA, AGV field-survey QA preparation, Wi-Fi/5G confusion cases, refusal examples and inference integration. Internal validation data and performance figures are outside the scope of this public reconstruction.
