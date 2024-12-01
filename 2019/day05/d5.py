from Optcode import OptCode

def get_data():
    from os import path

    data = []

    with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
        for line in f:
            data.append(line.strip())
    return data    

def part1(instructions):
    
    computer = OptCode(instructions)
    computer.run([1])
    
def part2(instructions):
    computer = OptCode(instructions)
    computer.run([5])

data = get_data()
part1(data[0])
part2(data[0])

