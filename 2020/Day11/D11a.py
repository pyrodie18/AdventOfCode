from collections import defaultdict

with open('./Day11/D11_Input.txt') as f:
    lines = [line.rstrip() for line in f]
area = []

def copy_area(area):
    new_area = []
    
    for row in area:
        new_row = []
        for column in row:
            new_row.append(column)
        new_area.append(new_row)
    return new_area

def check_seat(row, column, area):
    seats = defaultdict(int)
    row_count = len(area)
    column_count = len(area[0])
    current_value = area[row][column]

    for i in range(row - 1, row + 2, 2):
        if i < 0 or i >= row_count:
            continue
        else:
            for j in range(column - 1, column + 2):
                if j < 0 or j >= column_count:
                    continue
                else:
                    seats[area[i][j]] += 1
    if column >= 1:
        seats[area[row][column - 1]] += 1
    if column < (column_count - 1):
        seats[area[row][column + 1]] += 1

    if seats['#'] == 0:
        return '#'
    elif seats['#'] >= 4:
        return 'L'
    else:
        return current_value

for line in lines:
    line = list(line)
    area.append(line)
rows = len(area)
columns = len(area[0])

while True:
    next_map = copy_area(area)
    change = False
    for r in range(rows):
        for c in range(columns):
            if area[r][c] == '.':
                continue
            else:
                next_map[r][c] = check_seat(r, c, area)
                if next_map[r][c] != area[r][c]:
                    change = True
    area = copy_area(next_map)
    if not change:
        break

total = 0
for row in area:
    total += row.count('#')
print(total)