import fileinput
from collections import deque


if __name__ == '__main__':
    depth_increases = 0
    last_depth_triad_sum = None

    first_depth, second_depth, *depths = fileinput.input()
    depths_queue = deque([int(first_depth), int(second_depth)], maxlen=2)

    for line in depths:
        depth = int(line)

        depth_triad_sum = sum(list(depths_queue)) + depth
        depths_queue.append(depth)

        if last_depth_triad_sum and depth_triad_sum > last_depth_triad_sum:
            depth_increases += 1

        last_depth_triad_sum = depth_triad_sum

    print(f'Depth increases: {depth_increases}')
