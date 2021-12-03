import fileinput

zero = '0'
one = '1'

if __name__ == '__main__':
    first_line, *lines = fileinput.input()
    count_by_pos = [[1, 0] if c == zero else [0, 1]
                    for c in first_line.strip()]

    for line in lines:
        for i, bit in enumerate(line.strip()):
            if bit == zero:
                count_by_pos[i][0] += 1
            else:
                count_by_pos[i][1] += 1

    gamma_rate = ''.join([zero if c[0] > c[1] else one for c in count_by_pos])
    eps_rate = ''.join([zero if c[0] < c[1] else one for c in count_by_pos])
    consumption = int(gamma_rate, 2) * int(eps_rate, 2)

    print(f'Gamma: {int(gamma_rate, 2)}, Epsilon: {int(eps_rate, 2)}')
    print(f'Consumption (Gamma x Epsilon): {consumption}')
