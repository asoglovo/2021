from origami import fold_along, print_dots, read_input

if __name__ == '__main__':
    dots, instructions = read_input()

    for instruction in instructions:
        dots = fold_along(dots, instruction)

    print_dots(dots, 50, 7)
