import networkx as nx

def get_data():
    from os import path

    data = []

    with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
        for line in f:
            data.append(line.strip().split(")"))
    return data

def build_graph(data):
    G = nx.Graph()
    for line in data:
        G.add_edge(line[0], line[1])
        
    return G

def part1(G):
    
    answer = 0
      
    for node in G.nodes():
        i = nx.shortest_path_length(G, node, "COM")
        answer += i
    print('Part 1:  {}'.format(str(answer)))

def part2(G):
    YOU = list(nx.neighbors(G,"YOU"))
    SAN = list(nx.neighbors(G,"SAN"))
    answer = nx.shortest_path_length(G, YOU[0], SAN[0])
    print('Part 2:  {}'.format(str(answer)))

data = get_data()
G = build_graph(data)
part1(G)
part2(G)