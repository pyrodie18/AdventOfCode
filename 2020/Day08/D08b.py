

with open('./Day08/D08_Input.txt') as f:
    lines = [line.rstrip() for line in f]
    instructions = []

for line in lines:
    line = line.split()
    instructions.append((line[0], int(line[1])))

for i in range(len(lines)):
    used_instructions = []
    accumulator = 0
    position = 0
    if instructions[i][0] == "acc":
        continue
    else:
        original = instructions[i]
        if original[0] == "nop":
            instructions[i] = ("jmp", original[1])
        else:
            instructions[i] = ("nop", original[1])

    while True:
        if position in used_instructions:
            break
        else:
            used_instructions.append(position)
        try:
            instruction = instructions[position]
            if instruction[0] == "nop":
                position += 1
            elif instruction[0] == "acc":
                accumulator += instruction[1]
                position += 1
            else:
                position += instruction[1]
        except:
            print(accumulator)
            exit()
    instructions[i] = original
