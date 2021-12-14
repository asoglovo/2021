from typing import Counter

from polymer import polymerize, read_input

steps = 10

if __name__ == '__main__':
    polymer, rules = read_input()

    for steps in range(steps):
        polymer = polymerize(polymer, rules)

    count = Counter(polymer)
    most_common, *_, least_common = count.most_common()

    print(
        f'{most_common} - {least_common} = {most_common[1] - least_common[1]}'
    )
