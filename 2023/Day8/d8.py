def get_input():
    from os import path
    import re

    input = {}
    mappings = {}

    with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
        for line in f:
            line = line.strip()

            if line == "":
                continue
            elif "=" not in line:
                pattern = line
            else:
                line = re.sub(r'([\=\(\,\)])', "", line)
                line = line.split()
                mappings[line[0]] = (line[1], line[2])

    input = {
        "patterns": pattern,
        "mappings": mappings
    }
    return input


def find_end(start, input, part2=False):
    from itertools import cycle
    next_move = start
    moves = 0

    for c in cycle(input["patterns"]):
        if c == "L":
            next_move = input["mappings"][next_move][0]
        else:
            next_move = input["mappings"][next_move][1]
        moves += 1

        if (part2 and next_move.endswith("Z")) or next_move == "ZZZ":
            return moves


def part1(input):
    moves = find_end("AAA", input)
    print('Part 1:  {}'.format(str(moves)))


def part2(input):
    from math import lcm
    matches = []
    keys = input["mappings"].keys()
    for k in keys:
        if k.endswith("A"):
            matches.append(find_end(k, input, True))

    print('Part 2:  {}'.format(str(lcm(*matches))))


input = get_input()
part1(input)
part2(input)
