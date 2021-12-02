from collections import defaultdict

with open('./Day06/D06_Input.txt') as f:
    lines = [line.rstrip() for line in f]

groups = []
group_size = 0
total = 0

def get_total (answers, group_size):
    total = 0
    for question in answers.keys():
        if answers[question] == group_size:
            total += 1
    return total

answers = defaultdict(int)
for line in lines:
    if len(line) > 0:
        group_size += 1
        for i in line:
            answers[i] += 1
    else:
        total += get_total(answers, group_size)
        answers = defaultdict(int)
        group_size = 0
total += get_total(answers, group_size)

print(total)