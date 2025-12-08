from itertools import combinations
from math import sqrt
import networkx as nx

size = 1000

def get_data():
    from os import path

    data = []
    G = nx.Graph()

    with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
        for line in f:
            line = line.strip().split(",")
            node = ((int(line[0]), int(line[1]), int(line[2])))
            G.add_node(node)
            data.append(node)
    return data, G

def measure_distance(data):
    distances = {}
    for c in combinations(data, 2):
        d = 0
        for i in range(0, 3):
            d += (c[0][i] - c[1][i])**2
        distances[sqrt(d)] = c
    return distances

def add_edges(distances, G):
    costs = sorted(list(distances.keys()))
    for i in range(size):
        a = distances[costs[i]][0]
        b = distances[costs[i]][1]
        G.add_edge(a,b)
    return G
        
    
def part1(data, G):
    distances = measure_distance(data)
    G = add_edges(distances, G)
    sizes = [len(c) for c in sorted(nx.connected_components(G), key=len, reverse=True)]
    answer = 1
    for i in range(3):
        answer *= sizes[i]
    print('Part 1:  {}'.format(str(answer)))
    return G, distances

def part2(G, distances):
    i = size
    costs = sorted(list(distances.keys()))
    while nx.number_connected_components(G) > 1:
        a = distances[costs[i]][0]
        b = distances[costs[i]][1]
        G.add_edge(a,b)
        i += 1
    x1 = distances[costs[i-1]][0][0]
    x2 = distances[costs[i-1]][1][0]
    answer = x1 * x2
    print('Part 2:  {}'.format(str(answer)))

data, G = get_data()
G, distances  = part1(data, G)
part2(G, distances)