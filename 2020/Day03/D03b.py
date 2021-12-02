with open('./Day03/D03_Input.txt') as f:
    lines = [line.rstrip() for line in f]

slopes = [[1,1], [3,1], [5,1], [7,1], [1,2]]
total = 1
sec_len = len(lines[0])
forest_len = len(lines)

for slope in slopes:
    v = 0
    h = 0
    encounters = 0
    while v < forest_len:
        v = v + slope[1]
        h = h + slope[0]
        if h >= sec_len:
            h = h - sec_len
        try:
            if lines[v][h] == '#':
                encounters = encounters +1
        except:
            print(encounters)

    total = total * encounters

print(total)