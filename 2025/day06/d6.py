import numpy as np

def get_data():
    from os import path
    
    problems = []

    with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
        data = f.read()
        data = data.split("\n")
        
        # Find the true break between columns
        while len(data[0]) > 0:
            tmp = []
            max_end = 0
            for r in range(len(data)-1):
                num_found = False
                for i, c in enumerate(data[r]):
                    if c != " ":
                        num_found = True
                    if (c == " " or i == (len(data[r])-1)) and num_found:
                        if c == " ":
                            max_end = max(max_end, i)
                        else:
                            max_end = max(max_end, i + 1)
                        break
            # Extract the number and true spacing for each row
            for r in range(len(data)-1):
                tmp.append(data[r][: max_end])
                data[r] = data[r][max_end + 1:]
            # Add in function symbol
            tmp.append(data[len(data) - 1][: max_end])
            data[len(data) - 1] = data[len(data) - 1][max_end + 1 :]
            problems.append(tmp)
        return problems
        
        print(data)
    #     for line in f:
    #         line = line.strip()
    #         line = line.split()
    #         data.append(line)
    # return np.array(data)

def add(problem):
    answer = 0
    for i in range(len(problem) - 1):
        try:
            answer += int(problem[i])
        except ValueError:
            continue
    return answer

def multiply(problem):
    answer = 1
    for i in range(len(problem) - 1):
        try:
            answer *= int(problem[i])
        except ValueError:
            continue
    return answer

# def special_math(problem):
#     new_problem = []
    
#     for c in range(len(problem[0])):
#         c_num = ""
#         for r in range(len(problem) - 1):
#             c_num += problem[r][c]
#         new_problem.append(c_num.strip())
#     new_problem.append("")
    
#     if problem[-1] == "+":
#         return add(new_problem)
#     else:
#         return multiply(new_problem)

# def pad_numbers(problem):
#     max_length = len(max(problem, key=len))
#     update = []
#     for i in problem[:-1]:
#         t = ""
#         for j in range(max_length - len(i)):
#             t = t + " "
#         t = t + i
#         update.append(t)
#     update.append(str(problem[-1]))
#     return np.array(update)

def part1(data):
    answer = 0
    
    for p in data:
        if p[-1].strip() == "+":
            answer += add(p)
        else:
            answer += multiply(p)
            
    print('Part 1:  {}'.format(str(answer)))
        

def part2(data):
    answer = 0
    
    for r in data:
        tmp = [""] * (len(r))
        for j in range(len(r[0])):
            for i in range(len(r) - 1):
                tmp[j] += r[i][j: j+1]
        if r[-1].strip() == "+":
            answer += add(tmp)
        else:
            answer += multiply(tmp)
    print('Part 2:  {}'.format(str(answer)))

data = get_data()
part1(data)
part2(data)