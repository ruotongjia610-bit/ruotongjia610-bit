# Ruotong Jia · 贾若彤

**Robotics · Multimodal Learning · Reliable Autonomous Systems**

[中文介绍](README.zh-CN.md) · [Project portfolio](portfolio/README.md) · [Research record](research/README.md)

I am an algorithm engineer working on robot perception, autonomous navigation and model adaptation. My background in physical modeling and integration testing informs how I build AI systems: define the assumptions, implement the interfaces, test failure cases and check what the evidence actually supports.

My recent work focuses on point-cloud processing, relocalization, local obstacle avoidance and safe stopping for humanoid navigation. I also develop interaction actions and adapt language and vision-language models for specific tasks.

## Selected work

| Project | My contribution | Evidence and scope |
|---|---|---|
| [Robot perception and autonomous navigation](portfolio/robot-navigation.md) | Sensor-input validation, point-cloud processing, relocalization, local avoidance and safe-stop logic | Navigation simulation, offline regression and interface checks completed; complete physical navigation remains under validation. Public summary only. |
| [Humanoid interaction actions](portfolio/README.md#humanoid-interaction-actions) | Reusable action states, keyframe transitions, pause/resume behavior and integration with an existing locomotion controller | Selected actions tested on hardware. [Generic public example](projects/humanoid-robot-control/README.md) with deterministic tests. |
| [AGV field-survey question answering](projects/llm-field-survey-qa/README.md) | Domain QA preparation, Qwen-7B adaptation with QLoRA, confusion/refusal cases and an inference interface | Public reconstruction with data checks and mock inference; original training artifacts and internal results are not distributed. |
| [Vision-language image captioning](portfolio/README.md#vision-language-image-captioning) | Qwen2-VL-2B-Instruct adaptation, image-text formatting and batch collation for variable image sizes | Personal training project using COCO 2014, Transformers, PEFT and SwanLab; no held-out quality benchmark claimed. |
| [Real-time simulation and parameter identification](portfolio/README.md#real-time-simulation-and-parameter-identification) | Timing implementation and testing, numerical parameter estimation and residual analysis | Co-inventor of a granted timing patent. Historical implementation and engineering data are not distributed. |
| [Fluid mechanics and scientific computing](portfolio/README.md#fluid-mechanics-and-scientific-computing) | CFD modeling and comparison of bearing-surface microstructures | Second author of a published paper in *Lubrication Engineering*. |

## Research record

- **Published paper:** hydrostatic-bearing oil-film flow under different surface microstructures, *Lubrication Engineering*, 2024. Second author. [DOI](https://doi.org/10.3969/j.issn.0254-0150.2024.01.004).
- **Granted invention patent:** Windows real-time simulation timing, **CN119473492B**. Second-listed inventor; granted 10 October 2025. [Public patent record](https://patents.google.com/patent/CN119473492B/en).
- **Manuscripts in review:** collaborative decision-making in multi-agent manufacturing systems, and an industrial foundation-model Perspective. These are listed separately from publications.
- **Invention applications in progress:** three projects in robot sensing/navigation and equipment-health monitoring. Unpublished technical content is not included.

[Research topics, authorship and current status](research/README.md)

## How I approach engineering and research

- **Connect algorithms to systems.** Work across sensor data, coordinate frames, state estimation, task logic and execution interfaces.
- **Test failure behavior.** Examine stale inputs, invalid observations, state transitions and recovery as well as successful runs.
- **Make comparisons interpretable.** State the data, baseline and metric; distinguish a synthetic experiment from a hardware result.
- **Keep contributions explicit.** Separate my integration and algorithm work from vendor controllers, pretrained models and existing open-source components.

## Technical toolkit

| Area | Tools and methods used |
|---|---|
| Robotics | ROS 2, Nav2, MuJoCo, RViz, point-cloud processing, state machines |
| Learning | PyTorch, Transformers, PEFT, LoRA/QLoRA, Qwen, Qwen2-VL, SwanLab |
| Modeling and analysis | NumPy, Pandas, MATLAB, ANSYS Fluent, numerical optimization |
| Software | Python, C++, Git, automated tests, Linux/Windows integration |

## Background

B.Eng. in Energy and Power Engineering, **Hebei University of Technology**. My engineering experience spans engine simulation, avionics integration testing, industrial AI and humanoid robotics.

National Third Prize in the 14th and 15th National College Student Energy Conservation and Emission Reduction Competition.

## Explore the public code

- [Robot action and navigation example](projects/humanoid-robot-control/README.md)
- [AGV QA reconstruction](projects/llm-field-survey-qa/README.md)
- [Automated checks](https://github.com/ruotongjia610-bit/ruotongjia610-bit/actions/workflows/tests.yml)

This portfolio combines public examples, published research references and high-level engineering summaries. Company implementations, deployment details, maps, private datasets and unpublished invention mechanisms are excluded.

**Contact:** [ruotongjia610@gmail.com](mailto:ruotongjia610@gmail.com)

*Updated 16 October 2026. Research and validation status refer to this date.*
