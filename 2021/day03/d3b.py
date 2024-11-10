import os
o2 = []
co2 = []

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), "r") as f:
    for line in f:
        o2.append(line.strip())
        co2.append(line.strip())



def get_code(input, high):
    position = 0
    while len(input) > 1:
        total_lines = 0
        on = 0
        for line in input:
            if line[position] == '1':
                on += 1
            total_lines += 1
        if (total_lines / 2) <= on:
            if high:
                bit = '1'
            else:
                bit = '0'
        else:
            if high:
                bit = '0'
            else:
                bit = '1'

        lines_to_del = []

        for line in input:
            if line[position] != bit:
                lines_to_del.append(line)

        for line in lines_to_del:
            input.remove(line)
        position += 1
    return input[0]

print(int(get_code(o2, True),2) * int(get_code(co2, False), 2) )

    

