from random import shuffle
import os

transforms = []
with open(os.path.join(os.path.dirname(__file__), "D19_Input.txt"), "r") as fd:
    lines = [line.strip() for line in fd]
    for line in lines:
        if "=>" in line:
            frm, _, to = line.split()
            transforms.append((frm, to))
        else:
            molecule = line

count = 0
shuffles = 0

current_molecule = molecule
while len(current_molecule) > 1:
    start = current_molecule
    for frm, to in transforms:
        while to in current_molecule:
            count += current_molecule.count(to)
            current_molecule = current_molecule.replace(to, frm)

    if start == current_molecule:
        shuffle(transforms)
        current_molecule = molecule
        count = 0
        shuffles += 1

print("{} transforms after {} shuffles".format(count, shuffles))
