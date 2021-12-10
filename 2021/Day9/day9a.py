import os

grid = []
with open(os.path.join(os.path.dirname(__file__), 'input.txt'), "r") as f:
    for line in f:
        line = line.strip()
        line = list(line)
        int_line = []
        for i in line:
            int_line.append(int(i))
        grid.append(int_line)

height = len(grid)
width = len(grid[0])
risk_total = 0
count = 0
for r in range(height):
    for c in range(width):
        if (c >= 1) and (c < (width - 1)):
            sample = grid[r][c -1: c + 2]
        elif c == 0:
            sample = [1000]
            sample += grid[r][c: c + 2]
        else:
            sample = grid[r][c - 1 :]
            sample += [1000]

        if sample[0] > sample[1] < sample[2]:
            if (r >= 1) and (r < (height - 1)):
                if grid[r - 1][c] > sample[1] < grid[r + 1][c]:
                    risk_total += (sample[1] + 1)
                    count += 1
            elif r == 0:
                if sample[1] < grid[r + 1][c]:
                    risk_total += (sample[1] + 1)
                    count += 1
            else:
                if grid[r - 1][c] > sample[1]:
                    risk_total += (sample[1] + 1)
                    count += 1
print(risk_total)
print(count)