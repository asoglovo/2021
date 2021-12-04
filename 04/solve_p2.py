import fileinput
from board import (compute_board_score, draw_num_in_board, is_winning_board,
                   read_boards)

board_size = 5


def read_bingo_from_input():
    drawn_nums, *board_def_lines = fileinput.input()
    drawn_nums = [int(n) for n in drawn_nums.split(',')]
    boards = read_boards(board_def_lines, board_size)

    return drawn_nums, boards


if __name__ == '__main__':
    drawn_nums, boards = read_bingo_from_input()
    winner_boards = []

    for n in drawn_nums:
        unwon_boards = [
            board for board in boards
            if board not in winner_boards
        ]

        for board in unwon_boards:
            draw_num_in_board(board, n)
            if is_winning_board(board):
                winner_boards.append(board)

        if len(winner_boards) == len(boards):
            break

    last_winner = winner_boards[-1]
    last_winner_score = compute_board_score(last_winner)
    print(f'Winning score: {last_winner_score}')
