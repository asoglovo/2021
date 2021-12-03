import fileinput
import re

forward_re = re.compile(r'^forward (\d+)$')
down_re = re.compile(r'^down (\d+)$')
up_re = re.compile(r'^up (\d+)$')

if __name__ == '__main__':
    x, y, aim = 0, 0, 0

    for line in fileinput.input():
        if (match := forward_re.match(line)):
            dx = int(match.group(1))
            x += dx
            y += aim * dx
        elif (match := down_re.match(line)):
            dy = int(match.group(1))
            aim += dy
        elif (match := up_re.match(line)):
            dy = int(match.group(1))
            aim -= dy

    print(f'Final position: ({x}, {y})')
    print(f'{x} * {y} = {x * y}')
