from unittest import TestCase

from syntax import (chars_to_complete_chunk, compute_completion_score,
                    compute_line_syntax_error_score,
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

    def test_complete_chunk(self):
        tests = [
            ('[({(<(())[]>[[{[]{<()<>>', '}}]])})]'),
            ('[(()[<>])]({[<{<<[]>>(', ')}>]})'),
            ('(((({<>}<{<{<>}{[]{[]{}', '}}>}>))))'),
            ('{<[[]]>}<{[{[{[]{()[[[]', ']]}}]}]}>'),
            ('<{([{{}}[<[[[<>{}]]]>[]]', '])}>'),
        ]

        for line, expected_completion in tests:
            self.assertEqual(
                expected_completion,
                chars_to_complete_chunk(line)
            )

    def test_completion_score(self):
        tests = [
            ('}}]])})]', 288957),
            (')}>]})', 5566),
            ('}}>}>))))', 1480781),
            (']]}}]}]}>', 995444),
            ('])}>', 294),
        ]

        for completion, expected_score in tests:
            self.assertEqual(
                expected_score,
                compute_completion_score(completion)
            )
