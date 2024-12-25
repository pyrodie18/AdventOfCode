def get_data():
    from os import path

    data = {}

    with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
        for line in f:
            line = line.strip().split()
            if len(line) > 0:
                if line[0] == "Register":
                    data[line[1][0]] = int(line[2])
                elif line[0] == "Program:":
                    data["Program"] = [int(i) for i in line[1].split(",")]
    return data

def adv(program, pointer, registers):
    a, b, c = registers
    
    combo = program[pointer + 1]
    
    ans = a / (2**decode_combo(combo, registers))
    ans = str(ans).split(".")
    return int(ans[0]), b, c

def bxl(program, pointer, registers):
    a, b, c = registers
    literal = program[pointer + 1]
    
    ans = literal ^ b
    return a, ans, c

def bst(program, pointer, registers):
    a, b, c = registers
    combo = decode_combo(program[pointer + 1],registers)
    
    ans = combo % 8
    return a, ans, c

def bxc(program, pointer, registers):
    a, b, c = registers
    
    ans = c ^ b
    return a, ans, c

def out(program, pointer, registers):
    combo = program[pointer + 1]
    
    ans = (decode_combo(combo, registers)) % 8
    return ans

def bdv(program, pointer, registers):
    a, b, c = registers
    
    combo = program[pointer + 1]
    
    ans = a / (2**decode_combo(combo, registers))
    ans = str(ans).split(".")
    return a, int(ans[0]), c

def cdv(program, pointer, registers):
    a, b, c = registers
    
    combo = program[pointer + 1]
    
    ans = a / (2**decode_combo(combo, registers))
    ans = str(ans).split(".")
    return a, b, int(ans[0])
    
def decode_combo(value, registers):
    a, b, c = registers
    
    if value <= 3:
        return value
    elif value == 4:
        return a
    elif value == 5:
        return b
    elif value == 6:
        return c
    else:
        raise ValueError

def run(data, check = False):
    answer = []
    a = data["A"]
    b = data["B"]
    c = data["C"]
    
    program = data["Program"]
    
    i = 0
    while i < len(program):
        instruction = program[i]
        
        if instruction == 0:
            a, b, c = adv(program, i, (a, b, c))
            i += 2
        elif instruction == 1:
            a, b, c = bxl(program, i, (a, b, c))
            i += 2
        elif instruction == 2:
            a, b, c = bst(program, i, (a, b, c))
            i += 2
        elif instruction == 3:
            if a != 0:
                i = program[i + 1]
            else:
                i += 2
        elif instruction == 4:
            a, b, c = bxc(program, i, (a, b, c))
            i += 2
        elif instruction == 5:
            answer.append(out(program, i, (a, b, c)))
            if check:
                for j in range(len(answer)):
                    if answer[j] != program[j]:
                        return False
            i += 2
        elif instruction == 6:
            a, b, c = bdv(program, i, (a, b, c))
            i += 2
        elif instruction == 7:
            a, b, c = cdv(program, i, (a, b, c))
            i += 2
    return answer

def part1(data):
    results = run(data)
    answer = ""
    for i in results:
        answer += str(i)
    
    print('Part 1:  {}'.format(str(results)))

def part2(data):
    i = 8208334368 # Last running iteration
    found = False
    
    while not found:
        data["A"] = i
        result = run(data, True)
        if result == data["Program"]:
            found = True
            print('Part 2:  {}'.format(str(i)))
            break
        i += 1
        
    # answer = None
    # print('Part 2:  {}'.format(str(answer)))

data = get_data()
# part1(data)
part2(data)