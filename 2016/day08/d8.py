import numpy as np


def get_input():
    from os import path

    input = []

    with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
        for line in f:
            line = line.strip().split()
            if line[0] == "rotate":
                line[2] = int(line[2][2:])
                line[4] = int(line[4])
            input.append(line)
    return input


def rect(dimensions, screen):
    dimensions = dimensions.split('x')
    for i in range(0, int(dimensions[1])):
        screen[i][0:int(dimensions[0])] = 1
    return screen


def rot_row(row, times, screen):
    screen[row] = np.roll(screen[row], times)
    return screen


def rot_col(col, times, screen):
    screen[:, col] = np.roll(screen[:, col], times)
    return screen


def part1(input):
    screen = np.zeros((6, 50), np.int8)
    for line in input:
        if line[0] == "rect":
            screen = rect(line[1], screen)
        elif line[1] == "column":
            screen = rot_col(line[2], line[4], screen)
        else:
            screen = rot_row(line[2], line[4], screen)
    print("Part 1: {}".format(str(np.sum(screen))))
    print(screen)


def part2(input):
    pass


input = get_input()
part1(input)
part2(input)
