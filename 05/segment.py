import re
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
    }


def points_in_segment(segment: Dict) -> List[Point]:
    x1, y1 = segment['start']
    x2, y2 = segment['end']

    if segment['is_horizontal']:
        start = min(x1, x2)
        end = max(x1, x2) + 1

        return [(x, y1) for x in range(start, end)]

    elif segment['is_vertical']:
        start = min(y1, y2)
        end = max(y1, y2) + 1

        return [(x1, y) for y in range(start, end)]

    else:
        # For now, diagonal segments aren't supported
        return []
