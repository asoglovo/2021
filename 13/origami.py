import fileinput
import re
from typing import List, Set, Tuple

Dot = Tuple[int, int]
Dots = Set[Dot]

horizontal_fold_re = re.compile(r'^x=(\d+)$')
vertical_fold_re = re.compile(r'^y=(\d+)$')


def read_input() -> Tuple[Dots, List[str]]:
    lines = [line.strip() for line in fileinput.input()]
    sep_index = lines.index('')

    dots = [
        tuple(map(int, coords.split(',')))
        for coords in lines[:sep_index]
    ]
    instructions = [
        instruction.replace('fold along ', '')
        for instruction in lines[sep_index + 1:]
    ]

    return set(dots), instructions


def fold_along(dots: Dots, instruction: str) -> Dots:
    """
    Folds the given dots along the given instruction.
    """
    if match := horizontal_fold_re.match(instruction):
        x = int(match.group(1))
        return __horizontal_fold(dots, x)

    elif match := vertical_fold_re.match(instruction):
        y = int(match.group(1))
        return __vertical_fold(dots, y)

    else:
        raise ValueError(f'Invalid instruction: {instruction}')


def __horizontal_fold(dots: Dots, x_axis: int) -> Dots:
    """
    Folds the right half left at the given x coordinate.
    """
    return set([
        (2 * x_axis - x, y) if x > x_axis else (x, y)
        for x, y in dots
    ])


def __vertical_fold(dots: Dots, y_axis: int) -> Dots:
    """
    Folds the bottom half up at the given y coordinate.
    """
    return set([
        (x, 2 * y_axis - y) if y > y_axis else (x, y)
        for x, y in dots
    ])


def print_dots(dots: Dots, width: int, height: int) -> None:
    """
    Prints the given dots in a grid of the given width and height.
    """
    for y in range(height):
        row = ['#' if (x, y) in dots else '.' for x in range(width)]
        print(''.join(row))
