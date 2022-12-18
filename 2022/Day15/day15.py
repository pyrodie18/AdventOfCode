def get_input():
    from os import path

    input = []

    with open(path.join(path.dirname(__file__), "input.txt"), "r") as f:
        for line in f:
            tmp = line.strip().split()
            x1 = int(tmp[2][2:-1])
            y1 = int(tmp[3][2:-1])
            x2 = int(tmp[8][2:-1])
            y2 = int(tmp[9][2:])
            distance = abs(x1 - x2) + abs(y1 - y2)
            input.append([[x1, y1], [x2, y2], distance])

    return input


def part1(input):
    marked_grids = []
    found_beacons = []
    the_line = 2000000

    for line in input:
        if line[1][1] == the_line:
            found_beacons.append(line[1][0])
        if abs(line[0][1] - the_line) > line[2]:
            continue
        left_over = line[2] - (abs(line[0][1] - the_line))
        for i in range(left_over + 1):
            marked_grids.append(line[0][0] + i)
            marked_grids.append(line[0][0] - i)
    beacons = set(found_beacons)
    empty = set(marked_grids)
    the_answer = len(empty.difference(beacons))
    print("Part 1:  " + str(the_answer))


def set_hor_limits(line, i, limit):
    min_h = line[0][0] - (line[2] - i)
    min_h = min_h if min_h >= 0 else 0
    max_h = line[0][0] + (line[2] + 1) - i
    max_h = max_h if max_h <= limit else limit + 1

    return min_h, max_h


def part2(input):
    import numpy as np

    limit = 4000000
    grid = np.zeros((limit + 1, limit + 1), dtype=bool)

    for line in input:
        # Mark the sensor itself
        if line[0][0] <= limit and line[0][1] <= limit:
            grid[line[0][0]][line[0][1]] = True

        for i in range(line[2] + 1):
            min_h, max_h = set_hor_limits(line, i, limit)
            if line[0][1] - i >= 0:
                grid[line[0][1] - i, min_h:max_h] = True
            if line[0][1] + i <= limit:
                grid[line[0][1] + i, min_h:max_h] = True
    print("Part 2:  " + str(np.where(grid == False)))


def part2b(input):
    from shapely import Polygon, geometry
    from shapely.ops import unary_union

    limit = 4000000
    covered = []

    for line in input:
        covered.append(
            Polygon(
                [
                    (line[0][0] + line[2], line[0][1]),
                    (line[0][0], line[0][1] + line[2]),
                    (line[0][0] - line[2], line[0][1]),
                    (line[0][0], line[0][1] - line[2]),
                ]
            )
        )

    search_area = geometry.box(0, 0, limit, limit)
    distress_position = search_area.difference(unary_union(covered))
    answer = int(
        ((distress_position.bounds[0] + 1) * limit) + distress_position.bounds[1] + 1
    )
    print("Part 2:  " + str(answer))


input = get_input()
part1(input)
part2b(input)
