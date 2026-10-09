# Source workbook profile

The user-provided workbook `AGV项目调研工勘表.xlsx` was inspected locally as a possible source for the AGV field-survey QA project.

## Structure

- One visible worksheet (`Sheet0`)
- 65 rows and 8 columns
- No formulas, comments, hyperlinks, hidden worksheets, or external links were found
- The form is organized into sections for site scenario, operating environment, route and layout, fixtures and load interfaces, network coverage, system integration, safety, and follow-up items

## What it supports

This is a field-survey source form rather than a ready-to-train JSONL dataset. It supports the project description that the model was intended to answer practical AGV deployment questions, including:

- operating conditions and floor/route constraints;
- 5G and Wi-Fi coverage, latency, handover and packet-loss checks;
- WMS/MES/PLC/WCS and other system-interface questions;
- obstacle, mixed-traffic and safety checks;
- recording open items and follow-up ownership.

## Public-use rule

The original workbook remains outside the public reconstruction package. The package contains only `qa_derived_from_deidentified_workbook.jsonl`, which rewrites the source into general engineering questions and removes customer, project, person, exact site, and internal deployment identifiers. The derived file is evidence of the data-preparation pipeline; it is not a copy of the company workbook.

The historical project facts remain separate: Qwen-7B, QLoRA, AGV field-survey QA, Wi-Fi/5G confusion cases, refusal examples, an internal inference tool, and a reported 97.6% exact match on an internal validation set.
