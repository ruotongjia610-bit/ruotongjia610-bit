# Robot Action and Tour Navigation

Python implementation of reusable robot action control and tour-navigation mission logic. The modules separate motion generation, safety checks, route management, sensor health, and command gating so each part can be tested in isolation.

## Features

- Smooth joint-space trajectories with bounded duration and finite-value checks.
- Action lifecycle: start, pause, resume, complete, stop, and fault.
- Joint limits and per-step pose-change protection.
- Waypoint sequencing with arrival tolerance and completion events.
- Velocity limits, pause/cancel handling, and fail-closed sensor monitoring.
- Configuration examples and unit tests for action and navigation behavior.

## Layout

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
