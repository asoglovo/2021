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

    for n in drawn_nums:
        winner_board, winner_score = None, 0

        for board in boards:
            draw_num_in_board(board, n)

            if is_winning_board(board):
                score = compute_board_score(board)
                if score > winner_score:
                    winner_board = board
                    winner_score = score

        if winner_board:
            print(f'Winning score: {winner_score}')
            break
