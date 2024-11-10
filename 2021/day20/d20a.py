import os
padding_depth = 100
grid_size = 100

grid = []
padding = ['0'] * padding_depth

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), "r") as f:
    input = f.readlines()

def reformat_line(line) -> str:
    line = line.strip()
    line = line.replace('.', '0')
    line = line.replace('#', '1')
    tmp = []
    tmp[:0] = line
    return tmp

def get_padding() -> list:
    padding = []
    for i in range(padding_depth):
        line = ['0'] * (grid_size + (padding_depth * 2))
        padding.append(line)
    return padding


algoritm = reformat_line(input[0])

grid += get_padding()
for line in input[2:]:
    line = reformat_line(line)
    line = padding.copy() + line + padding.copy()
    grid.append(line)
grid += get_padding()

for a in range(50):
    new_grid = []
    for b in range((grid_size + (padding_depth * 2))):
        row = ['0'] * (grid_size + (padding_depth * 2))
        new_grid.append(row)
    for i in range(1 + a, len(grid) - (1 + a)):
        for j in range(1 + a, len(grid[i]) - (1 + a)):
            input = []
            input += grid[i - 1][j - 1: j + 2]
            input += grid[i][j - 1: j + 2]
            input += grid[i + 1][j - 1: j + 2]
            input = ''.join(input)
            input = int(input, 2)
            new_grid[i][j] = algoritm[input]

    grid = new_grid.copy()

total = 0
for line in grid:
    total += line.count('1')

print(total)
