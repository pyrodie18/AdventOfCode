with open('./Day14/D14_Input.txt') as f:
    lines = [line.rstrip() for line in f]
register = {}
mask = []

def generate_addresses(mask, address):
    address = list('{0:036b}'.format(int(address)))
    variable_bits = []
    list_of_addresses = []
    temp_address = [0] * 36
    for i, bit in enumerate(mask):
        if bit == 'X':
            variable_bits.append(i)
        else:
            temp_address[i] = str(int(mask[i]) | int(address[i]))
    # Generate variations
    Xs = len(variable_bits)
    format_var = '{:0' + str(Xs) + 'b}'
    for j in range(2 ** Xs):
        for k, bit in enumerate(list(format_var.format(j))):
            temp_address[variable_bits[k]] = bit
        list_of_addresses.append(int(''.join(temp_address),2))

    return list_of_addresses



for line in lines:
    line = line.split()
    if line[0] == "mask":
        mask = list(line[2])
    else:
        current_value = list('{0:036b}'.format(int(line[2])))
        reg_num = line[0][4:-1]
        list_of_addresses = generate_addresses(mask, reg_num)
        new_value = [0] * 36
        for address in list_of_addresses:
            register[address] = int(''.join(current_value),2)

keys = register.keys()
total = 0
for key in keys:
    total += register[key]

print(total)
