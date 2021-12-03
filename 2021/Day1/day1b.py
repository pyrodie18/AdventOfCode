depths = []


with open(".\\2021\Day1\input.txt", "r") as f:
    for line in f:
        depths.append(int(line))

increase_count = 0

combined_depths = []
for i in range(0, len(depths) - 2):
    combined_depths.append(sum(depths[i:i+3]))

old_depth = combined_depths[0]
for depth in combined_depths:
    if depth > old_depth:
        increase_count += 1
    old_depth = depth

print(increase_count)