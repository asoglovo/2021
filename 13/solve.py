from origami import fold_along, read_input


if __name__ == '__main__':
    dots, instructions = read_input()
    first_fold = instructions[0]

    dots = fold_along(dots, first_fold)

    print(f'After the first fold, there are {len(dots)} dots.')
