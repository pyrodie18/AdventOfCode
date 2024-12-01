import sys
sys.path.append('../2019')

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
    result = computer.run()
    
    answer = result[0]
    print('Part 1:  {}'.format(str(answer)))
    print(result)

def part2(data):
    for n in range(100):
        for v in range(100):
            computer = OptCode(data)
            computer.set_value(1, n)
            computer.set_value(2, v)
            result = computer.run()
            if result[0] == 19690720:
                answer = 100 * n * v
                print('Part 2:  {}'.format(str(answer)))
                raise SystemExit(0)

data = get_data()
part1(data[0])
part2(data[0])

