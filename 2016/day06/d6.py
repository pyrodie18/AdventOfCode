def get_input():
    from os import path

    input = []

    with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
        for line in f:
            # line = line.strip()
            input.append(line.strip())
    return input


def part1(input):
    from collections import Counter
    from itertools import chain
    total = 0
    my_list = list(zip(*input))
    answer1 = ""
    answer2 = ""
    for col in my_list:
        col_counter = Counter(col)
        answer1 += col_counter.most_common(1)[0][0]
        answer2 += col_counter.most_common()[-1][0]

    print("Part 1: {}".format(answer1))
    print("Part 2: {}".format(answer2))


input = get_input()
part1(input)
