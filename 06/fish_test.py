import unittest

from fish import (spawn_days_from_start_day, spawn_days_from_timer,
                  total_fish_produced)


class FishTest(unittest.TestCase):

    simulation_duration = 20

    def test_total_fish_produced(self):
        expected = 6
        actual = total_fish_produced(3, self.simulation_duration)

        self.assertEqual(expected, actual)

    def test_spawn_days_from_timer(self):
        self.assertEqual(
            [4, 11, 18],
            spawn_days_from_timer(3, self.simulation_duration)
        )

    def test_spawn_days(self):
        self.assertEqual(
            [13, 20],
            spawn_days_from_start_day(4, self.simulation_duration)
        )
        self.assertEqual(
            [20],
            spawn_days_from_start_day(11, self.simulation_duration)
        )
        self.assertEqual(
            [],
            spawn_days_from_start_day(18, self.simulation_duration)
        )
