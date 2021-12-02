with open('./Day12/D12_Input.txt') as f:
    lines = [line.rstrip() for line in f]

ship_vertical = 0
ship_horizontal = 0
waypoint_vertical = 1
waypoint_horizontal = 10
directions = ('east', 'south', 'west', 'north')
direction_value = 0

def get_new_waypoint(waypoint_horizontal, waypoint_vertical, direction, degrees):
    num_of_turns = degrees // 90
    corrdinates = [waypoint_horizontal, waypoint_vertical]
    if direction == "L":
        for i in range(num_of_turns):
            corrdinates = [corrdinates[1] * -1, corrdinates[0]]
    else:
        for i in range(num_of_turns):
            corrdinates = [corrdinates[1], corrdinates[0] * -1]
    return corrdinates

for line in lines:
    move = line[0]
    distance = int(line[1:])

    if move == "N":
        waypoint_vertical += distance
    elif move == "S":
        waypoint_vertical += (-1 * distance)
    elif move == "W":
        waypoint_horizontal += (-1 * distance)
    elif move == "E":
        waypoint_horizontal += distance
    elif move == "L" or move == "R":
        temp_waypoint = get_new_waypoint(waypoint_horizontal, waypoint_vertical, move, distance)
        waypoint_horizontal = temp_waypoint[0]
        waypoint_vertical = temp_waypoint[1]
    else:
        ship_vertical += (waypoint_vertical * distance)
        ship_horizontal += (waypoint_horizontal * distance)

print(abs(ship_vertical) + abs(ship_horizontal))
