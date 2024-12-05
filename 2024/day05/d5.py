from collections import defaultdict
from itertools import permutations

def get_data():
    from os import path

    rules = defaultdict(list)
    updates = []
    rule = True

    with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
        for line in f:
            line = line.strip()
            if len(line) == 0:
                rule = False
                
            if rule:
                line = line.split("|")
                rules[line[0]].append(line[1])
            else:
                line = line.split(",")
                updates.append(line)
                
    updates.pop(0)
    return rules, updates

def validate_update(rules, update):
    for page in update:
        the_rules = rules[page]
        cur_page = update.index(page)
        for rule in the_rules:
            if rule in update:
                i = update.index(rule)
                if not cur_page < i:
                    return False
    return True

def get_center(update):
    l = len(update)
    return int(update[l//2])

def correct(rules, update):
    i = 1
    while i < len(update):
        the_rules = rules[update[i]]
        for rule in the_rules:
            if rule in update:
                if i > update.index(rule):
                    tmp = update.pop(update.index(rule))
                    update.insert(i, tmp)
                    i = 1
                    break
        i += 1
    return update            
    
    



def part1(rules, updates):
    total = 0
    for update in updates:
        if validate_update(rules, update):
            total += get_center(update)
    print('Part 1:  {}'.format(str(total)))

def part2(rules, updates):
    total = 0
    for update in updates:
        if not validate_update(rules, update):
            correct_update = correct(rules, update)
            total += get_center(correct_update)
    print('Part 2:  {}'.format(str(total)))

rules, updates = get_data()
part1(rules, updates)
part2(rules, updates)
