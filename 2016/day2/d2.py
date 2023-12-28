from enum import Enum
DIGIT = [
    [7, 8, 9],
    [4, 5, 6],
    [1, 2, 3]
]

BIG_DIGIT = [
    ["0", "0", "D", "0", "0"],
    ["0", "A", "B", "C", "0"],
    ["5", "6", "7", "8", "9"],
    ["0", "2", "3", "4", "0"],
    ["0", "0", "1", "0", "0"]
]


def get_input():
    from os import path

    input = []

    with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
        for line in f:
            line = line.strip()
            input.append(line)
    return input


def check_move(x, y):
    return BIG_DIGIT[y][x] != "0"


def get_new_position(x, y, move, expanded=False):
    if expanded:
        max = 3
    else:
        max = 1
    if move == "L" or move == "R":
        if move == "L" and x >= 1:
            if expanded:
                if check_move(x - 1, y):
                    x -= 1
            else:
                x -= 1
        elif move == "R" and x <= max:
            if expanded:
                if check_move(x + 1, y):
                    x += 1
            else:
                x += 1
    else:
        if move == "D" and y >= 1:
            if expanded:
                if check_move(x, y - 1):
                    y -= 1
            else:
                y -= 1
        elif move == "U" and y <= max:
            if expanded:
                if check_move(x, y + 1):
                    y += 1
            else:
                y += 1
    return x, y


def part1(input):
    code = []
    x = 1
    y = 1
    for line in input:
        for step in line:
            x, y = get_new_position(x, y, step)
        code.append(str(DIGIT[y][x]))
    print("Part 1:")
    print("".join(code))


def part2(input):
    code = []
    x = 0
    y = 2
    for line in input:
        for step in line:
            x, y = get_new_position(x, y, step, True)
        code.append(str(BIG_DIGIT[y][x]))
    print("Part 2:")
    print("".join(code))


input = get_input()
part1(input)
part2(input)
