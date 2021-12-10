import fileinput

from syntax import chars_to_coplete_chunk, compute_completion_score

if __name__ == '__main__':
    scores = []

    for line in fileinput.input():
        completion = chars_to_coplete_chunk(line.strip())
        score = compute_completion_score(completion)

        if score > 0:
            scores.append(score)

    # the winner is found by sorting all of the scores and then
    # taking the middle score.
    scores.sort()
    middle_score = scores[len(scores) // 2]
    print(f'Completion error score: {middle_score}')
