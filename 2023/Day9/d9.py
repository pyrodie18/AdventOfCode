import numpy as np


def get_input():
    from os import path

    input = []

    with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
        for line in f:
            line = np.array(line.strip().split())
            line = line.astype(np.int64)
            input.append(line)
    return input


def predict(values):
    differences = np.diff(values)
    if len(np.unique(differences)) == 1:
        return np.append(values, (values[-1] + differences[-1]))
    else:
        return np.append(values, (values[-1] + predict(differences)[-1]))


def extrapolate(values):
    differences = np.diff(values)
    if len(np.unique(differences)) == 1:
        return np.append((values[0] - differences[0]), values)
    else:
        return np.append((values[0] - extrapolate(differences)[0]), values)


def part1(input):
    total = 0
    for line in input:
        total += predict(line)[-1]
    print('Part 1:  {}'.format(str(total)))


def part2(input):
    total = 0
    for line in input:
        total += extrapolate(line)[0]
    print('Part 2  {}'.format(str(total)))


input = get_input()
part1(input)
part2(input)
