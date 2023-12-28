input = []
the_path = []


def get_input():
    from os import path

    with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
        for i, line in enumerate(f):
            line = line.strip()
            line = [c for c in line]
            line2 = [" " for i in line]
            if "S" in line:
                start_location = (line.index("S"), i)
            input.append(line)
            the_path.append(line2)
    return start_location


def find_next_loc(current_pos, last_pos):
    x = current_pos[0]
    y = current_pos[1]

    last_x = last_pos[0]
    last_y = last_pos[1]

    current_symbol = input[y][x]

    if current_symbol == "|":
        return (x, y + (y - last_y))
    elif current_symbol == "-":
        return (x + (x - last_x), y)
    elif current_symbol == "F":
        if x < last_x:
            return (x, y + 1)
        else:
            return (x + 1, y)
    elif current_symbol == "7":
        if x > last_x:
            return (x, y + 1)
        else:
            return (x - 1, y)
    elif current_symbol == "J":
        if x > last_x:
            return (x, y - 1)
        else:
            return (x - 1, y)
    elif current_symbol == "L":
        if x < last_x:
            return (x, y - 1)
        else:
            return (x + 1, y)


def part1(start_location):
    moves = 1

    x = start_location[0]
    y = start_location[1]

    if input[y][x + 1] in ["-", "J", "7"]:
        next_move = (x + 1, y)
    elif input[y][x - 1] in ["-", "L", "F"]:
        next_move = [x - 1, y]
    elif input[y + 1][x] in ["|", "F", "7"]:
        next_move = (y + 1, x)
    else:
        next_move = (y - 1, x)

    current_pos = (x, y)
    while input[next_move[1]][next_move[0]] != "S":
        last_pos = current_pos
        current_pos = next_move
        the_path[current_pos[1]][current_pos[0]
                                 ] = input[current_pos[1]][current_pos[0]]
        next_move = find_next_loc(current_pos, last_pos)
        moves += 1
    print('Part 1:  {}'.format(str(moves // 2)))


def part2():
    total = 0
    for i, line in enumerate(the_path):
        for j in range(len(line)):
            if line[j] == " ":
                invs = 0
                for k in range(j):
                    invs += line[k] in {"J", "L", "|"}
                if invs % 2 == 1:
                    total += 1
    print('Part 2:  {}'.format(str(total)))


start_location = get_input()
part1(start_location)
part2()
