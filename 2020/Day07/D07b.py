with open('./Day07/D07_Input.txt') as f:
    lines = [line.rstrip() for line in f]

rules = {}
current_rule = {}
total_bags = 0

def get_inside_bags(rules, current_bag):
    additional_bags = 0
    inside_bags = rules[current_bag].keys()
    for bag in inside_bags:
        additional_bags += int(rules[current_bag][bag])
        additional_bags += int(rules[current_bag][bag]) * get_inside_bags(rules, bag)
    return additional_bags


for line in lines:
    line = line.split()
    inside_bags = (len(line) - 4) // 4
    for bag in range(1, inside_bags + 1):
        current_rule[line[(bag * 4) + 1] + "_" + line[(bag * 4) + 2]] = line[(bag * 4)]
    rules[line[0] + "_" + line[1]] = current_rule
    current_rule = {}

for bag in rules['shiny_gold'].keys():
    total_bags += int(rules['shiny_gold'][bag])
    total_bags += int(rules['shiny_gold'][bag]) * get_inside_bags(rules, bag)

print(total_bags)