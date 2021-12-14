import fileinput
from itertools import tee
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
