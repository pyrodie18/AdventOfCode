import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)

#problem_input = [[0,0,1,0,0,1,0,0], [0,1,1,1,0,0,1,0], [1,0,0,1,1,0,1,0], [1,0,1,0,1,0,1,0], [0,1,0,0,1,1,1,0], [0,0,0,0,0,1,0,0], [1,0,0,0,1,1,1,1], [1,1,0,0,0,0,1,0]]
problem_input = [[0,1,0], [0,0,1], [1,1,1]]

pocket = np.zeros((10, 10, 10, 10), dtype=int)
new_pocket = np.zeros_like(pocket)
start = 5
z = start

def get_state(location, pocket):
    w = location[0]
    z = location[1]
    y = location[2]
    x = location[3]
    size = 10
    current_state = pocket[w,z,y,x]
    total_on = 0

    for iw in range(max(w - 1, 0), min(w + 2, size - 1)):
        for iz in range(max(z - 1, 0), min(z + 2, size - 1)):
            for iy in range(max(y - 1, 0), min(y + 2, size - 1)):
                for ix in range(max(x - 1, 0), min(x + 2, size - 1)):
                    if [w, z, y, x] == [iw, iz, iy, ix]:
                        continue
                    if pocket[iw, iz,iy,ix] == 1:
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

for cycles in range(3):
    for w, time in enumerate(pocket):
        for z, depth in enumerate(time):
            for y, row in enumerate(depth):
                for x, column in enumerate(row):
                    new_pocket[w,z,y,x] = get_state([w,z,y,x], pocket)

    pocket = np.copy(new_pocket)
    new_pocket = np.zeros_like(pocket,dtype=int)

print(pocket)

# total = 0
# for z, time in enumerate(pocket):
#     for z, depth in enumerate(time):
#         for y, row in enumerate(depth):
#             for x, column in enumerate(row):
#                 if column == 1:
#                     total += 1

# print(total)