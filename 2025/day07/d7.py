from collections import defaultdict
def get_data():
    from os import path

    data = []

    with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
        for line in f:
            line = line.strip()
            data.append(list(line))
    return data

def find_splitters(start, grid):
    found = 0
    r, c  = start
    
    while 0 <= c <= len(grid[0]) and 0 <= r <= (len(grid) - 1):

        if grid[r][c] == "." or grid[r][c] == "S":
            grid[r][c] = "|"
            r += 1
        elif grid[r][c] == "|":
            return found
        elif grid[r][c] == "^":
            found += find_splitters((r, c-1), grid)
            found += find_splitters((r, c+1), grid)
            found += 1
            break
    return found

def assign_nodes(grid):
    node = 1
    for y, r in enumerate(grid):
        for x, s in enumerate(r):
            if s == "^":
                grid[y][x] = str(node)
                node += 1
    return grid

def traverse(grid, start):
    x, y = start
    while 0 <= y <= (len(grid) - 1):
        if grid[y][x] == ".":
            y += 1
        else:
            return grid[y][x]
    return "exit"

def build_graph(grid):
    Graph = defaultdict(list)
    Graph["Start"].append("1")
    for y, r in enumerate(grid):
        for x, s in enumerate(r):
            if s != "." and s != "S":
                Graph[s].append(traverse(grid, (x - 1, y)))
                Graph[s].append(traverse(grid, (x + 1, y)))
    return Graph

def count_paths(Graph):
    Pathes = {}
    for i in range(len(Graph.keys()) - 1,0,-1):
        total = 0
        for n in Graph[str(i)]:
            if n == "exit":
                total += 1
            else:
                total += Pathes[int(n)]
        Pathes[i] = total
    return Pathes[1]

def part1(data):
    start = (0, int(len(data[0]) // 2))
    answer = find_splitters(start, data)
    print('Part 1:  {}'.format(str(answer)))

def part2(data):
    grid = assign_nodes(data)
    G = build_graph(grid)
    answer = count_paths(G)
    print('Part 2:  {}'.format(str(answer)))

data = get_data()
# part1(data)
part2(data)