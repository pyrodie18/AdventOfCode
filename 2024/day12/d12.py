import networkx as nx

def get_data():
    from os import path

    data = []

    with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
        for line in f:
            data.append(list(line.strip()))
    return data

def find_neighbors(grid, cord):
    neighbors = []
    x, y = cord
    
    for dir in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        dx, dy = dir
        xx = dx + x
        yy = dy + y
        
        if xx in range(len(grid[0])) and yy in range(len(grid)):
            if grid[yy][xx] == grid[y][x]:
                neighbors.append((xx, yy))
                
    return neighbors

def find_regions(grid):
    G = nx.Graph()
    
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            neighbors = find_neighbors(grid, (x,y))
            if len(neighbors) > 0:
                for neighbor in neighbors:
                    G.add_edge((x,y), neighbor)
            else:
                G.add_node((x,y))
                
    return G

def survey(region, G):
    fence = 0
    plots = len(list(region))
    for plot in region:
        fence += 4 - len(list(G.neighbors(plot)))
        
    return plots * fence

def mod_survey(region):
    plots = len(list(region))
    corners = 0
    for cur_plot in region:
        x, y = cur_plot
        for xx, yy in[(1, 1), (1, -1), (-1, 1), (-1, -1)]:
            x_neighbor = (x + xx, y)
            y_neighbor = (x, y + yy)
            d_neighbor = (x + xx, y + yy)
            
            if x_neighbor not in region and y_neighbor not in region:
                corners += 1
                
            if (x_neighbor in region) and (y_neighbor in region) and (d_neighbor not in region):
                corners += 1
    return corners * plots

def part1(grid):
    answer = 0
    G = find_regions(grid)
    
    for region in nx.connected_components(G):
        answer += survey(region, G)
        
    print('Part 1:  {}'.format(str(answer)))

def part2(grid):
    answer = 0
    G = find_regions(grid)
    
    for region in nx.connected_components(G):
        answer += mod_survey(region)
    print('Part 2:  {}'.format(str(answer)))

data = get_data()
part1(data)
part2(data)