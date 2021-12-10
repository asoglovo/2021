from unittest import TestCase

from syntax import (compute_line_syntax_error_score,
                    find_first_illegal_character)


class SyntaxTest(TestCase):

    def test_find_first_illegal_character(self):
        line = '{([(<{}[}>{[]{[(<()>'
        self.assertEqual(
            (8, '}'),
            find_first_illegal_character(line)
        )

    def test_compute_line_syntax_error_score(self):
        line = '{([(<{}[}>{[]{[(<()>'
        self.assertEqual(
            1197,
            compute_line_syntax_error_score(line)
        )
