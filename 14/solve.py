from polymer import polymer_score, polymerize, read_input

steps = 10

if __name__ == '__main__':
    polymer, rules = read_input()

    for steps in range(steps):
        polymer = polymerize(polymer, rules)

    most_common, least_common, score = polymer_score(polymer)

    print(
        f'{most_common} - {least_common} = {score}'
    )
