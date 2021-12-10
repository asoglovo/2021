import fileinput

from syntax import compute_line_syntax_error_score

if __name__ == '__main__':
    total_score = 0

    for line in fileinput.input():
        score = compute_line_syntax_error_score(line.strip())
        total_score += score

    print(f'Total syntax error score: {total_score}')
