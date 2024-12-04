import re

pattern = re.compile('mul\\((\\d{1,3},\\d{1,3})\\)')
pattern2 = r"(mul)\((\d{1,3}),(\d{1,3})\)|(do)\(\)|(don't)\(\)"

def get_data():
    from os import path

    data = []

    with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
        for line in f:
            data.append(line.strip())
    return data

def part1(data):
    answer = 0
    for line in data:
        matches = re.findall(pattern, line)
        for match in matches:
            tmp = match.split(',')
            answer += int(tmp[0]) * int(tmp[1])
    print('Part 1:  {}'.format(str(answer)))

def part2(data):
    answer = 0
    line = "".join(data)
    on = True

    hits = re.findall(pattern2, line)
    print(hits)
    for hit in hits:
        if hit[0] == "mul" and on:
            answer += int(hit[1]) * int(hit[2])
        elif hit[4] == "don't":
            on = False
        elif hit[3] == "do":
            on = True
        
    
        
    print('Part 2:  {}'.format(str(answer)))

data = get_data()
# part1(data)
part2(data)