import os

counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 , 0]
answer = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 , 0]
length = 0

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), "r") as f:
    for line in f:
        for i, bit in enumerate(line):
            if bit == '1':
                counts[i] += 1
        length += 1

midpoint = length / 2
for i, count in enumerate(counts):
    if count >= midpoint:
        answer[i] = 1
    else:
        answer[i] = 0

gamma = ''
for i in answer:
    gamma += str(i)
gamma = int(gamma, 2)

for i, bit in enumerate(answer):
    if bit == 1:
        answer[i] = 0
    else:
        answer[i] = 1

epsilon = ''
for i in answer:
    epsilon += str(i)
epsilon = int(epsilon, 2)

print(gamma * epsilon)