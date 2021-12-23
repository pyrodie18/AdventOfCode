p1_start = 4
p1_score = 0
p2_start = 1
p2_score = 0
p1 = True

def roll_dice():
    i = 1
    while True:
        total = 0
        for j in range(3):
            total += i
            i += 1
            if i > 100:
                i = 1
        yield total

def p1_board(spaces_to_move, positions=[p1_start]):
    start_pos = positions[-1]
    for i in range(spaces_to_move):
        start_pos += 1
        if start_pos > 10:
            start_pos = 1
    positions.append(start_pos)
    return start_pos

def p2_board(spaces_to_move, positions=[p2_start]):
    start_pos = positions[-1]
    for i in range(spaces_to_move):
        start_pos += 1
        if start_pos > 10:
            start_pos = 1
    positions.append(start_pos)
    return start_pos

roll_count = 0
while True:
    for i in roll_dice():
        roll_count += 3
        if p1:
            new_position = p1_board(i)
            p1_score += new_position
            print("p1: {}".format(p1_score))
        else:
            new_position = p2_board(i)
            p2_score += new_position
            print("p2: {}".format(p2_score))
        if p1_score >= 1000:
            print(roll_count)
            print(roll_count * p2_score)
            break
        elif p2_score >= 1000:
            print(roll_count)
            print(roll_count * p1_score)
            break
        else:
            p1 = not p1
    break