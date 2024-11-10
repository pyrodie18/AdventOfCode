def get_input():
    from os import path

    input = []

    with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
        for line in f:
            input.append([int(value) for value in line.split()])
    return input


def is_triangle(sides):
    a, b, c = sorted(sides)
    return a + b > c


def part1(input):
    total = 0
    for line in input:
        if is_triangle(line):
            total += 1

    print("Part 1: {}".format(str(total)))


def part2(input):
    from itertools import chain
    total = 0
    vertical = list(chain.from_iterable(zip(*input)))
    for i in range(0, len(vertical) - 2, 3):
        if is_triangle(vertical[i:i+3]):
            total += 1
    print("Part 2: {}".format(str(total)))


input = get_input()
part1(input)
part2(input)
