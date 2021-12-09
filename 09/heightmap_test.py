from unittest import TestCase

from heightmap import find_low_points


class SmokeTest(TestCase):

    def test_smoke(self):
        heightmap = [
            [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
            [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
            [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
            [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
            [9, 8, 9, 9, 9, 6, 5, 6, 7, 8],
        ]
        low_points = find_low_points(heightmap)

        self.assertEqual(
            [
                {'pos': (0, 1), 'height': 1, 'risk': 2},
                {'pos': (0, 9), 'height': 0, 'risk': 1},
                {'pos': (2, 2), 'height': 5, 'risk': 6},
                {'pos': (4, 6), 'height': 5, 'risk': 6},
            ],
            low_points
        )
