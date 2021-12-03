position = {'forward': 0, 'depth': 0, 'aim': 0}
with open(".\\2021\Day2\input.txt", "r") as f:
    for line in f:
        line = line.split()
        move = line[0]
        if move == "forward":
            position['forward'] += int(line[1])
            position['depth'] += (int(line[1]) * position['aim'])
        elif move == "down":
            position['aim'] += int(line[1])
        else:
            position['aim'] -= int(line[1])

print(position['depth'] * position['forward'])