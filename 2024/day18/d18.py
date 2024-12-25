import networkx as nx

def get_data():
    from os import path

    data = []

    with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
        for line in f:
            line = line.strip().split(",")
            data.append((int(line[0]), int(line[1])))
    return data

def build_graph(X, Y):
    G = nx.Graph()
    for y in range(Y):
        for x in range(X):
            for tx, ty in [(1, 0), (0, 1)]:
                xx = tx + x
                yy = ty + y
                if xx in range(X) and yy in range(Y):
                    G.add_edge((x, y), (xx, yy))
    return G

def part1(data, G):
    for i in range(1024):
        G.remove_node(data[i])
    answer = nx.shortest_path_length(G, (0,0), (70,70))
    print('Part 1:  {}'.format(str(answer)))

def part2(data, G):
    for i in range(1024, len(data)):
        G.remove_node(data[i])
        try:
            answer = nx.shortest_path_length(G, (0,0), (70,70))
        except: 
            print('Part 2:  {}'.format(str(data[i])))
            break

data = get_data()
G = build_graph(71, 71)
part1(data, G)
part2(data, G)