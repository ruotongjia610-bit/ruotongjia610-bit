# Ruotong Jia

AI algorithm engineer working on humanoid robot control, embodied intelligence, and reliable autonomous systems.

## Selected projects

### Humanoid Robot Action Control and Tour Navigation

Reusable Python modules for upper-body action control and multi-stop tour navigation.

- Smooth joint-space trajectories with bounded duration.
- Pause, resume, completion, stop, and fault-safe action states.
- Waypoint sequencing, arrival events, route cancellation, and sensor-health checks.
- Velocity limiting with a fail-closed safety gate.
- Deterministic unit tests and example configurations.

See the [robot control package](robot_control/README.md).

### AGV Field-Survey QA

A Qwen-7B + QLoRA workflow for AGV field-survey question answering.

- Domain QA preparation for deployment and network questions.
- Explicit Wi-Fi/5G disambiguation cases.
- Out-of-scope refusal examples and exact-match evaluation.
- A small inference service with structured logs.
- A public-safe derived dataset from a de-identified field-survey workbook.

See [projects/llm-field-survey-qa](projects/llm-field-survey-qa/README.md).

The AGV directory contains a reproducible public reconstruction. It does not include the local model weights or the original workbook.

## Repository layout

```text
robot_control/                    robot actions and tour navigation
projects/llm-field-survey-qa/    AGV field-survey QA pipeline
config/                           example action and route configuration
tests/                            deterministic robot-control tests
docs/                             architecture notes
```

## Test robot-control modules

```bash
python -m unittest discover -s tests -p 'test_*.py'
```
