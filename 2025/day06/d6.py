import numpy as np

def get_data():
    from os import path

    data = []

    with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
        for line in f:
            line = line.strip()
            line = line.split()
            data.append(line)
    return np.array(data)

def add(problem):
    answer = 0
    for i in range(len(problem) - 1):
        answer += int(problem[i])
    return answer

def multiply(problem):
    answer = 1
    for i in range(len(problem) - 1):
        answer *= int(problem[i])
    return answer

def special_math(problem):
    new_problem = []
    
    for c in range(len(problem[0])):
        c_num = ""
        for r in range(len(problem) - 1):
            c_num += problem[r][c]
        new_problem.append(c_num.strip())
    new_problem.append("")
    
    if problem[-1] == "+":
        return add(new_problem)
    else:
        return multiply(new_problem)

def pad_numbers(problem):
    max_length = len(max(problem, key=len))
    update = []
    for i in problem[:-1]:
        t = ""
        for j in range(max_length - len(i)):
            t = t + " "
        t = t + i
        update.append(t)
    update.append(str(problem[-1]))
    return np.array(update)

def part1(data):
    answer = 0
    
    for c in range(len(data[0])):
        problem = data[:,c]
        if problem[-1] == "+":
            answer += add(problem)
        else:
            answer += multiply(problem)
            
    print('Part 1:  {}'.format(str(answer)))
        

def part2(data):
    answer = 0
    
    for c in range(len(data[0])):
        problem = data[:,c]
        problem = pad_numbers(problem)
        answer += special_math(problem)
    # print('Part 2:  {}'.format(str(answer)))

data = get_data()
# part1(data)
part2(data)