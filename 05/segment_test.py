import unittest
from segment import parse_segment, points_in_segment


class SegmentTest(unittest.TestCase):

    def test_get_45_deg_points_descending(self):
        segment = parse_segment('6,4 -> 2,0')
        points = points_in_segment(segment)

        self.assertTrue(segment['is_45_deg'])
        self.assertEqual(
            [(6, 4), (5, 3), (4, 2), (3, 1), (2, 0)],
            points
        )

    def test_get_45_deg_points_ascending(self):
        segment = parse_segment('2,0 -> 6,4')
        points = points_in_segment(segment)

        self.assertTrue(segment['is_45_deg'])
        self.assertEqual(
            [(2, 0), (3, 1), (4, 2), (5, 3), (6, 4)],
            points
        )

    def test_get_minus_45_deg_points(self):
        segment = parse_segment('8,0 -> 0,8')
        points = points_in_segment(segment)

        self.assertTrue(segment['is_45_deg'])
        self.assertEqual(
            [(8, 0), (7, 1), (6, 2), (5, 3), (4, 4),
             (3, 5), (2, 6), (1, 7), (0, 8)],
            points
        )
