import os

input = []
calories = []

with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as f:
    for line in f:
        input.append(line.strip())

current_total = 0
for line in input:
    if line == "":
        calories.append(current_total)
        current_total = 0
    else:
        current_total += int(line)

calories.sort(reverse=True)

print(calories[0])

top3 = sum(calories[0:3])
print(top3)
