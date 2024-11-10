import os
min_value = 100000000000
low_position = 0
crabs = []
with open(os.path.join(os.path.dirname(__file__), 'input.txt'), "r") as f:
    for line in f:
        line = line.split(',')
        for i in line:
            crabs.append(int(i))

for pos in range(0, max(crabs)):
    fuel = 0
    for crab in crabs:
        cost = abs((crab - pos))
        cost = (cost * (cost + 1)) / 2
        fuel += cost
    if fuel < min_value:
        min_value = fuel
        low_position = pos

print(low_position)
print(min_value)