import re

r1 = re.compile('\\^\\^\\.')
r2 = re.compile('\\.\\^\\^')
r3 = re.compile('\\^\\.\\.')
r4 = re.compile('\\.\\.\\^')
regexs = [r1, r2, r3, r4]
def get_data():
    from os import path

    data = []

    with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
        for line in f:
            data.append(line.strip())
    return data

def fill_next_line(current_line):
    next_line = ["."] * len(current_line)
    for pattern in [r1, r2, r3, r4]:
        hits = re.finditer(pattern, current_line)
        for hit in hits:
            next_line[hit.start() + 1] = "^"
    next_line = "".join(next_line)    
    
    return next_line

def count_safe(current_line):
    return current_line.count('.') - 2

def part1(data):
    current_line = data[0]
    answer = current_line.count('.')
    current_line = "." + current_line + "."
    line_ct = 1
    
    while line_ct < 40:
        current_line = fill_next_line(current_line)
        answer += count_safe(current_line)
        line_ct += 1

    print('Part 1:  {}'.format(str(answer)))

def part2(data):
    current_line = data[0]
    answer = current_line.count('.')
    current_line = "." + current_line + "."
    line_ct = 1
    
    while line_ct < 400000:
        current_line = fill_next_line(current_line)
        answer += count_safe(current_line)
        line_ct += 1

    print('Part 2:  {}'.format(str(answer)))

data = get_data()
part1(data)
part2(data)