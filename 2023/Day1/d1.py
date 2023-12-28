def get_input():
    from os import path

    input = []

    with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
        for line in f:
            input.append(line.strip())
    return input


def part1(input):
    import re
    total = 0

    for line in input:
        values = re.findall(r'(\d)', line)
        the_value = values[0] + values[-1]
        total += int(the_value)

    print("Part 1:  {}".format(str(total)))


def part2(input):
    import re
    total = 0
    translations = {
        "zero": "z0o",
        "one": "o1e",
        "two": "t2o",
        "three": "t3e",
        "four": "f4r",
        "five": "f5e",
        "six": "s6x",
        "seven": "s7n",
        "eight": "e8t",
        "nine": "n9e"
    }

    for line in input:
        for k, v in translations.items():
            line = line.replace(k, v)
        values = re.findall(r'(\d)', line)
        the_value = values[0] + values[-1]
        total += int(the_value)
        # print("{}:   {}".format(line, the_value))
    print("Part 2:  {}".format(str(total)))


input = get_input()
part1(input)
part2(input)
