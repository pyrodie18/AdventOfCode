

def get_data():
    from os import path
    from collections import defaultdict

    data = defaultdict(list)

    with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
        for y, line in enumerate(f):
            line = list(line.strip())
            for x, i in enumerate(line):
                if i != ".":
                    data[i].append((x,y))
    return data, (len(line), y)

def fill_antinodes(cordinate, slope, direction, grid_size, fill=False):
    antinodes = []
    
    x, y = cordinate
    run, rise = slope
    
    if direction == "-":
        rise *= -1
        run *= -1
        
    x += run
    y += rise

    if fill:
        antinodes.append(cordinate)
        while (0 <= (x) < grid_size[0]) and (0 <= (y) <= grid_size[1]):
            antinodes.append((x, y))
            x += run
            y += rise        
    else:
        if (0 <= (x) < grid_size[0]) and (0 <= (y) <= grid_size[1]):
            antinodes.append((x, y))
            
    return antinodes
        
    

def calculate_antinodes(locations, grid_size, fill=False):
    from itertools import combinations
    antinodes = []
    
    pairs = combinations(locations, 2)
    for pair in pairs:
        rise = pair[1][1] - pair[0][1]
        run = pair[1][0] - pair[0][0]
        antinodes += (fill_antinodes(pair[0], (run, rise), "-", grid_size, fill))
        antinodes += (fill_antinodes(pair[1], (run, rise), "+", grid_size, fill))
        
    return antinodes
        
def part1(data, grid_size):
    answer = []
    
    for key in data.keys():
        answer += (calculate_antinodes(data[key], grid_size))
    
    answer = len(set(answer))
    print('Part 1:  {}'.format(str(answer)))

def part2(data, grid_size):
    answer = []
    
    for key in data.keys():
        answer += (calculate_antinodes(data[key], grid_size, True))
    
    answer = len(set(answer))
    print('Part 1:  {}'.format(str(answer)))

data, grid_size = get_data()
part1(data, grid_size)
part2(data, grid_size)