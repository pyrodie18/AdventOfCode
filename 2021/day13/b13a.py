import os

coordinates = []
folds = []

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), "r") as f:
    for line in f:
        line = line.strip()
        # Find the fold instructions
        if 'fold' in line:
            line = line.split(' ')
            line = line[2].split('=')
            line[1] = int(line[1])
            folds.append(line)
        else:
            line = line.split(',')
            if len(line) == 1:
                continue
            else:
                coordinates.append((int(line[0]), int(line[1])))

def fold_y(instruction, grid) -> list:
    x_length = len(grid[0])
    y_length = len(grid)

    for y in range(instruction + 1, y_length):
        new_y = instruction - abs(y - instruction)
        for x in range(x_length):
            grid[new_y][x] = max(grid[y][x], grid[new_y][x])
    del(grid[instruction:])
    return grid

def fold_x(instruction, grid) -> list:
    x_length = len(grid[0])
    y_length = len(grid)

    for y in range(y_length):
        for x in range(instruction + 1, x_length):
            new_x = instruction - abs(x - instruction)
            grid[y][new_x] = max(grid[y][new_x], grid[y][x])
        del(grid[y][instruction:])
    return grid

# Figure out grid size
max_x = 0
max_y = 0
for i in coordinates:
    max_x =  max(max_x, i[0])
    max_y = max(max_y, i[1])

grid = []
for y in range(max_y + 1):
    tmp = [0] * (max_x + 1) 
    grid.append(tmp)

for line in coordinates:
    x, y = line[0], line[1]
    grid[y][x] = 1

# fold = folds[0]
for fold in folds:
    if fold[0] == 'y':
        grid = fold_y(fold[1], grid)
    else:
        grid = fold_x(fold[1], grid)

total = 0
for y in grid:
    total += sum(y)
print(total)

for line in grid:
    print(line)