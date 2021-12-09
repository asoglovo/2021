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

    print(f'there are {len(lows)} low points')
    for low in lows:
        print(low)
        assert all([low['height'] < side for side in low['sides']])

    total_risk = sum(
        [low['risk'] for low in lows]
    )

    print(f'Total risk: {total_risk}')
