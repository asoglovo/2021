import fileinput

from display import identify_output_number


def parse_line(line):
    patterns, output = line.strip().split(' | ')
    patterns, output = patterns.split(), output.split()

    return patterns, output


if __name__ == '__main__':
    numbers_sum = 0

    for line in fileinput.input():
        patterns, output = parse_line(line)
        numbers_sum += identify_output_number(patterns, output)

    print(f'All numbers sum: {numbers_sum}')
