def get_input():
    from os import path

    input = []
    i = 1

    with open(path.join(path.dirname(__file__), "input.txt"), "r") as f:
        for line in f:
            input.append((int(line.strip()), i))
            i += 1
    return input


def part1(input):
    shuffle = [i for i in input]
    size = len(input) - 1

    for line in input:
        i = line[0]
        if i == 0:
            continue
        pos = shuffle.index(line)
        shuffle.remove(line)
        if abs(i) > size:
            tmp_i = i % size
            tmp_i = -tmp_i if i < 0 else tmp_i
        else:
            tmp_i = i

        new_pos = pos + tmp_i
        if new_pos > size:
            new_pos = new_pos - size
        elif new_pos == 0:
            new_pos = -1
        shuffle.insert(new_pos, line)

    print(shuffle)
    total = 0
    for i in [1000, 2000, 3000]:
        i = i % size
        zero_pos = shuffle.index((0, 4284))
        if zero_pos + i > size:
            i = (zero_pos + i) - size
        total += shuffle[i][0]

    print("Part 1:  " + str(total))


def part2(input):
    print("Part 2:  ")


input = get_input()
part1(input)
part2(input)
