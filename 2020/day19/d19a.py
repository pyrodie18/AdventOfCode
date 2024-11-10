from os import path

with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
    lines = [line.rstrip() for line in f]

rules = {}

for line in lines:
    index = line.split(":")[0]
    rules[index] = line.split(":")[1].split()

