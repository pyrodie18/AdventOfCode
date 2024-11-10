import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)

problem_input = [[0,0,1,0,0,1,0,0], [0,1,1,1,0,0,1,0], [1,0,0,1,1,0,1,0], [1,0,1,0,1,0,1,0], [0,1,0,0,1,1,1,0], [0,0,0,0,0,1,0,0], [1,0,0,0,1,1,1,1], [1,1,0,0,0,0,1,0]]

pocket = np.zeros((50, 50, 50), dtype=int)
new_pocket = np.zeros_like(pocket)
start = 25
z = start

def get_state(location, pocket):
    z = location[0]
    y = location[1]
    x = location[2]
    size = 50
    current_state = pocket[z,y,x]
    total_on = 0

    for iz in range(max(z - 1, 0), min(z + 2, size - 1)):
        for iy in range(max(y - 1, 0), min(y + 2, size - 1)):
            for ix in range(max(x - 1, 0), min(x + 2, size - 1)):
                if [z, y, x] == [iz, iy, ix]:
                    continue
                if pocket[iz,iy,ix] == 1:
                    total_on += 1
    
    if current_state == 1 and (total_on == 2 or total_on == 3):
        return 1
    elif current_state == 0 and (total_on == 3):
        return 1
    else:
        return 0

for y, row in enumerate(problem_input):
    for x, column in enumerate(row):
        pocket[z, start + y, start + x] = column
# print(pocket)

for cycles in range(6):
    for z, depth in enumerate(pocket):
        for y, row in enumerate(depth):
            for x, column in enumerate(row):
                new_pocket[z,y,x] = get_state([z,y,x], pocket)

    pocket = np.copy(new_pocket)
    new_pocket = np.zeros_like(pocket,dtype=int)

total = 0
for z, depth in enumerate(pocket):
    for y, row in enumerate(depth):
        for x, column in enumerate(row):
            if column == 1:
                total += 1

print(total)