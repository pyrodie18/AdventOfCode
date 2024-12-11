import networkx as nx

L = (-1,0)
R = (1,0)
U = (0,-1)
D = (0,1)
SEQUENCES = [L, R, U, D]

def get_data():
    from os import path

    data = []

    with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
        for line in f:
            line = line.strip()
            tmp = [int(i) for i in line]
            data.append(tmp)
    return data

def find_neighbords(grid, cord):
    valid_neighbors = []
    x, y = cord
    cur_val = grid[y][x]
    
    for x1 in [x - 1, x + 1]:
        if 0 <= x1 <= (len(grid[0]) - 1):
            tmp = grid[y][x1]
            if tmp - cur_val == 1:
                valid_neighbors.append((x1, y))
                
    for y1 in [y - 1, y + 1]:
        if 0 <= y1 <= (len(grid) - 1):
            tmp = grid[y1][x]
            if tmp - cur_val == 1:
                valid_neighbors.append((x, y1))
                
    return valid_neighbors

def build_graph(grid):    
    G = nx.DiGraph()
    for y, line in enumerate(grid):
        for x in range(len(line)):
            valid_neighbors = find_neighbords(grid, (x,y))
            for neighbor in valid_neighbors:
                G.add_edge((x,y), neighbor)
    return G

def find_ends(grid):
    zeros = []
    nines = []
    
    for y, line in enumerate(grid):
        for x, ele in enumerate(line):
            if ele == 9:
                nines.append((x,y))
            elif ele == 0:
                zeros.append((x,y))
                
    return zeros, nines

def part1(grid):
    answer = 0  
    G = build_graph(grid)
    
    # Find Starts and Ends
    zeros, nines = find_ends(grid)
                
    for start in zeros:
        for end in nines:
            try:
                paths = list(nx.all_shortest_paths(G, source=start, target=end))
                if len(paths) > 0: answer += 1 
            except nx.NetworkXNoPath:
                continue
        
            
    print('Part 1:  {}'.format(str(answer)))

def part2(data):
    answer = 0  
    G = build_graph(grid)
    
    # Find Starts and Ends
    zeros, nines = find_ends(grid)
                
    for start in zeros:
        for end in nines:
            try:
                paths = list(nx.all_shortest_paths(G, source=start, target=end))
                answer += len(paths) 
            except nx.NetworkXNoPath:
                continue
        
            
    print('Part 2:  {}'.format(str(answer)))

grid = get_data()
# part1(grid)
part2(grid)