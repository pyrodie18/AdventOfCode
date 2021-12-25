from functools import total_ordering
import os
from collections import defaultdict

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), "r") as f:
    inputs = f.readlines()

tmp = inputs[0].strip()
start = []
start[:0] = tmp

pair_rules = {}
for line in inputs[2:]:
    line = line.strip()
    line = line.split(' ')
    pair_rules[line[0]] = line[2]

for a in range(10):
    new_poly = []
    for i in range(len(start) - 1):
        current_pair = start[i: i+2]
        new_poly.append(current_pair[0])
        try:
            new_poly.append(pair_rules["{}{}".format(current_pair[0], current_pair[1])])
        except:
            continue
    new_poly.append(current_pair[1])
    start = new_poly

totals = defaultdict(int)
count = {}
for i in start:
    totals[i] += 1

high = 0
low = len(start)

for i in totals.keys():
    high = max(high, totals[i])
    low = min(low, totals[i])

print(high - low)