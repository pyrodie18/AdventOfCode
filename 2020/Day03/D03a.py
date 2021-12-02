with open('D03_Input.txt') as f:
    lines = [line.rstrip() for line in f]

sec_len = len(lines[0])
forest_len = len(lines)
v = 0
h = 0
encounters = 0
while v < forest_len:
    v = v + 1
    h = h + 3
    if h >= sec_len:
        h = h - sec_len
    try:
        if lines[v][h] == '#':
            encounters = encounters +1
    except:
        print("encounters")
