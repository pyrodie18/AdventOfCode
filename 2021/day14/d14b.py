import cProfile
from functools import total_ordering
import os
from collections import defaultdict
import numpy as np
import re

profiler = cProfile.Profile()
profiler.enable()
with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as f:
    inputs = f.readlines()

start = inputs[0].strip()
# start = []
# start[:0] = tmp

pair_rules = {}
for line in inputs[2:]:
    line = line.strip()
    line = line.split(" ")
    pair_rules[line[0]] = line[2]

for a in range(40):
    new_poly = np.chararray(len(start), itemsize=2)
    for key in pair_rules.keys():
        new_val = key[0] + pair_rules[key]
        for match in re.finditer("(?=(" + key + "))", start):
            new_poly[match.start()] = new_val
    new_poly[-1] = start[-1]
    start = new_poly.tostring().decode().rstrip("\x00")

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

profiler.disable()
profiler.print_stats()
