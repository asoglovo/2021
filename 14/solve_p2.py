from polymer import polymer_score, polymerize_steps, read_input

steps = 12

if __name__ == '__main__':
    polymer, rules = read_input()
    polymer = polymerize_steps(polymer, rules, steps)

    most_common, least_common, score = polymer_score(polymer)

    print(
        f'{most_common} - {least_common} = {score}'
    )
