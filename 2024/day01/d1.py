def get_data():
    from os import path

    left = []
    right = []

    with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
        for line in f:
            line = line.strip().split()
            left.append(int(line[0]))
            right.append(int(line[1]))
    return left, right

def part1(left, right):
    answer = 0
    left.sort()
    right.sort()
    
    for i in range(len(left)):
        answer += abs(left[i] - right[i])
    print('Part 1:  {}'.format(str(answer)))

def part2(left, right):
    answer = 0
    for i in range(len(left)):
        found = right.count(left[i])
        answer += left[i] * found
    print('Part 2:  {}'.format(str(answer)))

left, right = get_data()
part1(left, right)
part2(left, right)