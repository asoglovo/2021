import fileinput
import re


forward_re = re.compile(r'^forward (\d+)$')
down_re = re.compile(r'^down (\d+)$')
up_re = re.compile(r'^up (\d+)$')

if __name__ == '__main__':
    x, y = 0, 0

    for line in fileinput.input():
        if forward_re.match(line):
            dx = int(forward_re.match(line).group(1))
            x += dx
        elif down_re.match(line):
            dy = int(down_re.match(line).group(1))
            y += dy
        elif up_re.match(line):
            dy = int(up_re.match(line).group(1))
            y -= dy

    print(f'Final position: ({x}, {y})')
    print(f'{x} * {y} = {x * y}')
