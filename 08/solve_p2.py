import fileinput
from typing import List, Tuple

from display import (apply_mapping_to_segments, find_segments_mapping,
                     segments_to_number)


def parse_line(line: str) -> Tuple[List[str], List[str]]:
    patterns, output = line.strip().split(' | ')
    patterns, output = patterns.split(), output.split()

    return patterns, output


if __name__ == '__main__':
    numbers_sum = 0

    for line in fileinput.input():
        patterns, output = parse_line(line)

        mapping = find_segments_mapping(patterns)
        corrected_segments = apply_mapping_to_segments(mapping, output)
        number = segments_to_number(corrected_segments)

        numbers_sum += number

    print(f'All numbers sum: {numbers_sum}')
