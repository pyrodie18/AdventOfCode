def get_data():
    from os import path

    data = []

    with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
        chunks = f.read().split("\n\n")
    for chunk in chunks:
        data.append(chunk.split("\n"))
    return data


def transpose_cols(grid):
    import numpy as np
    new_grid = []

    for line in grid:
        new_grid.append([i for i in line])
    new_grid = np.array(new_grid).T.tolist()
    for i, line in enumerate(new_grid):
        new_grid[i] = "".join(line)
    return new_grid


def check_rows(grid, top_row, new1=False, new2=False):
    i = 0
    checked = []
    while (top_row - i >= 0) and (top_row + i <= len(grid) - 2):
        if grid[top_row - i] != grid[top_row + i + 1]:
            return False
        checked.append(top_row - i)
        checked.append(top_row + i + 1)
        i += 1

    if new1 in checked and new2 in checked:
        return True
    else:
        return False


def find_fold(grid, new1=False, new2=False):
    for i in range(len(grid) - 1):
        if grid[i] == grid[i + 1]:
            if check_rows(grid, i, new1, new2):
                return i + 1
    return False


def is_similar(line1, line2):
    t = 0
    for i in range(len(line1)):
        t += (line1[i] == line2[i])
    return t == (len(line1) - 1)


def find_smudge(grid):
    from itertools import combinations
    from difflib import SequenceMatcher

    combos = combinations([c for c in range(len(grid))], 2)
    for combo in combos:
        if is_similar(grid[combo[0]], grid[combo[1]]):
            new_grid = [i for i in grid]
            new_grid[combo[0]] = new_grid[combo[1]]

            fold = find_fold(new_grid, combo[0], combo[1])
            if fold:
                return fold
    return False


def part1(data):
    total = 0
    for grid in data:
        row = find_fold(grid)
        if row:
            total += (100 * row)
            continue
        else:
            transpose = transpose_cols(grid)
            col = find_fold(transpose)
            total += col

    pass
    print('Part 1:  {}'.format(str(total)))


def part2(data):
    total = 0
    i = 1
    for grid in data:
        row = find_smudge(grid)
        if row:
            total += (100 * row)
            print("{}:  {}".format(str(i), str(row * 100)))
        else:
            transpose = transpose_cols(grid)
            col = find_smudge(transpose)
            if col:
                total += col
                print("{}:  {}".format(str(i), str(col)))
            else:
                print(grid)
        i += 1

    print('Part 2:  {}'.format(str(total)))


data = get_data()
# part1(data)
# transpose_cols(data)
part2(data)
