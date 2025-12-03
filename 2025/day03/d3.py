def get_data():
    from os import path

    data = []

    with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
        for line in f:
            line = line.strip()
            # data.append(line)
            the_line = []
            for i in line:
                the_line.append(int(i))
            data.append(the_line)
    return data

def rindex(alist, value):
    return len(alist) - alist[-1::-1].index(value) -1

def reverse_sort(line):
    values = list(set(line))
    return sorted(values, reverse=True)
    # values.sort()
    # sorted_values = values[::-1]
    # return sorted_values

def find_max(line):
    sorted_values = reverse_sort(line)
    for i in sorted_values:
        for j in sorted_values:
            if line.index(i) < rindex(line, j):
                return int(f"{i}{j}")

def find_next_max(line, size):
    sorted_values = reverse_sort(line)
    length = len(line)
    for i in sorted_values:
        if length - line.index(i) >= size:
            return i, line[line.index(i) + 1:]

def find_mega_max(line):
    max_value = []
    remaining = 12
    remaining_line = line
    while remaining > 0:
        value, remaining_line = find_next_max(remaining_line, remaining)
        max_value.append(value)
        remaining -= 1
        
    return int(''.join(f"{i}" for i in max_value))

def part1(data):
    answer = 0
    for line in data:
        answer += find_max(line)
    
    print('Part 1:  {}'.format(str(answer)))

def part2(data):
    answer = 0
    for line in data:
        answer += find_mega_max(line)
        
    print('Part 2:  {}'.format(str(answer)))

data = get_data()
# part1(data)
part2(data)