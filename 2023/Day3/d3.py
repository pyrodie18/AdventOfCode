def get_input():
    from os import path
    import re

    input = []

    with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
        y = 0
        special_pos = []
        gear_pos = []
        for line in f:
            line = line.strip()
            line_len = len(line)

            row = [0] * line_len
            integers = re.finditer(r'(\d+)', line)
            for number in integers:
                the_int = int(number.group())
                for i in range(number.start(), number.end()):
                    row[i] = the_int
            specials = re.finditer(r'([^A-Za-z0-9\.])', line)
            for special in specials:
                special_pos.append((special.start(), y))
            gears = re.finditer(r'\*', line)
            for gear in gears:
                gear_pos.append((gear.start(), y))
            y += 1

            input.append(row)
    return input, special_pos, gear_pos


def find_adjacent(input, position):
    values = []
    max_y = len(input)
    max_x = len(input[0])
    y = position[1]
    x = position[0]

    for i in range(y - 1, y + 2):
        if i < 0 or i >= len(input):
            continue
        start = x - 1 if x - 1 >= 0 else 0
        end = x + 2 if x + 2 <= max_x else max_x
        values += list(set(input[i][start:end]))
    return values


def part1(input, special_pos):
    total = 0
    for special in special_pos:
        total += sum(find_adjacent(input, special))
    print("Part 1:  {}".format(str(total)))


def part2(input, gear_pos):
    total = 0
    for gear in gear_pos:
        ratios = list(set(find_adjacent(input, gear)))
        if 0 in ratios:
            ratios.remove(0)
        if len(ratios) == 2:
            total += (ratios[0] * ratios[1])
    print("Part 2:  {}".format(str(total)))


input, special_pos, gear_pos = get_input()
part1(input, special_pos)
part2(input, gear_pos)
