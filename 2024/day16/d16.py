import networkx as nx

def get_data():
    from os import path

    data = []

    with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
        for line in f:
            data.append(list(line.strip()))
    return data

def find_start(grid):
    start = None
    end = None
    for y, line in enumerate(grid):
        for x, val in enumerate(line):
            if val == "E":
                end = (x, y)
            elif val == "S":
                start = "H({}, {})".format(x, y)
                
    return start, end

def build_graph(grid):
    G = nx.Graph()
    Y = len(grid)
    X = len(grid[0])
    
    
    for y in range(Y):
        for x in range(X):
            if grid[y][x] == "#":
                continue
            H = False
            V = False
            if (x + 1 in range(X)) and (grid[y][x + 1] != "#"):
                G.add_edge("H({}, {})".format(x, y), "H({}, {})".format(x + 1, y), weight = 1)
                H = True
            if (y + 1 in range(Y)) and (grid[y + 1][x] != "#"):
                G.add_edge("V({}, {})".format(x, y), "V({}, {})".format(x, y + 1), weight = 1)
                V = True
            if (x - 1 in range(X)) and (grid[y][x - 1] != "#"):
                G.add_edge("H({}, {})".format(x, y), "H({}, {})".format(x - 1, y), weight = 1)
                H = True
            if (y - 1 in range(Y)) and (grid[y - 1][x] != "#"):
                G.add_edge("V({}, {})".format(x, y), "V({}, {})".format(x, y - 1), weight = 1)
                V = True
            if H and V:
                G.add_edge("V({}, {})".format(x, y), "H({}, {})".format(x, y), weight = 1000)
                
    return G

def score(route):
    score = 0
    dir = "right"
    i = 0
    
    for i in range(len(route) - 1):
        x, y = route[i]
        nx, ny = route[i + 1]
        
        if y == ny:
            if dir == "right":
                score += 1
            else:
                score += 1001
                dir = "right"
        else:
            if dir == "up":
                score += 1
            else:
                score += 1001
                dir = "up"
        i += 1
        
    return score
        

        

def part1(G, start, end):
    ex, ey = end
    
    path1 = nx.shortest_path(G, source=start, target="H({}, {})".format(ex, ey), weight="weight")
    path2 = nx.shortest_path(G, source=start, target="V({}, {})".format(ex, ey), weight="weight")
    cost1 = nx.path_weight(G, path1, weight="weight")
    cost2 = nx.path_weight(G, path2, weight="weight")
        
    print('Part 1:  {}'.format(str(min(cost1, cost2))))

def part2(G, start, end):
    nodes = set()
    ex, ey = end
    paths = nx.all_shortest_paths(G, source=start, target="V({}, {})".format(ex, ey), weight="weight")
    for path in paths:
        for node in path:
            node = node[2:-1]
            node = node.split(",")
            nodes.add((node[0], node[1]))
            
    print('Part 1:  {}'.format(str(len(nodes))))
    
data = get_data()
G = build_graph(data)
start, end = find_start(data)
part1(G, start, end)
part2(G, start, end)