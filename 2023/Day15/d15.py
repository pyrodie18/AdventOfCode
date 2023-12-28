def get_data():
    from os import path

    with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
        for line in f:
            data = line.strip().split(",")
    return data


def hash_step(data):
    total = 0
    for c in data:
        total += ord(c)
        total *= 17
        total %= 256
    return total


def part1(data):
    total = 0
    for step in data:
        total += hash_step(step)
    print('Part 1:  {}'.format(str(total)))


def part2(data):
    from collections import defaultdict

    boxes = defaultdict(list)

    for step in data:
        if "=" in step:
            label = step[:step.index("=")]
            lense = int(step[step.index("=")+1:])
            label_hash = hash_step(label)

            found = False
            for i, item in enumerate(boxes[label_hash]):
                if item[0] == label:
                    boxes[label_hash][i] = (label, lense)
                    found = True
            if not found:
                boxes[label_hash].append((label, lense))
        else:
            label = step[:-1]
            label_hash = hash_step(label)

            for i, item in enumerate(boxes[label_hash]):
                if item[0] == label:
                    del boxes[label_hash][i]
                    break

    total = 0

    for box in boxes.keys():
        for i, item in enumerate(boxes[box]):
            total += ((int(box) + 1) * (i + 1) * item[1])

    print('Part 2:  {}'.format(str(total)))


data = get_data()
part1(data)
part2(data)
