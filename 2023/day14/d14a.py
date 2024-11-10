import numpy as np


def get_data():
    from os import path

    data = []

    with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
        for line in f:
            line = line.strip()
            line = [i for i in line]
            data.append(line)

    return np.array(data)


def transpose_cols(grid):

    new_grid = np.array(grid).T
    # new_grid = new_grid.tolist()
    return new_grid


def shift_stones(grid):
    # col_length = len(grid[0])
    # num_of_cols = len(grid)
    # new_grid = []
    for col in grid:
        # new_col = ["" for i in range(col_length)]
        current_pos = 0
        for i, item in enumerate(col):
            if item == "#":
                current_pos = i + 1
                # new_col[current_pos] = "#"
                # current_pos += 1
            elif item == "O":
                if current_pos != i:
                    col[i] = ""
                    col[current_pos] = "O"
                # new_col[current_pos] = item
                current_pos += 1
        # new_grid.append(new_col)


def calculate_load(grid):
    col_length = len(grid[0])
    load = 0
    for col in grid:
        for i, item in enumerate(col):
            if item == "O":
                load += (col_length - i)
    return load


def part1(data):
    n_grid = data.T
    shift_stones(n_grid)
    load = calculate_load(n_grid)

    print('Part 1:  {}'.format(str(load)))


def part2(data):
    iternations = 1000000000
    seen = []
    grid = data
    n_grid = grid.T
    w_grid = grid
    s_grid = np.flipud(grid).T
    e_grid = np.fliplr(grid)

    for i in range(iternations):
        # print("grid")
        # print(grid)
        shift_stones(n_grid)
        # print("north")
        # print(grid)
        shift_stones(w_grid)
        # print("west")
        # print(grid)
        shift_stones(s_grid)
        # print("south")
        # print(grid)
        shift_stones(e_grid)
        # print("east")
        # print(grid)

        list_grid = grid.tolist()
        print("{}:  {}".format(str(i), str(calculate_load(n_grid))))
        # print(grid)
        if list_grid in seen:
            first_seen = seen.index(list_grid)
            loop_size = i - first_seen
            target = ((iternations - first_seen) % loop_size) + first_seen - 1
            print("Found!  {}".format(str(i)))
            print("Twin: {}".format(str(seen.index(list_grid))))
            # remainder = (1000000000 % i)
            break
        else:
            seen.append(list_grid)
    final_grid = seen[target]
    final_grid = np.array(final_grid).T
    load = calculate_load(final_grid)

    # print("grid")
    # print(grid)

    # for q in range(1000000000):
    #     # Shift Front
    #     grid = transpose_cols(grid)
    #     grid = shift_stones(grid)
    #     grid = transpose_cols(grid)

    #     # Shift Left
    #     grid = shift_stones(grid)

    #     # Shift Down
    #     grid = np.array(grid)
    #     grid = np.flipud(grid)
    #     grid = grid.tolist()
    #     grid = transpose_cols(grid)
    #     grid = shift_stones(grid)
    #     grid = transpose_cols(grid)
    #     grid = np.array(grid)
    #     grid = np.flipud(grid)
    #     grid = grid.tolist()

    #     # Shift Right
    #     grid = np.array(grid)
    #     grid = np.fliplr(grid)
    #     grid = grid.tolist()
    #     grid = shift_stones(grid)
    #     grid = np.array(grid)
    #     grid = np.fliplr(grid)
    #     grid = grid.tolist()

    # load = calculate_load(grid)
    print('Part 2:  {}'.format(str(load)))


data = get_data()
# part1(data)
part2(data)
