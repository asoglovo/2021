from itertools import permutations
from typing import Dict, List, Sequence, Set, Tuple

zero = set('abcefg')
one = set('cf')
two = set('acdeg')
three = set('acdfg')
four = set('bcdf')
five = set('abdfg')
six = set('abdefg')
seven = set('acf')
eight = set('abcdefg')
nine = set('abcdfg')

all_numbers = (zero, one, two, three, four, five, six, seven, eight, nine)
all_letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g')
all_possible_mappings = list(permutations(all_letters, len(all_letters)))

digits_by_length = {
    2: (one,),
    3: (seven,),
    4: (four,),
    5: (two, three, five),
    6: (zero, six, nine),
    7: (eight,),
}

SegmentsMapping = Tuple[str, ...]
Segments = str


def find_segments_mapping(patterns: List[Segments]) -> SegmentsMapping:
    """
    Given the measured segment patterns, finds the mapping of the segments such that
    all of the mapped patterns exist as a valid digit.
    """
    mappings = __compute_feasible_mappings(patterns)
    return next(
        mapping for mapping in mappings if __is_valid_mapping(patterns, mapping)
    )


def apply_mapping_to_segments(
    mapping: SegmentsMapping,
    segments_list: List[Segments]
) -> List[Segments]:
    """
    Retuns a list with the mapped segments: the result of applying the given mapping
    to each of the input segments.
    """
    return [__map_segments(segments, mapping) for segments in segments_list]


def segments_to_number(segments_list: List[Segments]) -> int:
    """
    Computes the number represented by the given segments, where each segment
    is a single digit.

    For example, the segments ['acdfg', 'abcdefg', 'abdefg'] would yield the 
    number 386.
    """
    digits = [__digit_from_segments(segments) for segments in segments_list]
    return int(''.join(digits))


def __compute_feasible_mappings(patterns: List[Segments]) -> List[SegmentsMapping]:
    """
    From all the possible mappings which can be used, this function returns only 
    those that are feasible given the input patterns.
    """
    all_mappings = all_possible_mappings.copy()
    possible_mappings = __possible_letter_mappings(patterns)

    for i, letter in enumerate(all_letters):
        valid_outputs = possible_mappings[letter]
        all_mappings = [
            mapping for mapping in all_mappings if mapping[i] in valid_outputs
        ]

    return all_mappings


def __possible_letter_mappings(patterns: List[str]) -> Dict[str, Set[str]]:
    """
    Given the read patterns, computes all possible letter mappings.

    The first letter in the tuple is the letter in the pattern and the second
    is the possible mapping. The mapping consists in changing the first letter
    appearance in a pattern by the second one.
    """
    possible_mappings = dict(
        [(pattern, set.union(*digits_by_length[len(pattern)]))
         for pattern in patterns]
    )

    letter_mappings = []
    for letter in all_letters:
        sets = [matches for pattern, matches in possible_mappings.items()
                if letter in pattern]
        letter_mappings.append(
            (letter, set.intersection(*sets))
        )

    return dict(letter_mappings)


def __is_valid_mapping(
    patterns: List[Segments],
    mapping: SegmentsMapping
) -> bool:
    """
    Determines whether the given mapping produces all valid patterns.
    """
    mapped_patterns = [__map_segments(pattern, mapping)
                       for pattern in patterns]

    return all(__is_valid_pattern(pattern) for pattern in mapped_patterns)


def __map_segments(segments: Segments, mapping: SegmentsMapping) -> str:
    return ''.join(
        [mapping[all_letters.index(letter)] for letter in segments]
    )


def __is_valid_pattern(pattern: Segments) -> bool:
    return set(pattern) in all_numbers


def __digit_from_segments(segments: Segments) -> str:
    segments_set = set(segments)

    if segments_set == zero:
        return '0'
    elif segments_set == one:
        return '1'
    elif segments_set == two:
        return '2'
    elif segments_set == three:
        return '3'
    elif segments_set == four:
        return '4'
    elif segments_set == five:
        return '5'
    elif segments_set == six:
        return '6'
    elif segments_set == seven:
        return '7'
    elif segments_set == eight:
        return '8'
    elif segments_set == nine:
        return '9'
    else:
        raise ValueError(f'Invalid segments: {segments}')
