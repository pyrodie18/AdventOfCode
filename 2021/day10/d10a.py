import os

open_char = ['(', '[', '{', '<']
close_char = [')', ']', '}', '>']
close_points = [3, 57, 1197, 25137]
complete_points = [1, 2, 3, 4]
points = 0

def check_line(line):
    i = 0
    while i <= (len(line) - 2):
        current_set = line[i: i+2]

        try:
            assert current_set[0] in open_char
            assert current_set[1] in close_char
        except:
            i += 1
            continue

        j = open_char.index(current_set[0])
        if current_set[1] == close_char[j]:
            del line[i:i+2]
            i = 0
        else:
            j = close_char.index(current_set[1])
            return close_points[j]
    return 0


def close_line(line):
    score = 0
    i = 0
    while i <= (len(line) - 1):
        current_set = line[i: i+2]

        try:
            assert current_set[0] in open_char
            assert current_set[1] in close_char
        except:
            i += 1
            continue
    
    while len(line) > 0:
        pos = open_char.index(line[-1])
        points = complete_points[pos]
        score *= 5
        score += points
        del line[-1]
    return score

incomplete_lines = []

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), "r") as f:
    for line in f:
        line = line.strip()
        tmp = []
        tmp[:0] = line
        additional_points = check_line(tmp)
        if additional_points > 0:
            points += additional_points
        else:
            incomplete_lines.append(tmp)

part2 = []
for line in incomplete_lines:
    part2.append(close_line(line))

part2.sort()


print(points)
print(part2[(len(part2)//2)])