import os

postition = [0, 0]
with open(os.path.join(os.path.dirname(__file__), 'input.txt'), "r") as f:
    for line in f:
        line = line.split()
        move = line[0]
        if move == "forward":
            postition[0] += int(line[1])
        elif move == "down":
            postition[1] += int(line[1])
        else:
            postition[1] -= int(line[1])

print(postition[0] * postition[1])