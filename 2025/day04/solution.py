from collections import defaultdict

def get_data():
    from os import path

    data = defaultdict(list)

    with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
        l = 0
        for line in f:
            line = line.strip()
            for i, j in enumerate(line):
                if j == "@":
                    data[l].append(i)
            l += 1
    return data

def find_adjacent(grid, x, y):
    total = 0
    for cx in range(x-1, x+2):
        for cy in range(y-1, y+2):
            if cx in grid.keys() and cy in grid[cx]:
                total += 1
    return total - 1

def part1(data):
    answer = 0
    
    for x in data.keys():
        for y in data[x]:
            if find_adjacent(data, x, y) <= 3:
                answer += 1
    print('Part 1:  {}'.format(str(answer)))

def part2(data):
    answer = 0
    
    while True:
        pending = []
        for x in data.keys():
            for y in data[x]:
                if find_adjacent(data, x, y) <= 3:
                    pending.append((x,y))
        if len(pending) == 0:
            break
        else:
            answer += len(pending)
            for i in pending:
                data[i[0]].remove(i[1])
                        
    print('Part 2:  {}'.format(str(answer)))

data = get_data()
part1(data)
part2(data)