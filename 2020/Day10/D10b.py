from collections import defaultdict
from itertools import combinations

def check_arrangement(arrangement):
    for j in range (len(arrangement) - 1):
        if arrangement[j + 1] - arrangement[j] > 3:
            return False
    return True


with open('./Day10/D10_Input.txt') as f:
    lines = [int(line.rstrip()) for line in f]
outlet_voltage = 0
system_volatge = max(lines) + 3
lines.sort()
print(lines)

valid_arrangements = defaultdict(int)
min_number = (max(lines) // 3) + 1

for i in range (min_number, len(lines) + 1):
    arrangements = combinations(lines, i)
    for arrangement in arrangements:
        arrangement = list(arrangement)
        if not (system_volatge - 3) in arrangement:
            continue
        arrangement.append(0)
        arrangement.append(system_volatge)
        arrangement.sort()
        if check_arrangement(arrangement):
            valid_arrangements[tuple(arrangement)] += 1

print(len(list(valid_arrangements.keys())))
