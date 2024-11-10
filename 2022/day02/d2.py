import os

input = []
part1_score = 0
part2_score = 0
win = 6
lost = 0
tie = 3
rock = 1
paper = 2
scissor = 3
odd_logic_normal = {
    "X": {"A": lost + scissor, "B": lost + rock, "C": lost + paper},
    "Y": {"A": tie + rock, "B": tie + paper, "C": tie + scissor},
    "Z": {"A": win + paper, "B": win + scissor, "C": win + rock},
}

logic_normal = {
    "X": {"A": tie + rock, "B": lost + rock, "C": win + rock},
    "Y": {"A": win + paper, "B": tie + paper, "C": lost + paper},
    "Z": {"A": lost + scissor, "B": win + scissor, "C": tie + scissor},
}

with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as f:
    for line in f:
        input.append(line.strip().split())

for line in input:
    part1_score += logic_normal[line[1]][line[0]]
    part2_score += odd_logic_normal[line[1]][line[0]]
print(part1_score)
print(part2_score)
