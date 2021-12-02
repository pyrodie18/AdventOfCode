with open('./Day19/D19_Input.txt') as f:
    lines = [line.rstrip() for line in f]

rules = {}

for line in lines:
    index = line.split(":")[0]
    rules[index] = line.split(":")[1].split()

