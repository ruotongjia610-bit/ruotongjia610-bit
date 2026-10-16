# Engineering and research portfolio

[Home](../README.md) · [中文主页](../README.zh-CN.md) · [Research record](../research/README.md)

These summaries identify the problem, my contribution and the scope of the available evidence. Public example code is linked where available. Industrial work is described at a high level.

## Robot perception and autonomous navigation

**Problem.** A navigation system must decide whether its observations and estimated position are reliable enough to move, and respond predictably when a route is obstructed or inputs become invalid.

**My contribution.** I work on point-cloud processing, relocalization, local obstacle avoidance and safe stopping, with experience integrating perception and mission interfaces in ROS 2/Nav2. I use repeatable failure cases to distinguish perception, localization, planning and execution problems.

**Evidence.** Navigation simulation, offline regression and interface checks have been completed. Physical sensor integration has begun; complete real-world autonomous navigation is still being validated. [Detailed public summary](robot-navigation.md).

**中文：** 在八客机器人自主导览开发中，我负责点云融合、重定位、局部避障和安全停车，重点处理“输入是否可信、定位是否可用、何时应停止、何时能恢复”等系统问题。已有仿真、离线和接口验证，完整真机闭环仍在推进。

## Humanoid interaction actions

**Problem.** An interaction gesture needs predictable transitions, completion criteria and interruption behavior while remaining compatible with the platform's existing motion control.

**My contribution.** I implemented reusable gesture states, keyframe interpolation, configurable hold durations and input bindings. My work concerns upper-body action development and integration with an existing locomotion policy, rather than training that policy.

**Evidence.** Selected actions have been debugged on hardware. The [public action and navigation example](../projects/humanoid-robot-control/README.md) demonstrates trajectories, state transitions and safety checks through deterministic tests. It is a generic example and is not the robot's production controller.

**中文：** 我将交互动作拆成姿态、过渡、保持和退出等状态，开发可复用的动作逻辑并完成部分真机调试。公开代码用于展示状态机、轨迹和异常处理，不包含原厂步态策略或公司控制器。

## AGV field-survey question answering

**Problem.** Domain assistants must distinguish similar technical concepts and recognize questions outside their knowledge boundary.

**My contribution.** I prepared domain question-answer data, adapted Qwen-7B with QLoRA, added Wi-Fi/5G confusion cases and refusal examples, and integrated an inference interface. The work combines data preparation, model adaptation and evaluation design.

**Evidence.** The [public reconstruction](../projects/llm-field-survey-qa/README.md) includes generalized examples, schema validation, training and evaluation entry points, and mock inference. Running the mock backend checks the software path; it does not measure a trained model's answer quality. Original company data, model weights and internal evaluation figures are not distributed.

**中文：** 这项工作涵盖领域数据整理、参数高效微调、事实混淆与拒答处理、推理服务接入。公开版本展示可检查的流程；模拟推理测试与真实模型效果评测分开说明。

## Vision-language image captioning

**Problem.** Image-captioning adaptation requires consistent image-text records and batching that respects the model's visual input representation.

**My contribution.** In a personal project, I adapted Qwen2-VL-2B-Instruct with LoRA using COCO 2014. I prepared conversation-format samples, handled variable image sizes in batch collation and monitored optimization with SwanLab, using Transformers and PEFT.

**Evidence.** The project establishes experience with multimodal data preparation and training integration. A held-out caption-quality or hallucination benchmark is not reported here. Source code and checkpoints for this project are not included in this repository.

**中文：** 个人项目中完成 Qwen2-VL 图像描述适配，处理图文格式与不同尺寸图像的训练批次问题。已有训练实践，不把损失下降直接等同于描述质量、视觉理解或机器人决策能力提升。

## Real-time simulation and parameter identification

**Problem.** A numerical simulation needs both a useful physical model and measured execution behavior. Timing accuracy and CPU consumption must be considered together.

**My contribution.** I implemented and tested timing mechanisms for Windows simulation, processed steady-state engine data, applied Gauss–Newton parameter identification and analyzed residuals. I also contributed to the timing patent documentation.

**Evidence.** I am the second-listed inventor of the granted [CN119473492B patent](https://patents.google.com/patent/CN119473492B/en), assigned to Tsinghua University. The public record describes the timing invention. This portfolio does not distribute the historical engineering implementation or claim a hard real-time guarantee.

**中文：** 我在发动机仿真中参与定时程序、参数辨识和残差分析，把数值模型与实际运行约束联系起来；相关定时发明已授权，本人为第二发明人。

## Fluid mechanics and scientific computing

**Problem.** Surface microstructure can affect the flow in a hydrostatic bearing; a numerical comparison must keep physical assumptions and boundary conditions explicit.

**My contribution.** I worked on ANSYS Fluent modeling and comparative analysis of bearing-surface microstructures. This work developed my experience in setting up numerical models and interpreting results against physical assumptions.

**Evidence.** Second author of “Study on Oil Film Flow Characteristics of Hydrostatic Bearings with Different Microstructures,” *Lubrication Engineering* 49(1), 2024. [DOI](https://doi.org/10.3969/j.issn.0254-0150.2024.01.004).

**中文：** 通过轴承微结构的 CFD 建模与对比分析积累数值研究经验，相关论文已发表，本人为第二作者。

## Systems integration and verification

My earlier engineering work included integration test-case development and execution for avionics display systems. This experience informs how I investigate interface mismatches, reproduce failures and separate a component test from a system-level result. Product-specific configurations, test procedures and operational data are not included here.

**中文：** 航空系统集成测试经历使我形成了接口检查、故障复现和逐项验证的工作习惯。这些能力也用于当前机器人项目的集成与问题定位。

## Research synthesis and invention work

I have contributed to research writing on multi-agent collaborative decision-making and industrial foundation models, alongside invention work in timing and mobile robotics. The [research record](../research/README.md) separates published, granted and in-progress work, and states my authorship or inventor role.

**中文：** 研究写作与发明工作强调文献组织、问题分解和证据表达。已发表、已授权与进行中的成果分别列示，不把研究原型写成已验收的工业系统。
