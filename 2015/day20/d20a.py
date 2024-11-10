import numpy as np

DesiredPresents = 34000000
max_limit = DesiredPresents // 10
# houses = np.zeros(max_limit + 1)

for i in range(1, max_limit + 1):
    houses[i:max_limit:i] += 10 * i
tmp = np.where(houses >= DesiredPresents)
print(tmp[0][0])


# Part 2
houses = np.zeros(max_limit + 1)

for i in range(1, max_limit + 1):
    houses[i : i * 50 : i] += 11 * i
tmp = np.where(houses >= DesiredPresents)
print(tmp[0][0])
