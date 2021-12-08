from itertools import permutations
from typing import Dict, List, Set

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
all_permutations = list(permutations(all_letters, len(all_letters)))

digits_by_length = {
    2: (one,),
    3: (seven,),
    4: (four,),
    5: (two, three, five),
    6: (zero, six, nine),
    7: (eight,),
}


def identify_output_number(patterns: List[str], output: List[str]) -> int:
    """
    Analyzes the given patterns, and figures out the wire connections in the four 
    output seven-segment displays, from which the number can be derived.
    """
    mappings = __compute_feasible_mappings(patterns)
    valid_mappings = [
        mapping for mapping in mappings if __is_valid_mapping(patterns, mapping)
    ]
    assert len(valid_mappings) == 1, 'More than one valid mapping found'

    return __number_from_mapped_output(valid_mappings[0], output)


def __compute_feasible_mappings(patterns: List[str]):
    """
    From all the possible permutations which can be used as mappings, this function
    returns only those that are feasible given the input patterns.
    """
    permutations = all_permutations.copy()
    mappings = __search_possible_letter_mappings(patterns)

    for i, letter in enumerate(all_letters):
        permutations = [perm for perm in permutations
                        if perm[i] in mappings[letter]]

    return permutations


def __search_possible_letter_mappings(patterns: List[str]) -> Dict[str, Set[str]]:
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


def __is_valid_mapping(patterns: List[str], mapping: List[str]) -> bool:
    """
    Determines whether the given mapping produces all valid patterns.
    """
    mapped_patterns = [__map_pattern(pattern, mapping) for pattern in patterns]

    return all(__is_valid_pattern(pattern) for pattern in mapped_patterns)


def __map_pattern(pattern: str, mapping: List[str]) -> str:
    return ''.join(
        [mapping[all_letters.index(letter)] for letter in pattern]
    )


def __is_valid_pattern(pattern: str) -> bool:
    return set(pattern) in all_numbers


def __number_from_mapped_output(mapping: List[str], output: List[str]) -> int:
    segments_list = [__map_pattern(pattern, mapping) for pattern in output]
    return int(''.join([__digit_from_segments(segments) for segments in segments_list]))


def __digit_from_segments(segments: List[str]) -> str:
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
