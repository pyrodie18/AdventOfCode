import os


def prepare():
    with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as f:
        for line in f:
            tmp = line.strip()
        input = list(tmp)
    return input


def solve(input):
    for i in range(len(input) - 4):
        check1 = set(input[i : i + 4])
        check2 = set(input[i : i + 14])
        if len(check1) == 4:
            check1 = i + 4
        if len(check2) == 14:
            check2 = i + 14
            return check1, check2


input = prepare()
part1, part2 = solve(input)
print("Part 1:  " + str(part1))
print("Part 2:  " + str(part2))
