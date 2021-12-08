import fileinput

zero = 'abcefg'
one = 'cf'
two = 'acdeg'
three = 'acdfg'
four = 'bcdf'
five = 'abdfg'
six = 'abdefg'
seven = 'acf'
eight = 'abcdefg'
nine = 'abcdfg'


def parse_line(line):
    patterns, output = line.strip().split(' | ')
    patterns, output = patterns.split(), output.split()

    return patterns, output


def is_known_digit(digit: str) -> bool:
    digit_len = len(digit)

    if digit_len == len(one):
        return True
    elif digit_len == len(four):
        return True
    elif digit_len == len(seven):
        return True
    elif digit_len == len(eight):
        return True
    else:
        return False


if __name__ == '__main__':
    count = 0

    for line in fileinput.input():
        patterns, output = parse_line(line)
        count += sum(is_known_digit(digit) for digit in output)

    print(f'Found {count} patterns')
