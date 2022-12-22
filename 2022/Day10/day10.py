def get_input():
    from os import path

    input = []

    with open(path.join(path.dirname(__file__), "input.txt"), "r") as f:
        for line in f:
            line = line.strip().split()
            try:
                line[1] = int(line[1])
                input.append(["noop"])
            except:
                pass
            input.append(line)
    return input


def check_count(x, i, total):
    checks = [20, 60, 100, 140, 180, 220]
    print(f"{i}:  x = {x}")
    if i in checks:
        print(f"{i}: {x * i}")
        total += x * i
        print(f"total: {total}")
    return total


def part1(input):
    x = 1
    i = 1
    total = 0

    for line in input:
        print(line)
        if line[0] == "noop":
            i += 1
            total = check_count(x, i, total)
        else:
            i += 1
            x += line[1]
            total = check_count(x, i, total)
    check_count(x, i, total)

    print("Part 1:  ")


def part2(input):
    import numpy as np

    grid = np.full((6, 40), ".")
    cycle = 1
    x = 1

    for line in input:
        if cycle == 195:
            print()
        pixel = (cycle % 40) - 1
        display_line = cycle // 40
        if pixel == -1:
            display_line -= 1
            pixel = 39

        if abs(x - pixel) <= 1:
            grid[display_line][pixel] = "#"

        if line[0] == "noop":
            cycle += 1
        else:
            cycle += 1
            x += line[1]

    print(grid)


input = get_input()
part1(input)
part2(input)
