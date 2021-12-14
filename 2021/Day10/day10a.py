import os

open_char = ['(', '[', '{', '<']
close_char = [')', ']', '}', '>']
close_points = [3, 57, 1197, 25137]
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


with open(os.path.join(os.path.dirname(__file__), 'input.txt'), "r") as f:
    for line in f:
        line = line.strip()
        tmp = []
        tmp[:0] = line
        points += check_line(tmp)

print(points)