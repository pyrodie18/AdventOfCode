import networkx as nx

def get_data():
    from os import path

    data = {}

    with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
        for line in f:
            line = line.strip()
            line = line.split(":")
            line[1] = line[1].split()
            data[line[0]] = line[1]
    return data

def next_device(mapping, current_deivce):
    found = 0
    for d in mapping[current_deivce]:
        if d == "out":
            found += 1
        else:
            found += next_device(mapping, d)
    return found

def build_graph(data, start, end, required_nodes):
    G = nx.DiGraph()
    G.add_edges_from([(k, d) for k, v in data.items() for d in v])
    del_nodes = []
    print(len(list(G.edges)))
    
    
    for node in G.nodes():
        if not nx.has_path(G, start, node):
            del_nodes.append(node)
        elif not nx.has_path(G, node, end):
            del_nodes.append(node)
        else:
            for n in required_nodes:
                if not (nx.has_path(G, node, n) or nx.has_path(G, n, node)):
                    del_nodes.append(node)
                    break
    G.remove_nodes_from(del_nodes)
      
    return G

def part1(data):
    answer = 0
    device = "you"
    answer += next_device(data, device)
    print('Part 1:  {}'.format(str(answer)))

def part2(data):
    answer = 1
    G = build_graph(data, "svr", "out", ["dac", "fft"])
    
    points = [("svr", "fft"), ("fft", "dac"), ("dac", "out")]
    for p in points:
        total = 0
        for path in nx.all_simple_paths(G, p[0], p[1]):
            total += 1
        answer *= total
        print('{}:  {}'.format(p, str(total)))
    print('Part 2:  {}'.format(str(answer)))

data = get_data()
part1(data)
part2(data)