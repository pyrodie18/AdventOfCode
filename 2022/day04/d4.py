import os
import cProfile

profiler = cProfile.Profile()
profiler.enable()


def prepare():
    input = []
    with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as f:
        for line in f:
            tmp = line.strip().split(",")
            for i in range(2):
                tmp[i] = tmp[i].split(("-"))
                for j in range(2):
                    tmp[i][j] = int(tmp[i][j])
            input.append(tmp)
    return input


def part1(input):
    total = 0
    for team in input:
        if team[0][0] >= team[1][0] and team[0][1] <= team[1][1]:
            total += 1
        elif team[1][0] >= team[0][0] and team[1][1] <= team[0][1]:
            total += 1
    return total


def part2(input):
    total = 0
    for team in input:
        if team[0][0] >= team[1][0] and team[0][0] <= team[1][1]:
            total += 1
        elif team[0][1] >= team[1][0] and team[0][1] <= team[1][1]:
            total += 1
        elif team[1][0] >= team[0][0] and team[1][0] <= team[0][1]:
            total += 1
        elif team[1][1] >= team[0][0] and team[1][1] <= team[0][1]:
            total += 1
    return total


input = prepare()
print(part1(input))
print(part2(input))

profiler.disable()
profiler.print_stats()
