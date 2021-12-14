from unittest import TestCase

from polymer import (compress_polymer, decompress_polymer, polymerize,
                     polymerize_steps)


class TestPolymer(TestCase):

    rules = {'CH': 'B', 'HH': 'N', 'CB': 'H', 'NH': 'C', 'HB': 'C', 'HC': 'B', 'HN': 'C', 'NN': 'C',
             'BH': 'H', 'NC': 'B', 'NB': 'B', 'BN': 'B', 'BB': 'N', 'BC': 'B', 'CC': 'N', 'CN': 'C'}

    compressed = (
        8,
        {'NC': [0, 7], 'CN': [1], 'NB': [2], 'BC': [3],
         'CH': [4], 'HB': [5], 'BN': [6]}
    )
    decompressed = 'NCNBCHBNC'

    def test_polymerize(self):
        self.assertEqual(
            'NCNBCHB',
            polymerize('NNCB', self.rules)
        )
        self.assertEqual(
            'NBCCNBBBCBHCB',
            polymerize('NCNBCHB', self.rules)
        )
        self.assertEqual(
            'NBBBCNCCNBBNBNBBCHBHHBCHB',
            polymerize('NBCCNBBBCBHCB', self.rules)
        )

    def test_compress_polymer(self):
        self.assertEqual(
            self.compressed,
            compress_polymer(self.decompressed)
        )

    def test_decompress_polymer(self):
        self.assertEqual(
            self.decompressed,
            decompress_polymer(self.compressed)
        )

    def test_polimerize_steps(self):
        self.assertEqual(
            'NBBBCNCCNBBNBNBBCHBHHBCHB',
            polymerize_steps('NNCB', self.rules, 3)
        )
