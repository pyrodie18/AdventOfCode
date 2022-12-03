import os

values = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
score1 = 0
score2 = 0
input = []

with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as f:
    for line in f:
        line = line.strip()
        l = len(line) // 2
        tmp = [line[0:l], line[l:]]
        input.append(line)
        for c in tmp[0]:
            if c in tmp[1]:
                score1 += values.rfind(c) + 1
                break

for i in range(0, len(input), 3):
    x = set(input[i])
    y = set(input[i + 1])
    z = set(input[i + 2])
    score2 += values.rfind(list(x.intersection(y, z))[0]) + 1

print(score1)
print(score2)
