with open('./Day14/D14_Input.txt') as f:
    lines = [line.rstrip() for line in f]
register = {}
mask = []


for line in lines:
    line = line.split()
    if line[0] == "mask":
        mask = list(line[2])
    else:
        current_value = list('{0:036b}'.format(int(line[2])))
        reg_num = line[0][4:-1]
        new_value = [0] * 36
        for i in range(len(mask)):
            if mask[i] == 'X':
                new_value[i] = current_value[i]
            else:
                new_value[i] = mask[i]
        register[reg_num] = int(''.join(new_value),2)

keys = register.keys()
total = 0
for key in keys:
    total += register[key]

print(total)
