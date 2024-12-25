import numpy as np
from fractions import Fraction

def get_data():
    from os import path

    data = []

    with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
        content = f.read()
        content = content.split('\n\n')
    
    for group in content:
        staged = {}
        lines = group.split('\n')
        for line in lines:
            line = line.replace(",","")
            line = line.split()
            if line[0] == "Button":
                staged[line[1][0]] = (int(line[2][2:]), (int(line[3][2:])))
            else:
                staged["Prize"] = (int(line[1][2:]), int(line[2][2:]))
        data.append(staged)

    return data

def find_cost(machine, modify = False):    
    AX, AY = machine["A"]
    BX, BY = machine["B"]
    PX, PY = machine["Prize"]
    
    if modify:
        PX += 10000000000000
        PY += 10000000000000
    
    a = Fraction(-(BY * PX - BX * PY),(AY * BX - AX * BY))
    b = Fraction((AY * PX - AX * PY),(AY * BX - AX * BY))
    if a.denominator != 1 or b.denominator != 1:
        return 0
    elif not modify and (a.denominator > 100 or b.denominator > 100):
        return 0
    else:
        return ((3 * a) + b)

def part1(machines):
    answer = 0
    
    for machine in machines:
        answer += find_cost(machine)
        
    print('Part 1:  {}'.format(str(answer)))

def part2(machines):
    answer = 0
    
    for machine in machines:
        answer += find_cost(machine, True)
        
    print('Part 2:  {}'.format(str(answer)))

data = get_data()
part1(data)
part2(data)