# Ruotong Jia

AI algorithm engineer working on humanoid robot control, embodied intelligence, and mobile robot navigation.

## Robot Action Development

- Reusable upper-body action states
- Smooth joint-space interpolation
- Pause, resume, completion, and safety-stop transitions
- Motion limits for stable execution

## Tour Navigation

- ROS 2/Nav2 route management
- Goal arrival events and cancellation
- Pause and resume handling
- Velocity limiting and sensor-fault shutdown

## Repository

The `robot_control` package contains the control modules. Tests are in `tests/`.

Run the tests with:

```bash
python -m unittest discover -s tests -p 'test_*.py'
```
