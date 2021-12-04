import re
from typing import List


def read_boards(board_def_lines: List[str], board_size):
    """
    Reads a list of board definition lines and parses each group of lines as a board.

    Boards are separated by a blank line, thus a board is parsed from as many lines
    as the board size plus one.
    """
    board_lines_count = board_size + 1
    boards = []
    boards_count = len(board_def_lines) // board_lines_count

    for i in range(boards_count):
        # start index skips the first line with the '\n' character
        start = i * board_lines_count + 1
        end = (i + 1) * board_lines_count
        boards.append(
            __parse_board(board_def_lines[start:end], board_size)
        )

    return boards


def __parse_board(lines: List[str], board_size):
    nums_str = re.split(r'\s+', ' '.join([line.strip() for line in lines]))
    nums_row = [int(n) for n in nums_str]
    nums = [{'num': n, 'drawn': False} for n in nums_row]

    return {
        'size': board_size,
        'last_num': None,
        'nums_set': set(nums_row),
        'nums': nums
    }


def draw_num_in_board(board, number):
    if number in board['nums_set']:
        board['last_num'] = number

        for n in board['nums']:
            if n['num'] == number:
                n['drawn'] = True


def is_winning_board(board):
    """
    A board is winning if an entire row or an entire column has been drawn.
    """
    size = board['size']

    for i in range(size):
        row = get_board_row(board, i)
        if all([n['drawn'] for n in row]):
            return True

        col = get_board_col(board, i)
        if all([n['drawn'] for n in col]):
            return True

    return False


def get_board_row(board, row_idx):
    nums = board['nums']
    size = board['size']

    return nums[row_idx*size:row_idx*size+size]


def get_board_col(board, col_idx):
    nums = board['nums']
    size = board['size']

    return [nums[i] for i in range(col_idx, size**2, size)]


def compute_board_score(board):
    """
    The score of a winning board is sum the of all undrawn numbers on that board
    multiplied by the last called number; the number which made the board win.
    """
    nums = board['nums']
    last_num = board['last_num']

    return last_num * sum(
        [n['num'] for n in nums if not n['drawn']]
    )
