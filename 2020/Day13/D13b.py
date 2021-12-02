import math

def all_equal(v):
    for i in range(1, len(v)):
        if v[i] != v[i - 1]:
            return False
    return True

with open('./Day13/D13_Input.txt') as f:

    _ = f.readline()  # ignore the first line
    periods = []
    positions = []
    
    for i, n in enumerate(f.readline().split(',')):
        if n != 'x':
            periods.append(int(n))
            positions.append(-i)    
    while not all_equal(positions):
        min_idx = positions.index(min(positions))
        max_idx = positions.index(max(positions))
        k = math.ceil((positions[max_idx] - positions[min_idx]) / periods[min_idx])
        positions[min_idx] += int(k * periods[min_idx])
        if positions[min_idx] == positions[max_idx]:
            # These 2 buses are now in sync and will only be in sync again with a period of lcm(period_a, period_b)
            periods[max_idx] = math.lcm(periods[min_idx], periods[max_idx])
            del periods[min_idx]
            del positions[min_idx]
    print(f'Part 2: {positions[0]}')