import unittest

from robot_control.gesture_controller import ActionStatus, GestureController
from robot_control.navigation_controller import Goal, SafetyGuard, TourRoute, Velocity


class ActionControllerTests(unittest.TestCase):
    def test_gesture_reaches_target_smoothly(self):
        controller = GestureController({"left_shoulder": 0.8}, duration_s=1.0)
        controller.start({"left_shoulder": 0.0})
        first = controller.step(0.1)["left_shoulder"]
        for _ in range(9):
            final = controller.step(0.1)["left_shoulder"]
        self.assertGreater(first, 0.0)
        self.assertAlmostEqual(final, 0.8, places=6)
        self.assertEqual(controller.status, ActionStatus.COMPLETE)

    def test_pause_holds_pose(self):
        controller = GestureController({"head_yaw": 0.5}, duration_s=1.0)
        controller.start({"head_yaw": 0.0})
        pose = controller.step(0.2)
        controller.pause()
        self.assertEqual(controller.step(0.5), pose)


class NavigationControllerTests(unittest.TestCase):
    def test_guard_clamps_velocity(self):
        guard = SafetyGuard(max_linear_mps=0.3, max_angular_rps=0.5)
        self.assertEqual(guard.command(Velocity(1.0, -1.0)), Velocity(0.3, -0.5))

    def test_sensor_fault_stops_command(self):
        guard = SafetyGuard(sensor_healthy=False)
        self.assertEqual(guard.command(Velocity(0.2, 0.1)), Velocity())

    def test_route_advances_once_per_arrival(self):
        route = TourRoute([Goal("lobby", 1.0, 0.0), Goal("lab", 2.0, 0.0)])
        _, event = route.update(Velocity(0.2), at_goal=True)
        self.assertEqual(event, "lobby")
        self.assertEqual(route.active_goal.name, "lab")


if __name__ == "__main__":
    unittest.main()
