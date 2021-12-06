import unittest

from fish import days_when_fish_produced, spawn_days, total_fish_produced


class FishTest(unittest.TestCase):

    simulation_duration = 20

    def test_total_fish_produced(self):
        expected = 6
        actual = total_fish_produced(3, self.simulation_duration)

        self.assertEqual(expected, actual)

    def test_days_when_fish_produced(self):
        self.assertEqual(
            [4, 11, 18],
            days_when_fish_produced(3, self.simulation_duration)
        )

    def test_spawn_days(self):
        self.assertEqual([13, 20], spawn_days(4, self.simulation_duration))
        self.assertEqual([20], spawn_days(11, self.simulation_duration))
        self.assertEqual([], spawn_days(18, self.simulation_duration))
