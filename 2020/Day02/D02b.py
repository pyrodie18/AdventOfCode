with open('D02_Input.txt') as f:
    lines = [line.rstrip() for line in f]

total = 0

for line in lines:
    line = line.split(' ')
    count = line[2].count(line[1][0])

    if (line[2][int(line[0].split('-')[0])-1] == line[1][0]) ^ (line[2][int(line[0].split('-')[1])-1] == line[1][0]):
        total = total + 1

print(total)
    