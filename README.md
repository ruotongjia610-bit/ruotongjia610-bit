# Ruotong Jia

AI algorithm engineer working on humanoid robot control, embodied intelligence, and mobile robot navigation.

## Selected project

### Robot Action and Tour Navigation

A Python implementation of reusable robot action control and tour-navigation mission logic.

- Smooth joint-space trajectories with bounded duration.
- Action lifecycle with pause, resume, completion, stop, and fault states.
- Joint-limit and per-step motion protection.
- Waypoint sequencing with arrival tolerance and completion events.
- Velocity limiting, pause/cancel handling, and sensor-health checks.
- Deterministic unit tests and a small CI workflow.

The implementation is organized in the [robot_control package](robot_control/README.md).

## Repository layout

```text
robot_control/action/        trajectory, safety, and action state machine
robot_control/navigation/    route, mission, sensor, and velocity modules
config/                      example action and route configuration
tests/                       deterministic unit tests
docs/                        architecture notes
```

## Test

```bash
python -m unittest discover -s tests -p 'test_*.py'
```
