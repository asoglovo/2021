import fileinput
from collections import Counter

from segment import parse_segment, points_in_segment

if __name__ == '__main__':
    intersections_count = Counter()

    for line in fileinput.input():
        segment = parse_segment(line)

        if segment['is_horizontal'] or segment['is_vertical'] or segment['is_45_deg']:
            intersections_count.update(
                points_in_segment(segment)
            )

    total = len([count for count in intersections_count.values() if count >= 2])
    print(f'Points where two or more lines intersect: {total}')
