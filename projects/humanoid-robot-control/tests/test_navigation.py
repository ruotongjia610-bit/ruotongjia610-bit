import unittest

from robot_control.navigation.mission_manager import MissionManager, MissionState
from robot_control.navigation.route_manager import RouteManager, RouteState, Waypoint
from robot_control.navigation.sensor_monitor import SensorMonitor, SensorStatus
from robot_control.navigation.velocity_guard import VelocityCommand, VelocityGuard, VelocityLimits


class NavigationTests(unittest.TestCase):
    def make_mission(self):
        route = RouteManager([Waypoint("lobby", 1.0, 0.0), Waypoint("lab", 2.0, 0.0)])
        sensors = SensorMonitor(timeout_s=0.5)
        guard = VelocityGuard(VelocityLimits(0.3, 0.5))
        mission = MissionManager(route, sensors, guard)
        return mission, sensors

    def test_velocity_is_limited(self):
        guard = VelocityGuard(VelocityLimits(0.3, 0.5))
        self.assertEqual(guard.apply(VelocityCommand(1.0, -1.0)), VelocityCommand(0.3, -0.5))

    def test_stale_sensor_fault_stops_mission(self):
        mission, _ = self.make_mission()
        mission.start()
        event = mission.tick(VelocityCommand(0.2, 0.0), 2.0, now_s=1.0)
        self.assertEqual(event.state, MissionState.FAULT)

    def test_route_completion(self):
        mission, sensors = self.make_mission()
        mission.start()
        sensors.update(0.0)
        mission.tick(VelocityCommand(0.2, 0.0), 0.2, now_s=0.1)
        sensors.update(0.2)
        event = mission.tick(VelocityCommand(0.2, 0.0), 0.2, now_s=0.3)
        self.assertEqual(event.waypoint, "lab")
        self.assertEqual(event.state, MissionState.COMPLETE)

    def test_running_mission_keeps_guarded_command(self):
        mission, sensors = self.make_mission()
        mission.start()
        sensors.update(0.0)
        mission.tick(VelocityCommand(1.0, -1.0), 2.0, now_s=0.1)
        self.assertEqual(mission.last_command, VelocityCommand(0.3, -0.5))


if __name__ == "__main__":
    unittest.main()

