import networkx as nx

def get_data():
    from os import path

    data = []

    with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
        for line in f:
            data.append(line.strip().split("-"))
    return data

def build_graph(data):
    G = nx.Graph()
    for line in data:
        G.add_edge(line[0], line[1])
        
    return G

def part1(data):
    answer = 0
    t_computers = set()
    G = build_graph(data)
    
    for node in G.nodes:
        if node[0] == "t":
            t_computers.add(node)

    all_cliques= nx.enumerate_all_cliques(G)
    triad_cliques=[x for x in all_cliques if len(x)==3 ]
    for triangle in triad_cliques:
        for node in t_computers:
            if node in triangle:
                answer += 1
                break
    
    print('Part 1:  {}'.format(str(answer)))

def part2(data):
    answer = 0
    G = build_graph(data)
    
    all_cliques= list(nx.enumerate_all_cliques(G))
    max_clique = all_cliques[-1]
    max_clique = sorted(max_clique)
    answer = ",".join(max_clique)

    
    print('Part 2:  {}'.format(str(answer)))

data = get_data()
part1(data)
part2(data)