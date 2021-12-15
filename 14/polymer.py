import fileinput
from collections import Counter, defaultdict
from typing import Dict, Tuple

InsertionRules = Dict[str, str]
Polymer = str


def read_input() -> Tuple[str, InsertionRules]:
    template, _, *rules = fileinput.input()
    rules = dict([rule.strip().split(' -> ') for rule in rules])

    return template.strip(), rules


def polymerize(polymer: Polymer, rules: InsertionRules, steps: int = 1) -> Polymer:
    cache = {}
    hits = 0

    def expand(polymer: Polymer) -> Polymer:
        assert len(polymer) == 2, f'Polymer {polymer} must be of length 2'
        return polymer[0] + rules[polymer] + polymer[1]

    def recur(polymer: Polymer, steps: int) -> Polymer:
        cache_key = (polymer, steps)
        nonlocal hits

        if cache_key in cache:
            hits += 1
            return cache[cache_key]

        if len(polymer) == 2:
            if steps == 1:
                cache[cache_key] = expand(polymer)
                return cache[cache_key]
            else:
                expanded = expand(polymer)
                cache[cache_key] = concat_polymers(
                    recur(expanded[:2], steps - 1),
                    recur(expanded[1:], steps - 1)
                )
                return cache[cache_key]

        cache[cache_key] = concat_polymers(
            recur(polymer[:2], steps),
            recur(polymer[1:], steps)
        )
        return cache[cache_key]

    result = recur(polymer, steps)
    print(f'hits: {hits}')
    return result


def concat_polymers(a: Polymer, b: Polymer) -> Polymer:
    assert a[-1] == b[0], f'Cannot concatenate {a} and {b}'
    return a + b[1:]


def size_after_steps(initial_length: int, steps: int) -> int:
    """
    Calculates the size of the polymer after a given number of steps given the
    initial length of the polymer.
    """
    exp = 2**steps
    return exp * initial_length - exp + 1


def polymer_score(polymer: Polymer):
    count = Counter(polymer)
    most_common, *_, least_common = count.most_common()
    score = most_common[1] - least_common[1]

    return most_common, least_common, score
