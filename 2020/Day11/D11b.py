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

    # Check Left
    for c in range(column - 1, -1, -1):
        if area[row][c] != '.':
            seats[area[row][c]] += 1
            break
    # Check Right
    for c in range(column + 1, column_count):
        if area[row][c] != '.':
            seats[area[row][c]] += 1
            break
    # Check Up
    for r in range(row - 1, -1, -1):
        if area[r][column] != '.':
            seats[area[r][column]] += 1
            break
    # Check Down
    for r in range(row + 1, row_count):
        if area[r][column] != '.':
            seats[area[r][column]] += 1
            break
    # Up Left
    angles = [(-1,-1), (-1, 1), (1, -1), (1, 1)]
    for angle in angles:
        r = row + angle[0]
        c = column + angle[1]
        while True:
            if (r < 0 or r >= row_count) or (c < 0 or c >= column_count):
                break
            else:
                if area[r][c] != '.':
                    seats[area[r][c]] += 1
                    break
                else:
                    r += angle[0]
                    c += angle[1]


    if seats['#'] == 0:
        return '#'
    elif seats['#'] >= 5:
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