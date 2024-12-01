from collections import defaultdict


class Node():
    def __init__(self, node_name=None, low=None, high=None):
        self.node_name = node_name
        self.values=[]
        self.low_out = low
        self.high_out = high
               
    def add_value(self, value):
        self.values.append(value)
        if len(self.values) == 2 and self.node_name is not None:
            # Check for Part 1 Answer
            if min(self.values) == 17 and max(self.values) == 61:
                print('Part 1:  {}'.format(self.node_name))
            NODES[self.low_out].add_value(min(self.values))
            NODES[self.high_out].add_value(max(self.values))
            self.values = []
        if "o2" in NODES.keys() and "o1" in NODES.keys() and "o0" in NODES.keys():
            answer = NODES["o0"].values[0] * NODES["o1"].values[0] * NODES["o2"].values[0]
            print('Part 2:  {}'.format(str(answer)))
            raise ValueError

NODES = defaultdict(Node)

def get_data():
    from os import path

    data = []

    with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
        for line in f:
            data.append(line.strip().split())
    data.sort()
    return data

def populate_nodes(data):
    for line in data:
        if line[0] == "bot":
            node = "b" + line[1]
            low = line[5][0] + line[6]
            high = line[10][0] + line[11]
            NODES[node] = Node(node, low, high)
        else:
            value = int(line[1])
            node = "b" + line[5]
            NODES[node].add_value(value)

def part1(data):
    populate_nodes(data)

data = get_data()
part1(data)
