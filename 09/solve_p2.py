import fileinput

from heightmap import find_basin_size, find_low_points


def read_heightmap():
    return [
        list(map(int, list(line.strip())))
        for line in fileinput.input()
    ]


if __name__ == '__main__':
    heighmap = read_heightmap()
    lows = find_low_points(heighmap)
    basin_sizes = [
        find_basin_size(heighmap, low) for low in lows
    ]
    basin_sizes.sort(reverse=True)
    a, b, c, *rest = basin_sizes

    print(f'Basins {a} * {b} * {c} = {a * b * c}')
