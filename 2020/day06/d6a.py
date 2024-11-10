from collections import defaultdict
from os import path

with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
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