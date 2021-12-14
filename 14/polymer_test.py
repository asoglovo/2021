from unittest import TestCase
from polymer import polymerize


class TestPolymer(TestCase):

    rules = {'CH': 'B', 'HH': 'N', 'CB': 'H', 'NH': 'C', 'HB': 'C', 'HC': 'B', 'HN': 'C', 'NN': 'C',
             'BH': 'H', 'NC': 'B', 'NB': 'B', 'BN': 'B', 'BB': 'N', 'BC': 'B', 'CC': 'N', 'CN': 'C'}

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
