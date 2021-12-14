from unittest import TestCase

from polymer import polymerize


class TestPolymer(TestCase):

    rules = {
        'CH': 'B',
        'HH': 'N',
        'CB': 'H',
        'NH': 'C',
        'HB': 'C',
        'HC': 'B',
        'HN': 'C',
        'NN': 'C',
        'BH': 'H',
        'NC': 'B',
        'NB': 'B',
        'BN': 'B',
        'BB': 'N',
        'BC': 'B',
        'CC': 'N',
        'CN': 'C'
    }

    cases = (
        ('NN', 1, 'NCN'),
        ('NCN', 1, 'NBCCN'),
        ('NN', 2, 'NBCCN'),
        ('NNCB', 1, 'NCNBCHB'),
        ('NNCB', 2, 'NBCCNBBBCBHCB'),
        ('NNCB', 3, 'NBBBCNCCNBBNBNBBCHBHHBCHB'),
        ('NNCB', 4, 'NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB'),
    )

    def test_polymerize(self):
        for in_poly, steps, expected_poly in self.cases:
            self.assertEqual(
                expected_poly,
                polymerize(in_poly, self.rules, steps)
            )
