import re
from math import copysign
from typing import Dict, List, Tuple

Point = Tuple[int, int]
segment_re = re.compile(r'^(\d+),(\d+)\s+->\s+(\d+),(\d+)$')


def parse_segment(line: str):
    match = segment_re.match(line)
    x1, y1, x2, y2 = map(int, match.groups())

    return {
        'start': (x1, y1),
        'end': (x2, y2),
        'is_horizontal': y1 == y2,
        'is_vertical': x1 == x2,
        'is_45_deg': abs(y2 - y1) == abs(x2 - x1)
    }


def points_in_segment(segment: Dict) -> List[Point]:
    if segment['is_horizontal']:
        return __get_horizontal_points(segment)

    elif segment['is_vertical']:
        return __get_vertical_points(segment)

    elif segment['is_45_deg']:
        return get_45_deg_points(segment)

    else:
        raise ValueError('Invalid segment')


def __get_horizontal_points(segment):
    x1, y = segment['start']
    x2, _ = segment['end']

    start = min(x1, x2)
    end = max(x1, x2) + 1

    return [(x, y) for x in range(start, end)]


def __get_vertical_points(segment):
    x, y1 = segment['start']
    _, y2 = segment['end']

    start = min(y1, y2)
    end = max(y1, y2) + 1

    return [(x, y) for y in range(start, end)]


def get_45_deg_points(segment):
    x1, y1 = segment['start']
    x2, y2 = segment['end']

    x_step = 1 if x2 > x1 else -1
    y_step = 1 if y2 > y1 else -1

    return [
        (x, y) for x, y in
        zip(
            range(x1, x2 + x_step, x_step),
            range(y1, y2 + y_step, y_step)
        )
    ]
