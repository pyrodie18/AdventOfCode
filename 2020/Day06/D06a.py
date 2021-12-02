from collections import defaultdict

with open('./Day06/D06_Input.txt') as f:
    lines = [line.rstrip() for line in f]

groups = []

answers = defaultdict(int)
for line in lines:
    if len(line) > 0:
        for i in line:
            answers[i] += 1
    else:
        groups.append(answers)
        answers = defaultdict(int)
groups.append(answers)

total = 0
for group in groups:
    total += len(group)

print(total)