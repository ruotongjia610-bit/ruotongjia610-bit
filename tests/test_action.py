import unittest

from robot_control.action.safety import JointLimit, SafetyConfig, SafetyMonitor
from robot_control.action.state_machine import ActionController, ActionState
from robot_control.action.trajectory import TrajectoryConfig


class ActionControllerTests(unittest.TestCase):
    def setUp(self):
        safety = SafetyMonitor(SafetyConfig({"shoulder": JointLimit(-1.0, 1.0)}))
        self.controller = ActionController(safety)

    def test_reaches_target_and_emits_complete(self):
        self.controller.start({"shoulder": 0.0}, {"shoulder": 0.8}, TrajectoryConfig(1.0))
        for _ in range(10):
            pose = self.controller.step(0.1)
        self.assertAlmostEqual(pose["shoulder"], 0.8, places=6)
        self.assertEqual(self.controller.state, ActionState.COMPLETE)

    def test_pause_and_resume_hold_progress(self):
        self.controller.start({"shoulder": 0.0}, {"shoulder": 0.8})
        before_pause = self.controller.step(0.2)
        self.controller.pause()
        self.assertEqual(self.controller.step(0.5), before_pause)
        self.controller.resume()
        self.assertNotEqual(self.controller.step(0.2), before_pause)

    def test_limit_violation_enters_fault(self):
        self.controller.start({"shoulder": 0.0}, {"shoulder": 2.0})
        self.assertEqual(self.controller.state, ActionState.FAULT)


if __name__ == "__main__":
    unittest.main()

