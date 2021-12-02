import json

with open('./Day18/D18_Input.txt') as f:
    lines = [line.rstrip() for line in f]

def new_math(equation):
    i = 0
    while i < (len(equation) - 2):
        if type(equation[i]) is list:
            equation[i] = new_math(equation[i])
        if type(equation[i + 2]) is list:
            equation[i + 2] = new_math(equation[i + 2])
        current_step = "".join(str(equation[i:i+3]))
        current_step = current_step.replace("[", "").replace("]", "").replace("'", "").replace(",", "")


        equation[i+2] = str(eval(current_step))
        i += 2
    return int(equation[-1])

total = 0
for line in lines:
    line = "[" + line + "]"
    line = line.replace("(", "[")
    line = line.replace(")", "]")
    line = line.replace('*', '"*"')
    line = line.replace('+', '"+"')
    line = line.replace(" ", ",")
    line = json.loads(line)
    total += new_math(line)

print(total)