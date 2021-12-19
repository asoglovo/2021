from unittest import TestCase

from chiton import find_safest_path
from riskmap import RiskMap
from extended_riskmap import ExtendedRiskMap


class ChitonTest(TestCase):

    risk_map_data = [
        [1, 1, 6, 3, 7, 5, 1, 7, 4, 2],
        [1, 3, 8, 1, 3, 7, 3, 6, 7, 2],
        [2, 1, 3, 6, 5, 1, 1, 3, 2, 8],
        [3, 6, 9, 4, 9, 3, 1, 5, 6, 9],
        [7, 4, 6, 3, 4, 1, 7, 1, 1, 1],
        [1, 3, 1, 9, 1, 2, 8, 1, 3, 7],
        [1, 3, 5, 9, 9, 1, 2, 4, 2, 1],
        [3, 1, 2, 5, 4, 2, 1, 6, 3, 9],
        [1, 2, 9, 3, 1, 3, 8, 5, 2, 1],
        [2, 3, 1, 1, 9, 4, 4, 5, 8, 1]
    ]
    risk_map = RiskMap(risk_map_data)
    extended_risk_map = ExtendedRiskMap(risk_map_data, 5)
    shortest_path = [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3),
                     (2, 4), (2, 5), (2, 6), (3, 6), (3, 7), (4, 7), (5, 7),
                     (5, 8), (6, 8), (7, 8), (8, 8), (8, 9), (9, 9)]

    def test_find_path(self):
        path, risk = find_safest_path(self.risk_map)

        self.assertEqual(self.shortest_path, path)
        self.assertEqual(40, risk)

    def test_find_small_path(self):
        risk_map = RiskMap([
            [5, 1, 1, 3],
            [3, 3, 1, 3],
            [3, 1, 1, 3],
            [3, 1, 1, 5]
        ])
        shortest_path = [(0, 0), (0, 1), (0, 2), (1, 2),
                         (2, 2), (3, 2), (3, 3)]

        path, risk = find_safest_path(risk_map)

        self.assertEqual(shortest_path, path)
        self.assertEqual(10, risk)

    def test_read_expandeded_risk_map(self):
        tests = [
            ((0, 49), 6),
            ((1, 49), 6),
            ((12, 49), 4),
            ((10, 10), 3),
        ]

        for pos, expected in tests:
            self.assertEqual(
                expected,
                self.extended_risk_map[pos]
            )

    def test_find_path_in_extended_map(self):
        _, risk = find_safest_path(self.extended_risk_map)
        self.assertEqual(315, risk)
