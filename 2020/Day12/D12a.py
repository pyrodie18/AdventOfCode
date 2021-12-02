with open('./Day12/D12_Input.txt') as f:
    lines = [line.rstrip() for line in f]

vertical = 0
horizontal = 0
directions = ('east', 'south', 'west', 'north')
direction_value = 0

def get_direction(direction_value, turn, degrees):
    num_of_turns = degrees // 90
    if turn == "L":
        num_of_turns = num_of_turns * -1
    return ((direction_value + num_of_turns) % 4)

def get_move(direction_value, distance):
    if direction_value == 1 or direction_value == 2:
        distance = distance * -1
    if direction_value == 0 or direction_value == 2:
        return (0, distance)
    else:
        return (distance,0)

for line in lines:
    move = line[0]
    distance = int(line[1:])

    if move == "N":
        vertical += distance
    elif move == "S":
        vertical += (-1 * distance)
    elif move == "W":
        horizontal += (-1 * distance)
    elif move == "E":
        horizontal += distance
    elif move == "L" or move == "R":
        direction_value = get_direction(direction_value, move, distance)
    else:
        move = get_move(direction_value, distance)
        vertical += move[0]
        horizontal += move[1]

print(abs(vertical) + abs(horizontal))
