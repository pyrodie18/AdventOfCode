def get_data():
    from os import path

    data = []

    with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
        for line in f:
            data.append(line.strip())
    return data

def figure_mod(pos, move, direction):
    zeros = 0
    current_pos = pos
    if direction == "L":
        for i in range(move):
            current_pos -= 1
            if current_pos == 0:
                zeros += 1
            elif current_pos < 0:
                current_pos = 99
    else:
        for i in range(move):
            current_pos += 1
            if current_pos == 100:
                zeros += 1
                current_pos = 0
    return zeros

def turn (pos, instruction, mod=False):
    direction = instruction[0]
    spaces = int(instruction[1:])
    
    if direction == "L":
        new_pos = (pos - (spaces % 100))
        if new_pos < 0:
            new_pos = 100 + new_pos
    else:
        new_pos = pos + spaces
        new_pos =  new_pos % 100
        
    if mod:
        return new_pos, figure_mod(pos, spaces, direction)
    else:
        return new_pos

def part1(data):
    answer = 0
    pos = 50
    
    for instruction in data:
        pos = turn(pos, instruction)
        if pos == 0:
            answer += 1
    
    print('Part 1:  {}'.format(str(answer)))

def part2(data):
    answer = 0
    pos = 50
    
    for instruction in data:
        pos, zeros = turn(pos, instruction, True)
        answer += zeros
    
    print('Part 2:  {}'.format(str(answer)))

data = get_data()
# part1(data)
part2(data)