from origami import fold_along, print_dots, read_input

width = 39
height = 6


if __name__ == '__main__':
    dots, instructions = read_input()

    for instruction in instructions:
        dots = fold_along(dots, instruction)

    print_dots(dots, width, height)
