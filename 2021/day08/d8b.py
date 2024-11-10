import os

def find_numbers(wire_mapping):
    numbers = {
        0: ['a', 'b', 'c', 'e', 'f', 'g'],
        1: ['c', 'f'],
        2: ['a', 'c', 'd', 'e', 'g'],
        3: ['a', 'c', 'd', 'f', 'g'],
        4: ['b', 'c', 'd', 'f'],
        5: ['a', 'b', 'd', 'f', 'g'],
        6: ['a', 'b', 'd', 'e', 'f', 'g'],
        7: ['a', 'c', 'f'],
        8: ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
        9: ['a', 'b', 'c', 'd', 'f', 'g'],
    }

    for i in range(10):
        key = []
        for wire in numbers[i]:
            key.append(wire_mapping[wire][0])
        numbers[i] = sorted(key)

    return numbers

def find_wires(current_display):
    wires = {
        'a': ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
        'b': ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
        'c': ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
        'd': ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
        'e': ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
        'f': ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
        'g': ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    }
    patterns = current_display['patterns']

    # Get wire count
    wire_count = {
        'a': 0,
        'b': 0,
        'c': 0,
        'd': 0,
        'e': 0,
        'f': 0,
        'g': 0,
    }

    for pattern in patterns:
        for i in pattern:
            wire_count[i] += 1

    # Find b, e, f
    for i in 'abcdefg':
        search = None
        if wire_count[i] == 4:
            wires['e'] = [i]
            search = 'abcdfg'
        elif wire_count[i] == 6:
            wires['b'] = [i]
            search = 'acdefg'
        elif wire_count[i] == 9:
            wires['f'] = [i]
            search = 'abcdeg'
        if search is not None:
            for j in search:
                try:
                    wires[j].remove(i)
                except:
                    pass

    # Find 1 and c
    for pattern in patterns:
        if len(pattern) == 2:
            pattern.remove(wires['f'][0])
            wires['c'] = pattern
            for i in 'adg':
                wires[i].remove(pattern[0])
            break

    # Find 7 and a
    for pattern in patterns:
        if len(pattern) == 3:
            pattern.remove(wires['c'][0])
            pattern.remove(wires['f'][0])
            wires['a'] = pattern
            for i in 'dg':
                wires[i].remove(pattern[0])
            break

    # Find 4 and b, d
    for pattern in patterns:
        if len(pattern) == 4:
            for i in 'bcf':
                pattern.remove(wires[i][0])
            wires['d'] = [pattern[0]]
            wires['g'].remove(pattern[0])

    return wires

def get_output(display, number_mapping):
    outputs = display['outputs']
    output_number = ''
    for digit in outputs:
        for i in number_mapping.keys():
            if digit == number_mapping[i]:
                output_number += str(i)
                break
    return int(output_number)

displays = []

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), "r") as f:
    for line in f:
        line = line.split('|')
        patterns = line[0].split()
        for i, pattern in enumerate(patterns):
            patterns[i] = sorted(pattern)
        outputs = line[1].split()
        for i, output in enumerate(outputs):
            outputs[i] = sorted(output)
        displays.append({'patterns': patterns, 'outputs': outputs})

total = 0
for display in displays:
    wire_mapping = find_wires(display)
    number_mapping = find_numbers(wire_mapping)
    total += get_output(display, number_mapping)
print(total)