def get_input():
    from os import path

    input = []

    with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
        for line in f:
            input = line.split(', ')
    return input


def get_direction(current_direction, move):
    if move == "L":
        direction = (current_direction - 90) % 360
    else:
        direction = (current_direction + 90) % 360
    return direction


def get_distance(x, y):
    return abs(x) + abs(y)


def part1(input):
    x = 0
    y = 0
    facing = 0
    locations = []
    start_pos = (0, 0)

    for instruction in input:
        facing = get_direction(facing, instruction[0])

        if facing > 90:
            distance = int(instruction[1:]) * -1
        else:
            distance = int(instruction[1:])

        if facing == 90 or facing == 270:
            x += distance
        else:
            y += distance

        locations.append((start_pos, (x, y)))
        start_pos = (x, y)

    print("Part 1: {}".format(get_distance(x, y)))
    return locations


def find_intersection(locations):
    from shapely import LineString
    for i, current_segment in enumerate(locations):
        if i >= 2:
            a = LineString([(current_segment[0][0], current_segment[0][1]),
                            (current_segment[1][0], current_segment[1][1])])
            for j in range(0, i - 1):
                b = LineString([(locations[j][0][0], locations[j][0][1]),
                                (locations[j][1][0], locations[j][1][1])])
                intersect = a.intersection(b)
                if intersect.type == "Point":
                    return intersect


def part2(locations):
    intersect = find_intersection(locations)
    print("Part 2: {}".format(get_distance(int(intersect.x), int(intersect.y))))


input = get_input()
locations = part1(input)
part2(locations)
