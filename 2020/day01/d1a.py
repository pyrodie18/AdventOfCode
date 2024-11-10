from itertools import combinations
from os import path

with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
    lines = [line.rstrip() for line in f]

a1 = combinations(lines, 2)
for i in a1:
    if int(i[0]) + int(i[1]) == 2020:
        print(int(i[0]) * int(i[1]))

a2 = combinations(lines, 3)
for i in a2:
    if (int(i[0]) + int(i[1]) + int(i[2])) == 2020:
        print(int(i[0]) * int(i[1]) * int(i[2]))