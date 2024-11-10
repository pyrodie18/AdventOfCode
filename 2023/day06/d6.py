def get_input():
    from os import path

    with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
        for line in f:
            line = line.strip().split()
            if line[0].startswith("Time"):
                time = [int(i) for i in line[1:]]
            if line[0].startswith("Distance"):
                distance = [int(i) for i in line[1:]]
    input = {
        "time": time,
        "distance": distance
    }

    return input


def find_winners(time, record):
    import numpy as np

    results = np.zeros(time, np.int64)

    for t in range(1, time):
        distance = (time - t) * t
        results[t] = distance
    return (results > record).sum()


def part1(input):
    winners = []
    for i in range(len(input["distance"])):
        winners.append(find_winners(input["time"][i], input["distance"][i]))

    margin = 1
    for i in winners:
        margin *= i

    print("Part 1:  {}".format(str(margin)))


def part2(input):
    time = ""
    for t in input["time"]:
        time += str(t)
    time = int(time)

    distance = ""
    for d in input["distance"]:
        distance += str(d)
    distance = int(distance)

    winners = find_winners(time, distance)
    print("Part 2:  {}".format(str(winners)))


input = get_input()
part1(input)
part2(input)
