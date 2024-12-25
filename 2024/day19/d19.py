from collections import defaultdict
from functools import cache


def get_data():
    from os import path
    with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
        lines = f.read()
        lines = lines.split("\n\n")
        towels = lines[1].split("\n")
        patterns = lines[0].split(", ")
    return patterns, towels

@cache
def deconstruct(patterns, towel):
    if len(towel) == 0:
        return True
    for pattern in patterns:
        if towel.startswith(pattern):
            if deconstruct(patterns, towel[len(pattern):]):
                return True
    return False

@cache
def reconstruct(patterns, towel):
    found = 0
    
    if len(towel) == 0:
        found += 1
        return found
    for pattern in patterns:
        if towel.startswith(pattern):
            found += reconstruct(patterns, towel[len(pattern):])
    return found
                
        
def part1(patterns, towels):
    answer = 0
    
    for towel in towels:
        if deconstruct(patterns, towel):
            answer += 1
    print('Part 1:  {}'.format(str(answer)))

def part2(patterns, towels):
    answer = 0
    
    for towel in towels:
        answer +=  reconstruct(patterns, towel)
    print('Part 2:  {}'.format(str(answer)))

patterns, towels = get_data()
patterns = frozenset(patterns)
# part1(patterns, towels)
part2(patterns, towels)
