# Architecture

The project is split into two layers that can be integrated with a robot runtime
without changing the control logic.

```text
action request -> trajectory -> safety monitor -> action state machine

route + sensor health + velocity request -> mission manager
                                      -> route manager
                                      -> velocity guard
```

## Action layer

`PoseTrajectory` generates smooth joint-space targets. `SafetyMonitor` checks
joint limits and the maximum change allowed in one control step.
`ActionController` owns the lifecycle and emits a small event object whenever
the action starts, pauses, resumes, completes, stops, or enters a fault state.

## Navigation layer

`RouteManager` advances through named waypoints using an arrival tolerance.
`SensorMonitor` turns the latest sensor timestamp into a healthy/stale state.
`VelocityGuard` clamps commands and fails closed when the mission is paused or
cancelled. `MissionManager` combines the three components and exposes the last
command that would be sent to a downstream motion interface.

The modules use plain Python data classes and enums so the same logic can be
connected to a simulator, a ROS 2 node, or a vendor-specific adapter.

