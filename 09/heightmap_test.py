from unittest import TestCase

from heightmap import find_basin_size, find_low_points


class HeightmapTest(TestCase):

    heightmap = [
        [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
        [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
        [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
        [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
        [9, 8, 9, 9, 9, 6, 5, 6, 7, 8],
    ]

    def test_smoke(self):
        low_points = find_low_points(self.heightmap)

        self.assertEqual(
            [
                {'pos': (0, 1), 'height': 1, 'risk': 2},
                {'pos': (0, 9), 'height': 0, 'risk': 1},
                {'pos': (2, 2), 'height': 5, 'risk': 6},
                {'pos': (4, 6), 'height': 5, 'risk': 6},
            ],
            low_points
        )

    def test_find_basin(self):
        low_point_one = {'pos': (0, 1)}
        self.assertEqual(
            3,
            find_basin_size(self.heightmap, low_point_one)
        )

        low_point_two = {'pos': (0, 9)}
        self.assertEqual(
            9,
            find_basin_size(self.heightmap, low_point_two)
        )

        low_point_three = {'pos': (2, 2)}
        self.assertEqual(
            14,
            find_basin_size(self.heightmap, low_point_three)
        )
