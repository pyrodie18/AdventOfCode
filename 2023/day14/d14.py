import numpy as np


def get_data():
    from os import path

    data = []

    with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
        for line in f:
            line = line.strip()
            line = [i for i in line]
            data.append(line)

    return data


def transpose_cols(grid):

    new_grid = np.array(grid).T
    new_grid = new_grid.tolist()
    return new_grid


def shift_stones(grid):
    col_length = len(grid[0])
    new_grid = []
    for col in grid:
        new_col = ["" for i in range(col_length)]
        current_pos = 0
        for i, item in enumerate(col):
            if item == "#":
                current_pos = i
                new_col[current_pos] = "#"
                current_pos += 1
            elif item not in ["#", ".", ""]:
                new_col[current_pos] = item
                current_pos += 1
        new_grid.append(new_col)
    return new_grid


def calculate_load(grid):
    col_length = len(grid[0])
    load = 0
    for col in grid:
        for i, item in enumerate(col):
            if item == "O":
                load += (col_length - i)
    return load


def part1(data):
    grid = transpose_cols(data)
    grid = shift_stones(grid)
    load = calculate_load(grid)

    print('Part 1:  {}'.format(str(load)))


def part2(data):
    grid = data
    for q in range(1000000000):
        # Shift Front
        grid = transpose_cols(grid)
        grid = shift_stones(grid)
        grid = transpose_cols(grid)

        # Shift Left
        grid = shift_stones(grid)

        # Shift Down
        grid = np.array(grid)
        grid = np.flipud(grid)
        grid = grid.tolist()
        grid = transpose_cols(grid)
        grid = shift_stones(grid)
        grid = transpose_cols(grid)
        grid = np.array(grid)
        grid = np.flipud(grid)
        grid = grid.tolist()

        # Shift Right
        grid = np.array(grid)
        grid = np.fliplr(grid)
        grid = grid.tolist()
        grid = shift_stones(grid)
        grid = np.array(grid)
        grid = np.fliplr(grid)
        grid = grid.tolist()

    load = calculate_load(grid)
    print('Part 2:  {}'.format(str(load)))


data = get_data()
# part1(data)
part2(data)
