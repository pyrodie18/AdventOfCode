import numpy as np


def get_input():
    from os import path

    with open(path.join(path.dirname(__file__), "input.txt"), "r") as f:
        input = np.genfromtxt(f, delimiter=1, dtype=int)
    return input


def part1(input):
    count = 0
    array_shape = input.shape
    for r in range(1, array_shape[0] - 1):
        row = input[r, :]
        for c in range(1, array_shape[1] - 1):
            current_value = input[r][c]
            col = input[:, c]
            if (max(row[:c]) < current_value) or (max(row[c + 1 :]) < current_value):
                count += 1
            elif (max(col[:r]) < current_value) or (max(col[r + 1 :]) < current_value):
                count += 1

    count += array_shape[0] * 2
    count += (array_shape[1] - 2) * 2
    print("Part 1:  " + str(count))


def part2(input):
    max_score = 0
    array_shape = input.shape
    for r in range(array_shape[0]):
        row = input[r, :]
        for c in range(array_shape[1]):
            current_value = input[r][c]
            col = input[:, c]
            left = right = up = down = 0
            for i in range(c - 1, -1, -1):
                if row[i] >= current_value:
                    left += 1
                    break
                else:
                    left += 1
            for i in range(c + 1, len(row)):
                if row[i] >= current_value:
                    right += 1
                    break
                else:
                    right += 1
            for i in range(r - 1, -1, -1):
                if col[i] >= current_value:
                    up += 1
                    break
                else:
                    up += 1
            for i in range(r + 1, len(col)):
                if col[i] >= current_value:
                    down += 1
                    break
                else:
                    down += 1
            scenic_score = left * right * up * down
            if scenic_score > max_score:
                max_score = scenic_score

    print("Part 2:  " + str(max_score))


input = get_input()
part1(input)
part2(input)
