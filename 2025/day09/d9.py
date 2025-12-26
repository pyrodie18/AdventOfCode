from itertools import combinations
import shapely

def get_data():
    from os import path

    data = []

    with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
        for line in f:
            line = line.strip().split(",")
            data.append((int(line[0]), int(line[1])))
            # data.append(line.strip())
    return data

def calc_area(combo):
    l = abs(combo[0][1] - combo[1][1]) + 1
    w = abs(combo[0][0] - combo[1][0]) + 1
    return l * w

def part1(data):
    answer = 0
    for c in combinations(data, 2):
        answer = max(answer, calc_area(c))
    print('Part 1:  {}'.format(str(answer)))

def part2(data):
    answer = 0
    data.append(data[0])
    S = shapely.Polygon(data)
    for c in combinations(data, 2):
        R = shapely.Polygon([c[0], (c[1][0], c[0][1]), c[1], (c[0][0], c[1][1]), c[0]])
        if shapely.within(R, S):
            answer = max(answer, calc_area(c))
    print('Part 2:  {}'.format(str(answer)))

data = get_data()
part1(data)
part2(data)