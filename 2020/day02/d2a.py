from os import path

with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
    lines = [line.rstrip() for line in f]

total = 0

for line in lines:
    line = line.split(' ')
    count = line[2].count(line[1][0])
    if (count >= int(line[0].split('-')[0])) and (count <= int(line[0].split('-')[1])):
        total = total + 1

print(total)
    