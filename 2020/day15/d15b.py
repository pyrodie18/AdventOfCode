starting_nums = [0,3,6]

sequence = {}

for i in range(1, len(starting_nums) + 1):
    sequence[starting_nums[i-1]] = i

current_num = 0

for i in range(len(starting_nums) + 1, 2020):
    if current_num in sequence:
        distance = i - sequence[current_num]
    else:
        distance = 0
    sequence[distance] = i
    current_num = distance

print(sequence[-1])