import fileinput
from collections import Counter, defaultdict
from typing import Dict, List, Tuple

InsertionRules = Dict[str, str]
Polymer = str
CompressedPolymer = Tuple[int, Dict[Polymer, List[int]]]


def read_input() -> Tuple[str, InsertionRules]:
    template, _, *rules = fileinput.input()
    rules = dict([rule.strip().split(' -> ') for rule in rules])

    return template.strip(), rules


def polymerize(polymer: Polymer, rules: InsertionRules) -> Polymer:
    """
    Produces a new polymer chain result of applying the insertion rules to the input polymer.
    The resulting polymer has a length of 2n - 1, being n the length of the input polymer.
    """
    length, compressed = compress_polymer(polymer)
    extended = dict(
        [(pattern[0] + rules[pattern] + pattern[1], indices)
         for pattern, indices in compressed.items()]
    )

    return decompress_polymer((length, extended))


def polymerize_steps(polymer: Polymer, rules: InsertionRules, steps: int) -> Polymer:
    compressed = compress_polymer(polymer)

    for step in range(steps):
        compressed = __polymerize_compressed(compressed, rules)
        if step % 10 == 0:
            print(step, ':', compressed)

    return decompress_polymer(compressed)


def __polymerize_compressed(
    polymer: CompressedPolymer,
    rules: InsertionRules
) -> CompressedPolymer:
    length, compressed = polymer
    polymerized = defaultdict(list)

    for polymer, indices in compressed.items():
        one, two = __expand_polymer(polymer, rules)

        polymerized[one].extend([2 * i for i in indices])
        polymerized[two].extend([2 * i + 1 for i in indices])

    return (2 * length, polymerized)


def __expand_polymer(polymer: Polymer, rules: InsertionRules) -> Tuple[Polymer, Polymer]:
    assert len(polymer) == 2, 'Polymer must be of length 2'
    middle = rules[polymer]

    return (polymer[0] + middle, middle + polymer[1])


def polymer_score(polymer: Polymer):
    count = Counter(polymer)
    most_common, *_, least_common = count.most_common()
    score = most_common[1] - least_common[1]

    return most_common, least_common, score


def compress_polymer(polymer: Polymer) -> CompressedPolymer:
    pairs = __parwise(polymer)
    compressed = defaultdict(list)

    for i, pair in enumerate(pairs):
        compressed[pair].append(i)

    return len(pairs), compressed


def decompress_polymer(polymer: CompressedPolymer) -> Polymer:
    length, compressed = polymer
    decompressed = [None] * length

    for pattern, indices in compressed.items():
        for index in indices:
            decompressed[index] = pattern[:-
                                          1] if index < length - 1 else pattern

    return ''.join(decompressed)


def __parwise(polymer: Polymer):
    return [polymer[i-1:i+1] for i in range(1, len(polymer))]
