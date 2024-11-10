import os

grid = []
low_points = []
basins = []
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
                    low_points.append((r,c))
                    count += 1
            elif r == 0:
                if sample[1] < grid[r + 1][c]:
                    risk_total += (sample[1] + 1)
                    low_points.append((r,c))
                    count += 1
            else:
                if grid[r - 1][c] > sample[1]:
                    risk_total += (sample[1] + 1)
                    low_points.append((r,c))
                    count += 1
print(risk_total)


def calc_basin(low, done=[]):
    if low in done:
        return 0

    done.append(low)
    r = low[0]
    c = low[1]
    ret_val = 1

    try:
        assert (r - 1) >= 0
        assert (grid[r-1][c]) != 9
        ret_val += calc_basin((r - 1,c))
    except:
        pass

    try:
        assert (r + 1) <= len(grid)
        assert (grid[r+1][c]) != 9
        ret_val += calc_basin((r + 1,c))
    except:
        pass

    try:
        assert (c - 1) >= 0
        assert grid[r][c-1] != 9
        ret_val += calc_basin((r, c-1))
    except:
        pass

    try:
        assert (c + 1) <= len(grid[r])
        assert grid[r][c+1] != 9
        ret_val += calc_basin((r, c+1))
    except:
        pass

    return ret_val

for point in low_points:
    basins.append(calc_basin(point))

basins.sort(reverse=True)
print(basins)
print(basins[0] * basins[1] * basins[2])
