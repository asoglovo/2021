from typing import Tuple

score = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}
opening_chars = set(['(', '[', '{', '<'])
closing_chars = set([')', ']', '}', '>'])
chunks = set(['()', '[]', '{}', '<>'])


def compute_line_syntax_error_score(line: str) -> int:
    """
    Computes the illegal syntax score of a line.
    """
    _, char = find_first_illegal_character(line)
    return score[char] if char else 0


def find_first_illegal_character(line: str) -> Tuple[int, str]:
    """
    Finds the index of the first character and returns a tuple of the index and 
    the character.

    Returns (-1, None) if no wrong character is found.
    """
    chars_stack = []

    for i, char in enumerate(line):
        if char in opening_chars:
            chars_stack.append(char)
        else:
            last = chars_stack[-1]
            if __is_closed_chunk(last, char):
                chars_stack.pop()
            else:
                return i, char

    return -1, None


def __is_closed_chunk(open: str, close: str) -> bool:
    """
    Checks if a chunk made of the opening and closing characters is closed.
    """
    return f'{open}{close}' in chunks
