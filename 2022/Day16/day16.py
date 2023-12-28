def get_input():
    from os import path

    input = []

    with open(path.join(path.dirname(__file__), "input.txt"), "r") as f:
        for line in f:
            input.append(line.strip())
    return input


def part1(input):
    print("Part 1:  ")


def part2(input):
    print("Part 2:  ")


input = get_input()
part1(input)
part2(input)
