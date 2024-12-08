def get_data():
    from os import path

    data = []

    with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
        for line in f:
            line = line.strip().split(":")
            line[1] = line[1].split()
            data.append(line)
    return data

def calculate (current_value, remaining_values, oper, goal, concatinate = False):
    if current_value > goal:
        return False
    if not remaining_values and current_value == goal:
        return True
    elif not remaining_values:
        return False
    else:
        if oper == '*':
            current_value = current_value * int(remaining_values[0])
        elif oper == '+':
            current_value = current_value + int(remaining_values[0])
        elif oper == "|":
            current_value = int(str(current_value) + str(remaining_values[0]))
        
        if concatinate:
            return (calculate(current_value, remaining_values[1:], '*', goal, True) or
                    calculate(current_value, remaining_values[1:], '+', goal, True) or
                    calculate(current_value, remaining_values[1:], '|', goal, True))
        else:
            return ((calculate(current_value, remaining_values[1:], '*', goal) or
                    calculate(current_value, remaining_values[1:], '+', goal)))

def part1(data):
    answer = 0
    
    for line in data:
        goal = int(line[0])
        current_value = int(line[1][0])
        remaining_values = line[1][1:]
        
        if ((calculate(current_value, remaining_values, "+", goal)) or
            (calculate(current_value, remaining_values, "*", goal))):
            print(goal)
            answer += goal
        
    print('Part 1:  {}'.format(str(answer)))

def part2(data):
    answer = 0
    
    for line in data:
        goal = int(line[0])
        current_value = int(line[1][0])
        remaining_values = line[1][1:]
        
        if ((calculate(current_value, remaining_values, "+", goal, True)) or
            (calculate(current_value, remaining_values, "*", goal, True)) or
            (calculate(current_value, remaining_values, "|", goal, True))):
            print(goal)
            answer += goal
        
    print('Part 2:  {}'.format(str(answer)))

data = get_data()
# part1(data)
part2(data)