# Robot action and tour-navigation reference demos

These small Python examples are a vendor-neutral reconstruction prepared for a
portfolio showcase. They demonstrate the engineering patterns used in the
project without distributing company source code, vendor SDKs, robot models,
calibration data, or real operational logs.

## What the examples show

- Smooth named-joint pose interpolation with a bounded action state machine.
- Pause, resume, completion, and fail-safe stopping for an action controller.
- Tour-goal sequencing with arrival events and cancel handling.
- Velocity limiting and fail-closed behavior when perception is paused or
  unhealthy.
- Unit tests for the control and navigation invariants.

Run the tests with:

```bash
python -m unittest discover -s public_showcase -p 'test_*.py'
```

The examples are reference implementations, not a claim that this repository
contains the company's original deployment code.
