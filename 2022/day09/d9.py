import numpy as np


def get_input():
    from os import path

    input = []

    with open(path.join(path.dirname(__file__), "input.txt"), "r") as f:
        for line in f:
            input.append(line.strip().split())
    return input


def parse_move(line, t, h):
    moves = []
    for i in range(int(line[1])):
        if line[0] == "U" or line[0] == "D":
            hor_diff = 0
            if line[0] == "U":
                h[0] -= 1
                # Did we move more than one space away on the vertical?
                if (t[0] - h[0]) > 1:
                    hor_diff = h[1] - t[1]
                    t[0] -= 1
            else:
                h[0] += 1
                if (h[0] - t[0]) > 1:
                    hor_diff = h[1] - t[1]
                    t[0] += 1
            t[1] += hor_diff
        else:
            ver_diff = 0
            if line[0] == "L":
                h[1] -= 1
                if (t[1] - h[1]) > 1:
                    ver_diff = h[0] - t[0]
                    t[1] -= 1
            else:
                h[1] += 1
                if (h[1] - t[1]) > 1:
                    ver_diff = h[0] - t[0]
                    t[1] += 1
            t[0] += ver_diff
        moves.append([t[0], t[1]])

    return t, h, moves


def part1(input, board):
    t = [500, 500]
    h = [500, 500]

    for line in input:
        t, h, moves = parse_move(line, t, h)
        for move in moves:
            board[move[0]][move[1]] = 1

    print("Part 1:  " + str(board.sum()))


def part2(input):
    print("Part 2:  ")


board = np.zeros((1000, 1000), dtype=int)

input = get_input()
part1(input, board)
part2(input)
