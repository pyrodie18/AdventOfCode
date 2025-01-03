from collections import defaultdict
from os import path

with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
    lines = [int(line.rstrip()) for line in f]
lines.append(0)
lines.append(max(lines) + 3)

adapters = []
differences = defaultdict(int)

for line in lines:
    adapters.append(int(line))

adapters.sort()
print(adapters)

for i in range (len(adapters) - 1):
    differences[adapters[i + 1] - adapters[i]] += 1
#    print(str(adapters[i + 1]) + " - " + str(adapters[i]) + " = " + str(adapters[i + 1] - adapters[i]))

print(differences)
print(differences[1] * differences[3])