def get_data():
    from os import path

    data = []

    with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
        for line in f:
            data.append(line.strip().split())
    return data

def run(data, register):
    ins = 0
   
    while ins < len(data):
        if data[ins][0] == "cpy":
            #if its an integer
            if data[ins][1].isnumeric():
                register[data[ins][2]] = int(data[ins][1])
            else:
                register[data[ins][2]] = register[data[ins][1]]
            ins += 1
        elif data[ins][0] == "jnz":
            if data[ins][1].isnumeric():
                if int(data[ins][1]):
                    ins += int(data[ins][2])
            elif register[data[ins][1]] != 0:
                ins += int(data[ins][2])
            else:
                ins += 1
        elif data[ins][0] == "inc":
            register[data[ins][1]] += 1
            ins += 1
        else:
            register[data[ins][1]] -= 1
            ins += 1
        
    return register

def part1(data):
    register = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0
    }
    register = run(data, register)
    print('Part 1:  {}'.format(str(register['a'])))

def part2(data):
    register = {
        "a": 0,
        "b": 0,
        "c": 1,
        "d": 0
    }
    register = run(data, register)
    print('Part 2:  {}'.format(str(register['a'])))

data = get_data()
part1(data)
part2(data)