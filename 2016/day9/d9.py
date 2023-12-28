def get_input():
    from os import path

    input = []

    with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
        for line in f:
            input.append(line.strip())
    return input


def extract_marker(marker):
    import re

    close_paren = re.search(r'\(\d+x\d+(\))', marker)
    marker_size = close_paren.end()
    the_marker = marker[1:marker_size - 1]
    tmp = the_marker.split("x")
    repeat = int(tmp[1])
    length = int(tmp[0])

    return {
        "marker": the_marker,
        "marker_size": marker_size,
        "repeat": repeat,
        "length": length
    }


def part1(input):
    answer = ""
    i = 0
    while i < len(input):
        if input[i] == "(":
            marker = extract_marker(input[i:i + 10])
            compressed = input[i + marker["marker_size"]
                :i + marker["marker_size"] + marker["length"]]
            for j in range(0, marker["repeat"]):
                answer += compressed
            i = i + marker["marker_size"] + marker["length"]
        else:
            answer += input[i]
            i += 1
    # print(answer)
    print("Part 1:  {}".format(str(len(answer))))


def part2(input):
    pass


input = get_input()
part1(input[0])
part2(input[0])
