import fileinput
from collections import Counter
from typing import Dict, Tuple

InsertionRules = Dict[str, str]


def read_input() -> Tuple[str, InsertionRules]:
    template, _, *rules = fileinput.input()
    rules = dict([rule.strip().split(' -> ') for rule in rules])

    return template.strip(), rules


def polymerize(polymer: str, rules: InsertionRules) -> str:
    polymer_letters = []

    for i in range(1, len(polymer)):
        polymer_letters.append(polymer[i - 1])

        pattern = polymer[i - 1:i + 1]
        polymer_letters.append(rules[pattern])

    polymer_letters.append(polymer[-1])

    return ''.join(polymer_letters)


def polymer_score(polymer: str):
    count = Counter(polymer)
    most_common, *_, least_common = count.most_common()
    score = most_common[1] - least_common[1]

    return most_common, least_common, score
