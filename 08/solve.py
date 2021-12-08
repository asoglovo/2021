import fileinput

zero = set('abcefg')
one = set('cf')
two = set('acdeg')
three = set('acdfg')
four = set('bcdf')
five = set('abdfg')
six = set('abdefg')
seven = set('acf')
eight = set('abcdefg')
nine = set('abcdfg')


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
