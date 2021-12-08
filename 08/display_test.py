from unittest import TestCase

from display import identify_output_number


class DisplayTest(TestCase):

    def test_identify_output_number(self):
        patterns = ['acedgfb', 'cdfbe', 'gcdfa', 'fbcad',
                    'dab', 'cefabd', 'cdfgeb', 'eafb', 'cagedb', 'ab']
        output = ['cdfeb', 'fcadb', 'cdfeb', 'cdbaf']

        self.assertEqual(5353, identify_output_number(patterns, output))
