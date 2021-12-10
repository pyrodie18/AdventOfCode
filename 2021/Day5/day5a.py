import os
size = 1000
vents = []

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), "r") as f:
    for line in f:
        line = line.split()
        line[0] = line[0].split(',')
        line[2] = line[2].split(',')
        for i in 0, 2:
            for j in 0, 1:
                line[i][j] = int(line[i][j])
        # vents.append([line[0], line[2]])
        vents.append({'start': {'col': line[0][0], 'row': line[0][1]}, 'end': {'col': line[2][0], 'row': line[2][1]}})

grid = []
for i in range(0, size):
    row = []
    for j in range(0, size):
        row.append(0)
    grid.append(row)

for vent in vents:
    # Moving Across
    if vent['start']['row'] == vent['end']['row']:
        for c in range(min(vent['start']['col'], vent['end']['col']), max(vent['start']['col'], vent['end']['col']) + 1):
            grid[vent['start']['row']][c] += 1
    # Moving Virtical
    elif vent['start']['col'] == vent['end']['col']:
        for r in range(min(vent['start']['row'], vent['end']['row']), max(vent['start']['row'], vent['end']['row']) + 1):
            grid[r][vent['start']['col']] += 1

total = 0
for i in range(0, size):
    for j in range(0, size):
        if grid[i][j] > 1:
            total += 1

print(total)