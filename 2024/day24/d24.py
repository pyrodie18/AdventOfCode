from collections import defaultdict

class Gate():
    def __init__(self, my_name=None, input_a=None, input_b=None, operation=None, initizer=False):
        self.my_name = my_name
        self.operation = operation
        self.inputs = {
            input_a: None,
            input_b: None
        }
        self.outputs = []
        self.output_signal = None
        if my_name is None:
            self.initizer = True
        else:
            self.initizer = initizer
    
    def recieve_input(self, input_name, signal):
        if not self.initizer:
            self.inputs[input_name] = signal

            ready = True
            for k in self.inputs.keys():
                if self.inputs[k] is None:
                    ready = False
            if ready:
                self.send_output()
        else:
            self.my_name = input_name
            self.send_output(directed_output=signal)

    def add_output(self, output_name):
        self.outputs.append(output_name)
        
    def send_output(self, directed_output=None):
        if directed_output is None:
            my_inputs = list(self.inputs.keys())
            
            if self.operation == "OR":
                output = self.inputs[my_inputs[0]] | self.inputs[my_inputs[1]]
            elif self.operation == "XOR":
                output = self.inputs[my_inputs[0]] ^ self.inputs[my_inputs[1]]
            elif self.operation == "AND":
                output = self.inputs[my_inputs[0]] & self.inputs[my_inputs[1]]
        else:
            output = directed_output
        
        self.output_signal = output
                
        for dest in self.outputs:
            GATES[dest].recieve_input(self.my_name, int(output))
            
    def get_output(self):
        return self.output_signal
        
GATES = defaultdict(Gate)

def get_data():
    from os import path

    data = []
    inits = []

    with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
        lines = f.read()
        lines = lines.split("\n\n")
        lines[0] = lines[0].split("\n")
        
        # Inits
        for line in lines[0]:
            line = line.split()
            inits.append((line[0][:-1], int(line[1])))
        
        # Connections 
        lines[1] = lines[1].split("\n")
        for line in lines[1]:
            line = line.split()
            data.append((line[0], line[1], line[2], line[4]))

    return data, inits
  

def part1(data, inits):
    answer = ""
    
    # Create all items that get an output
    for line in data:
        GATES[line[3]] = Gate(line[3], line[0], line[2], line[1])
    
    # Add outputs to all nodes
    for line in data:
        GATES[line[0]].add_output(line[3])
        GATES[line[2]].add_output(line[3])
        
    for line in inits:
        GATES[line[0]].recieve_input(line[0], line[1])
        
    output_nodes = [i for i in GATES.keys() if i[0] == "z"]
    output_nodes = sorted(output_nodes, reverse=True)
    for i in output_nodes:
        answer += str(GATES[i].get_output())
        
    print('Part 1:  {}'.format(str(int(answer, 2))))

def part2(data):
    answer = None
    # print('Part 2:  {}'.format(str(answer)))

data, inits = get_data()
part1(data, inits)
# part2(data)