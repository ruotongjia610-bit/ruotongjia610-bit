# Robot Action and Tour Navigation

Python modules for humanoid action control and tour-navigation logic.

## Contents

- `robot_control/gesture_controller.py`: action state machine and smooth pose interpolation
- `robot_control/navigation_controller.py`: route sequencing, arrival events, velocity limits, and fault handling
- `tests/test_robot_control.py`: unit tests for action and navigation behavior

## Test

```bash
python -m unittest discover -s tests -p 'test_*.py'
```
