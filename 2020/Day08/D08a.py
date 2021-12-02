used_instructions = []
accumulator = 0
instructions = []
position = 0

with open('./Day08/D08_Input.txt') as f:
    lines = [line.rstrip() for line in f]

for line in lines:
    line = line.split()
    instructions.append((line[0], int(line[1])))

while True:
    if position in used_instructions:
        break
    else:
        used_instructions.append(position)
    instruction = instructions[position]
    if instruction[0] == "nop":
        position += 1
    elif instruction[0] == "acc":
        accumulator += instruction[1]
        position += 1
    else:
        position += instruction[1]

print(accumulator)