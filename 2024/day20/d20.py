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
                start = (x, y)          
    return start, end

def find_candidate(grid, cord, X, Y):
    x, y = cord
    R = grid[y][x + 1] if (x + 1 in range(X)) else "#"
    L = grid[y][x - 1] if (x - 1 in range(X)) else "#"
    U = grid[y - 1][x] if (y - 1 in range(Y)) else "#"
    D = grid[y + 1][x] if (y + 1 in range(Y)) else "#"
    
    if L != "#" and R != "#" and U == "#" and D == "#":
        return ((x, y), (x - 1, y), (x + 1, y))
    elif U != "#" and D != "#" and L == "#" and R == "#":
        return ((x, y), (x, y - 1), (x, y + 1))
    else:
        return False
        
def build_graph(grid):
    G = nx.DiGraph()
    Y = len(grid)
    X = len(grid[0])
    candidates = []
    
    
    for y in range(1, Y - 1, 1):
        for x in range(1, X- 1, 1):
            if grid[y][x] == "#":
                candidate = find_candidate(grid, (x, y), X, Y)
                if candidate:
                    candidates.append(candidate)
                continue
            if (x + 1 in range(X)) and (grid[y][x + 1] != "#"):
                G.add_edge((x, y), (x + 1, y))
                G.add_edge((x + 1, y), (x, y))
            if (y + 1 in range(Y)) and (grid[y + 1][x] != "#"):
                G.add_edge((x, y), (x, y + 1))
                G.add_edge((x, y + 1), (x, y))
                
    return G, candidates

def draw(G):
    import matplotlib
    import matplotlib.pyplot
    
    pos = nx.spring_layout(G, seed=20160)
    
    fig = matplotlib.pyplot.figure()
    nx.draw_networkx(G, pos ,arrows=True, ax=fig.add_subplot(), with_labels=False )
    matplotlib.use("Agg")
    fig.savefig("graph.png")

def part1(grid):
    G, candidates = build_graph(grid)
    # draw(G)
    start, end = find_start(grid)
    answer = 0
    
    baseline = nx.shortest_path_length(G, start, end)
    for candidate in candidates:
        G.add_edge(candidate[1], candidate[0])
        G.add_edge(candidate[0], candidate[2])
        time = nx.shortest_path_length(G, start, end)
        if baseline - time >= 100:
            answer += 1
            # print(baseline - time)
        G.remove_node(candidate[0])
        # Other Direction
        G.add_edge(candidate[2], candidate[0])
        G.add_edge(candidate[0], candidate[1])
        time = nx.shortest_path_length(G, start, end)
        if baseline - time >= 100:
            answer += 1
            # print(baseline - time)
        G.remove_node(candidate[0])
            
    print('Part 1:  {}'.format(str(answer)))

def part2(data):
    answer = None
    # print('Part 2:  {}'.format(str(answer)))

data = get_data()
part1(data)
part2(data)