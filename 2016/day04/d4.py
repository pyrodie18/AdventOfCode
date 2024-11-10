ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def get_input():
    from os import path

    input = []

    with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
        for line in f:
            line = line.strip().split("-")
            name = "".join(line[:-1])
            sector = int(line[-1].split("[")[0])
            checksum = line[-1].split("[")[1][0:-1]
            data = {
                "line": line,
                "name": name,
                "sector": sector,
                "checksum": checksum
            }
            input.append(data)
    return input


def validate_checksum(name, checksum):
    from collections import Counter
    letter_counts = dict(Counter(name))
    counts = list(letter_counts.values())
    counts.sort(reverse=True)
    keys = list(letter_counts.keys())
    keys.sort()
    calc_checksum = []
    for item in counts[:5]:
        for key in keys:
            if letter_counts[key] == item:
                calc_checksum.append(key)
                del letter_counts[key]
                keys.remove(key)
                break
    return "".join(calc_checksum) == checksum


def part1(input):
    total = 0
    for room in input:
        if validate_checksum(room["name"], room["checksum"]):
            total += room["sector"]
    print("Part 1:  {}".format((str(total))))


def part2(input):
    for room in input:

        if validate_checksum(room["name"], room["checksum"]):
            rot = room["sector"] % 26
            pt_room = []
            for ct_word in room["line"][:-1]:
                pt_word = []
                for cl in ct_word:
                    my_index = ALPHABET.index(cl)
                    my_index += rot
                    my_index = my_index % 26
                    pt_word.append(ALPHABET[my_index])
                pt_room.append("".join(pt_word))
            if (" ".join(pt_room)) == "northpole object storage":
                print("Part 2:  {}".format(room["sector"]))


input = get_input()
part1(input)
part2(input)
