def get_data():
    from os import path

    data = []

    with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
        for line in f:
            line = line.strip()
            ranges = line.split(",")
            for i in ranges:
                i = i.split("-")
                data.append((int(i[0]), int(i[1])))
    return data

def find_valid(ids):
    total = 0
    for i in range (ids[0], ids[1] + 1):
        i = str(i)
        size = len(i)
        if size % 2 != 0:
            continue
        if i[0:int(size / 2)] == i[int(size / 2):]:
            total += int(i)
    return total

def find_valid2(ids):
    total = 0
    for i in range (ids[0], ids[1] + 1):
        i = str(i)
        size = len(i)
        for j in range (int(size/2),0, -1):
            found = True
            if size % j != 0:
                continue
            pattern = i[:j]
            for k in range(j, size, j):
                if pattern != i[k:k+j]:
                    found = False
                    break
            if found:
                total += int(i)
                break
    return total

def part1(data):
    answer = 0
    for ids in data:
        answer += find_valid(ids)
    print('Part 1:  {}'.format(str(answer)))

def part2(data):
    answer = 0
    for ids in data:
        answer += find_valid2(ids)
    print('Part 2:  {}'.format(str(answer)))

data = get_data()
part1(data)
part2(data)