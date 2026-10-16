# Robot perception and autonomous navigation

[Home](../README.md) · [All projects](README.md)

## The engineering problem

Humanoid tour navigation connects perception, localization, route execution and an existing walking controller. A planned route alone is insufficient: the system must recognize when its inputs or position estimate are unreliable, stop predictably and resume only under valid conditions.

My focus is point-cloud fusion, relocalization, local obstacle avoidance and safe stopping on the Bake humanoid robot platform (八客机器人). Work on calibration, maps, global routes, tour scheduling and the walking interface is shared across the team; those modules are not presented as my sole contribution.

## My contribution

| Area | Work I carried out | Engineering purpose |
|---|---|---|
| Perception inputs | Investigated sensor data validity and consistency; developed point-cloud processing and fusion logic | Avoid treating incomplete or unreliable observations as dependable free-space evidence. |
| Relocalization | Developed localization checks and exercised incorrect or unavailable pose cases | Establish whether the robot has enough evidence to navigate from its estimated position. |
| Local navigation | Integrated obstacle observations with local avoidance and task execution interfaces | Respond to obstacles while retaining an explicit stopping behavior. |
| Safety and recovery | Developed checks for invalid or stale inputs and examined stop/recovery transitions | Make interruption and recovery predictable, rather than treating every stop as a planning failure. |
| Verification | Built offline and interface checks, investigated failures and documented validation limits | Separate algorithm behavior, communication problems and physical execution effects. |

## Evidence and current status

- **Navigation simulation:** exercised goal reaching, obstacle detours and sensor-loss handling. These results support the navigation software behavior in the tested setup.
- **Offline and interface verification:** exercised perception inputs, localization decisions, task transitions and stopping behavior with repeatable inputs.
- **Physical integration:** performed sensor bring-up and data checks. Sensor stability, calibration and complete physical navigation remain work in progress.

No real-world navigation accuracy, stopping distance or unattended-operation capability is claimed from those software tests. The existing locomotion controller is a platform component; training a new walking policy is not my contribution here.

## What can be inspected publicly

The existing [generic action and mission example](../projects/humanoid-robot-control/README.md) illustrates state machines, waypoint sequencing, input freshness and command gating. It is not a release of the company's navigation implementation and does not reproduce the complete current system.

The current industrial code, calibration values, maps, device details, deployment configuration and internal test artifacts remain outside this repository.

## 中文概述

这项工作的目标是在八客机器人上实现可靠自主导览。我的主责是点云融合、重定位、局部避障与安全停车：核对感知输入是否有效，判断定位结果是否足以支持运动，将障碍处理接入导航，并检查异常停止后的恢复行为。

已有导航仿真、离线回归与接口验证，也开展了真机传感器接入和数据核对。完整真机自主导航仍在推进，不能把软件测试通过当作真实到点精度或制动能力已验收。标定、地图、全局路线、导览调度和原厂行走接口属于团队协作范围。

这里通过问题拆解、贡献和验证范围说明我的能力，不公开公司内部实现。公开的动作与任务示例是通用演示，不是公司导航系统的源代码。
