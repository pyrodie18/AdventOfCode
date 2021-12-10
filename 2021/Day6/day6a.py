import os
cycles = 256
current_timer = [0] * 9
new_timer = [0] * 9
day = 1

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), "r") as f:
    for line in f:
        line = line.split(',')
for i in range(len(line)):
    current_timer[int(line[i])] += 1

while day <= cycles:
    new_timer = [0] * 9
    new_timer[8] = current_timer[0]
    new_timer[6] = current_timer[0]
    for i in range(1,9):
        new_timer[i-1] += current_timer[i]
    for i in range(9):
        current_timer[i] = new_timer[i]
    print(current_timer)
    day += 1

print(sum(current_timer))


