

def get_input(round2=False):
    from os import path

    positions = []

    if round2:
        expansion = 1000000
    else:
        expansion = 1

    with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
        y = 0
        for line in f:
            if not "#" in line:
                y += (expansion - 1)
            else:
                for x, i in enumerate(line):
                    if i == "#":
                        positions.append((x, y))
            y += 1

        present_cols = []

        for pos in positions:
            present_cols.append(pos[0])

        for i in range(max(present_cols), 0, -1):
            if i not in present_cols:
                for j, pos in enumerate(positions):
                    if pos[0] >= i:
                        positions[j] = (pos[0] + (expansion - 1), pos[1])

    return positions


def part1():
    from itertools import combinations

    positions = get_input()

    total = 0

    for combo in combinations(positions, 2):
        rise = abs(combo[0][1] - combo[1][1])
        run = abs(combo[0][0] - combo[1][0])
        total += (rise + run)
        print("{} :  {}". format(str(combo), str(rise + run)))
    print('Part 1:  {}'.format(str(total)))


def part2():
    from itertools import combinations

    positions = get_input(True)
    total = 0

    for combo in combinations(positions, 2):
        rise = abs(combo[0][1] - combo[1][1])
        run = abs(combo[0][0] - combo[1][0])
        total += (rise + run)
        print("{} :  {}". format(str(combo), str(rise + run)))
    print('Part 2:  {}'.format(str(total)))


part1()
part2()
