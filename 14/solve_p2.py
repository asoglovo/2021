from polymer import polymer_score, polymerize, read_input, size_after_steps
from collections import Counter

steps = 30

if __name__ == '__main__':
    polymer, rules = read_input()
    final_size = size_after_steps(len(polymer), steps)
    polymer = polymerize(polymer, rules, steps)

    # most_common, least_common, score = polymer_score(polymer)

    # print(
    #     f'{most_common} - {least_common} = {score}'
    # )
    print(f'Predicted final size: {final_size}')
