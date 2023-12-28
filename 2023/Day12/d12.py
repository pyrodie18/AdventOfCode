def get_input():
    from os import path

    input = []

    with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
        for line in f:
            line = line.strip()
            line = line.split()
            line[1] = [int(i) for i in line[1].split(',')]
            input.append(line)

    return input


def part1(input):
    import re

    for line in input:
        matches = re.findall(
            r'(?=([\?\#]{2}[\?\.]+))', line[0])
        print(matches)
    # print('Part 1:  {}'.format(str(winners)))


def part2(input):
    pass
    # print('Part 2:  {}'.format(str(winners)))


input = get_input()
part1(input)
part2(input)
