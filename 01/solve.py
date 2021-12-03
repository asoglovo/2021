import fileinput


if __name__ == '__main__':
    depth_increases, depth_decreases = 0, 0
    prev_depth = None

    for line in fileinput.input():
        depth = int(line)

        if prev_depth is None:
            prev_depth = depth
            continue

        if depth > prev_depth:
            depth_increases += 1
        else:
            depth_decreases += 1

        prev_depth = depth

    print(f'Depth increases: {depth_increases}')
    print(f'Depth decreases: {depth_decreases}')
