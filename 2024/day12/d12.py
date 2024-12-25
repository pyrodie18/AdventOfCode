import networkx as nx
from shapely.geometry import Polygon
from shapely.ops import unary_union
from sympy import Polygon as symPolygon
from sympy import Point


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
    shapes = []
    sides = 0
    for cur_plot in region:
        x, y = cur_plot
        shapes.append(Polygon([(x, y), (x, y + 1), (x + 1, y + 1), (x + 1, y), (x, y)]))
    
    
    union_shape = unary_union(shapes)
    outline = list(union_shape.exterior.coords)
    
    i = 1
    while i < len(outline) - 1:
    # for i in range(1, len(outline) - 1, 1):
        if (outline[i - 1][0] == outline[i][0] == outline[i + 1][0]) or (outline[i - 1][1] == outline[i][1] == outline[i + 1][1]):
            outline.pop(i)
            i = 1
        else:
            i += 1
    outline.pop(-1)
    if (outline[0][0] == outline[1][0] == outline[-1][0]) or (outline[0][1] == outline[1][1] == outline[-1][1]):
        outline.pop(0)
    # elif (outline[0][0] == outline[-1][0] == outline[-2][0]) or (outline[0][1] == outline[-1][1] == outline[-2][1]):
    #     outline.pop(-1)
    
    # simplified_shape = symPolygon(*xy)
    # a = tuple(map(Point, simplified_shape.angles))
    # for p in a:
    #     b = simplified_shape.angles[p]
    #     if len(b.args) > 0:
    #         sides += 1
    sides = len(outline)
    return sides

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
        x, y = list(region)[0]
        plant = grid[y][x]
        area = len(region)
        if plant == "E":
            pass
        sides = mod_survey(region)
        print(f'{plant} (area: {area}, edges: {sides})')# : {region}')
        # answer += mod_survey(region)
    # print('Part 2:  {}'.format(str(answer)))

data = get_data()
# part1(data)
part2(data)