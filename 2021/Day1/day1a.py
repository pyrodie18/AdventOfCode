depths = []


with open(".\\2021\Day1\input.txt", "r") as f:
    for line in f:
        depths.append(int(line))


increase_count = 0
old_depth = depths[0]
for depth in depths:
    if depth > old_depth:
        increase_count += 1
    old_depth = depth

print(increase_count)