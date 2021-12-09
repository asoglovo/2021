import fileinput

from heightmap import find_low_points


def read_heightmap():
    return [
        list(map(int, list(line.strip())))
        for line in fileinput.input()
    ]


if __name__ == '__main__':
    heighmap = read_heightmap()
    lows = find_low_points(heighmap)
    total_risk = sum(
        [low['risk'] for low in lows]
    )

    print(f'Total risk: {total_risk}')
