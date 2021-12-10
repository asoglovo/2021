from typing import Tuple

score = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}
completion_score = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}

opening_chars = set(['(', '[', '{', '<'])
closing_chars = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}
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


def __is_corrupted_line(line: str) -> bool:
    """
    A line is corrupted if it contains any illegal character.
    """
    _, char = find_first_illegal_character(line)
    return char is not None


def chars_to_coplete_chunk(line: str) -> str:
    if __is_corrupted_line(line):
        return ''

    simplified = __simplify_line(line)
    return ''.join(
        reversed([closing_chars[char] for char in simplified])
    )


def __simplify_line(line: str) -> str:
    if not __can_simplify_line(line):
        return line

    simplified = line \
        .replace('()', '') \
        .replace('[]', '') \
        .replace('{}', '') \
        .replace('<>', '')

    return __simplify_line(simplified)


def __can_simplify_line(line: str) -> bool:
    return any(chunk in line for chunk in chunks)


def compute_completion_score(completion: str) -> int:
    """
    Start with a total score of 0. Then, for each character, multiply the total score 
    by 5 and then increase the total score by the point value given for the completion
    scores dictionary.
    """
    score = 0
    for char in completion:
        score *= 5
        score += completion_score[char]

    return score


def __is_closed_chunk(open: str, close: str) -> bool:
    """
    Checks if a chunk made of the opening and closing characters is closed.
    """
    return f'{open}{close}' in chunks
