# 贾若彤 · Ruotong Jia

**机器人 · 多模态学习 · 可靠自主系统**

[English](README.md) · [项目介绍](portfolio/README.md) · [论文与专利](research/README.md)

我是一名算法工程师，主要从事机器人感知、自主导航和模型适配。此前的物理建模与系统集成测试经历，使我习惯从假设、接口和实验结果出发分析问题，把算法实现与系统行为联系起来。

近期重点是人形机器人导航中的点云处理、重定位、局部避障和安全停车，同时具备机器人交互动作开发、语言模型与视觉语言模型适配经验。

## 项目成果

| 项目 | 我的贡献 | 已有证据与当前状态 |
|---|---|---|
| [机器人感知与自主导航](portfolio/robot-navigation.md) | 传感器输入核验、点云处理、重定位、局部避障与安全停车 | 完成导航仿真、离线回归和接口检查；完整真机自主导航仍在验证。这里提供公开概述。 |
| [人形机器人交互动作](portfolio/README.md#humanoid-interaction-actions) | 动作状态、关键帧过渡、暂停恢复，以及与已有步态控制器的集成 | 部分动作已进行真机调试；另有可检查的[通用公开示例](projects/humanoid-robot-control/README.md)与自动化测试。 |
| [AGV 工勘问答](projects/llm-field-survey-qa/README.md) | 领域问答整理、Qwen-7B 的 QLoRA 适配、易混淆事实与拒答样本、推理接口 | 公开重构版本包含数据检查与模拟推理；不公开原始训练资料或内部指标。 |
| [视觉语言模型图像描述](portfolio/README.md#vision-language-image-captioning) | Qwen2-VL-2B-Instruct 适配、图文对话格式整理、不同图像尺寸的批次处理 | 基于 COCO 2014 的个人训练项目；不将训练损失下降写成独立测试集上的性能提升。 |
| [实时仿真与参数辨识](portfolio/README.md#real-time-simulation-and-parameter-identification) | 定时实现与测试、数值参数估计、残差分析 | 参与的定时发明专利已授权；历史工程实现与数据不公开。 |
| [流体力学与科学计算](portfolio/README.md#fluid-mechanics-and-scientific-computing) | 轴承微结构的 CFD 建模与对比分析 | 相关论文发表于《润滑与密封》，本人为第二作者。 |

## 论文与专利

- **已发表论文：** 不同表面微结构条件下的静压轴承油膜流动研究，《润滑与密封》，2024 年，第二作者。[DOI](https://doi.org/10.3969/j.issn.0254-0150.2024.01.004)。
- **已授权发明专利：** Windows 系统实时仿真高精度定时，**CN119473492B**，第二发明人，2025 年 10 月 10 日授权。[公开专利记录](https://patents.google.com/patent/CN119473492B/en)。
- **审稿中的稿件：** 智能制造中的多智能体协同决策综述、工业基础模型 Perspective；与已发表论文分开列示。
- **进行中的发明申请：** 三项涉及机器人感知导航与设备健康监测的工作，未公开的技术方案不在本仓库展示。

[查看研究主题、作者贡献与具体状态](research/README.md)

## 我的工作方式

- **连接算法与系统：** 将传感器数据、坐标关系、定位、任务状态和执行接口作为一条完整链路分析。
- **验证异常行为：** 除成功案例外，检查断流、无效观测、状态切换和恢复过程。
- **让结果可解释：** 说明数据、基线与指标，区分合成实验、接口检查和真机验证。
- **明确个人贡献：** 将自己的算法与集成工作和原厂控制器、预训练模型、开源组件区分清楚。

## 技术工具

| 方向 | 使用过的工具与方法 |
|---|---|
| 机器人 | ROS 2、Nav2、MuJoCo、RViz、点云处理、状态机 |
| 模型适配 | PyTorch、Transformers、PEFT、LoRA/QLoRA、Qwen、Qwen2-VL、SwanLab |
| 建模与分析 | NumPy、Pandas、MATLAB、ANSYS Fluent、数值优化 |
| 软件工程 | Python、C++、Git、自动化测试、Linux/Windows 集成 |

## 背景

河北工业大学能源动力工程专业，工程学学士。工程经历涵盖发动机仿真、航空系统集成测试、工业 AI 和人形机器人开发。

曾获第十四届、第十五届全国大学生节能减排竞赛国家三等奖。

## 公开代码入口

- [机器人动作与导航通用示例](projects/humanoid-robot-control/README.md)
- [AGV 问答公开重构](projects/llm-field-survey-qa/README.md)
- [自动化检查](https://github.com/ruotongjia610-bit/ruotongjia610-bit/actions/workflows/tests.yml)

本仓库展示公开示例、已公开研究引用与工程工作概述，不包含公司实现、部署细节、地图、私有数据集或未公开发明方案。

**联系邮箱：** [ruotongjia610@gmail.com](mailto:ruotongjia610@gmail.com)

*更新于 2026 年 10 月 16 日，研究与验证状态以此日期为准。*
