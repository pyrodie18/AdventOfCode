def get_data():
    from os import path

    data = []

    with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
        for line in f:
            line = line.strip().split()
            line[1] = int(line[1])
            line[2] = line[2][2:-1]
            data.append(line)
    return data


def part1(data):
    from shapely import geometry

    x = 0
    y = 0
    coords = []
    coords.append((x, y))

    for line in data[:-1]:
        if line[0] == "U":
            y += line[1]
        elif line[0] == "D":
            y -= line[1]
        if line[0] == "L":
            x -= line[1]
        if line[0] == "R":
            x += line[1]
        coords.append((x, y))

    poly = geometry.Polygon(coords)

    import matplotlib.pyplot as plt

    x, y = poly.exterior.xy
    plt.plot(x, y)
    plt.savefig('test.png')

    # print('Part 1:  {}'.format(str(winners)))


def part2(data):
    pass
    # print('Part 2:  {}'.format(str(winners)))


data = get_data()
part1(data)
part2(data)
