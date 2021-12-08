from unittest import TestCase

from display import (apply_mapping_to_segments, find_segments_mapping,
                     segments_to_number)


class DisplayTest(TestCase):

    def test_find_mapping(self):
        patterns = ['acedgfb', 'cdfbe', 'gcdfa', 'fbcad',
                    'dab', 'cefabd', 'cdfgeb', 'eafb', 'cagedb', 'ab']
        expected = ('c', 'f', 'g', 'a', 'b', 'd', 'e')

        self.assertEqual(expected, find_segments_mapping(patterns))

    def test_apply_mapping_to_digits(self):
        mapping = ('c', 'f', 'g', 'a', 'b', 'd', 'e')
        output = ['cdfeb', 'fcadb', 'cdfeb', 'cdbaf']
        expected = ['gadbf', 'dgcaf', 'gadbf', 'gafcd']

        self.assertEqual(expected, apply_mapping_to_segments(mapping, output))

    def test_digits_to_number(self):
        digits = ['gadbf', 'dgcaf', 'gadbf', 'gafcd']
        expected = 5353

        self.assertTrue(expected, segments_to_number(digits))
