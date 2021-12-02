from collections import deque
from itertools import combinations  

with open('./Day09/D09_Input.txt') as f:
    lines = [int(line.rstrip()) for line in f]

register = deque('',25)

# load register
for i in range (25):
    register.append(lines[i])

for i in range(25, len(lines)):
    value = lines[i]
    combos = combinations(register, 2)
    found = False
    for combo in list(combos):
        if combo[0] + combo[1] == value:
            found = True
    if not found:
        print(value)
        break
    else:
        register.append(value)

for j in range(i):
    current_set = []
    total = 0
    for k in range(j,i):
        total += lines[k]
        current_set.append(lines[k])
        if total == value:
            print("Min " + str(min(current_set)))
            print("Max " + str(max(current_set)))
            print("Total " + str(min(current_set) + max(current_set)))
            exit()