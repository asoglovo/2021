import fileinput


def find_rating(report_nums, bit_criteria_fn, bit_pos=0) -> int:
    zeroes = [num_list for num_list in report_nums if num_list[bit_pos] == 0]
    ones = [num_list for num_list in report_nums if num_list[bit_pos] == 1]
    candidates = bit_criteria_fn(zeroes, ones)

    return bin_string_to_int(candidates[0]) if len(candidates) == 1 \
        else find_rating(candidates, bit_criteria_fn, bit_pos + 1)


def bin_string_to_int(bin_string):
    return int(''.join(str(x) for x in bin_string), 2)


if __name__ == '__main__':
    report_nums = [
        [int(c) for c in line.strip()] for line in fileinput.input()
    ]

    o2_rating = find_rating(
        report_nums,
        lambda zeroes, ones: zeroes if len(zeroes) > len(ones) else ones
    )
    co2_rating = find_rating(
        report_nums,
        lambda zeroes, ones: zeroes if len(zeroes) <= len(ones) else ones
    )

    print(f'O2 rating: {o2_rating}, CO2 rating: {co2_rating}')
    print(f'Life supporting rating: {o2_rating * co2_rating}')
