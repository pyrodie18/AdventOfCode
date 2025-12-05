def get_data():
    from os import path
    ingredients = []
    fresh_ranges = []
    

    with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
        ingredients_active = False
        for line in f:
            line = line.strip()
            if len(line) == 0:
                ingredients_active = True
                continue
            elif ingredients_active:
                ingredients.append(int(line))
            else:
                line = line.split("-")
                fresh_ranges.append([int(line[0]), int(line[1])])
    return ingredients, fresh_ranges

def consolidate_ranges(ranges):
    ranges.sort()
    opt_ranges = []
    opt_ranges.append(ranges[0])
    
    for i in range(1, len(ranges)):
        last = opt_ranges[-1]
        curr = ranges[i]
        
        if curr[0] <= last[1]:
            last[1] = max(last[1], curr[1])
        else:
            opt_ranges.append(curr)
            
    return opt_ranges

def check_freshness(ingredent, fresh_ranges):
    for r in fresh_ranges:
        if r[0] <= ingredent <= r[1]:
            return True
    return False
        

def part1(ingredients, fresh_ranges):
    answer = 0
    for i in ingredients:
        if check_freshness(i, fresh_ranges):
            answer += 1
            
    print('Part 1:  {}'.format(str(answer)))

def part2(fresh_ranges):
    answer = 0
    
    for r in fresh_ranges:
        answer += ((r[1] - r[0]) + 1)
    print('Part 2:  {}'.format(str(answer)))

ingredients, fresh_ranges  = get_data()
fresh_ranges = consolidate_ranges(fresh_ranges)
# part1(ingredients, fresh_ranges)
part2(fresh_ranges)