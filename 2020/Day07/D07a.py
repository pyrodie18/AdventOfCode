with open('./Day07/D07_Input.txt') as f:
    lines = [line.rstrip() for line in f]

rules = {}
current_rule = {}
total_bags = 0

def get_inside_bags(rules, current_bag):
    gold_bag_found = False
    inside_bags = rules[current_bag].keys()
    if 'shiny_gold' in inside_bags:
        gold_bag_found = True
    else:
        for bag in inside_bags:
            if get_inside_bags(rules, bag):
                gold_bag_found = True
                break
    return gold_bag_found


for line in lines:
    line = line.split()
    inside_bags = (len(line) - 4) // 4
    for bag in range(1, inside_bags + 1):
        current_rule[line[(bag * 4) + 1] + "_" + line[(bag * 4) + 2]] = line[(bag * 4)]
    rules[line[0] + "_" + line[1]] = current_rule
    current_rule = {}

for color in rules.keys():
    if get_inside_bags(rules, color):
        total_bags += 1

print(total_bags)