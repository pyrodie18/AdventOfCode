import os

grid = []

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), "r") as f:
    for line in f:
        line = line.strip()
        tmp = []
        for i in line:
            tmp.append(int(i))
        grid.append(tmp)

flash_count = 0

for a in range(100):
    # Increase all by one
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j] += 1

    # Loop thorugh and flash as required
    dirty = True
    while dirty:
        dirty = False
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] >= 10:
                    for i1 in range(i-1, i+2):
                        for j1 in range(j-1, j+2):
                            try:
                                assert i1 >= 0
                                assert j1 >= 0
                                if grid[i1][j1] > 0:
                                    grid[i1][j1] += 1
                                    dirty = True
                            except:
                                continue
                    grid[i][j] = 0
                    flash_count += 1

    

print(flash_count)