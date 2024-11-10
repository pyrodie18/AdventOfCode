def get_input():
    from os import path

    input = []

    with open(path.join(path.dirname(__file__), "input.txt"), "r") as f:
        for line in f:
            input.append([int(i) for i in line.strip().split(",")])
    return input


def find_range(i, max_value):
    low = i - 1 if i - 1 >= 0 else 0
    high = i + 2 if i + 2 <= max_value - 1 else max_value - 1
    return [low, high]


def create_grid(input):
    import numpy as np

    max_value = np.max(input) + 2
    grid = np.zeros((max_value, max_value, max_value), dtype=np.int8)

    for line in input:
        grid[line[2], line[1], line[0]] = 1
    return grid


def part1(input, grid):
    surface_area = 0
    # Cycle through and see how many sides are exposed
    for line in input:
        c = line[0]
        r = line[1]
        d = line[2]
        d_range = find_range(d, max_value)
        r_range = find_range(r, max_value)
        c_range = find_range(c, max_value)
        # check across
        adjacent = sum(grid[d, r, c_range[0] : c_range[1]]) - 1
        # check virtical
        adjacent += sum(grid[d, r_range[0] : r_range[1], c]) - 1
        # check forward/back
        adjacent += sum(grid[d_range[0] : d_range[1], r, c]) - 1
        surface_area += 6 - adjacent
    print("Part 1:  " + str(surface_area))

    return surface_area


def part2(input, grid, surface_area):
    print("Part 2:  ")


input = get_input()
grid = create_grid(input)
surface_area = part1(input, grid)
part2(input, grid, surface_area)
