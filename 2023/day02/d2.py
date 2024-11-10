CUBES = {
    "red": 12,
    "green": 13,
    "blue": 14
}


def get_input():
    from os import path

    input = []

    with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
        for line in f:
            game_info = {}
            line = line.strip().split(":")
            game = line[0].split()
            game_info["game"] = int(game[1])
            game_info["rounds"] = []
            rounds_tmp = line[1].split(";")
            for rd in rounds_tmp:
                round = {}
                items = rd.split(",")
                for item in items:
                    item = item.split()
                    round[item[1]] = int(item[0])
                game_info["rounds"].append(round)
            input.append(game_info)
    return input


def valid_round(round):
    for k, v in round.items():
        if v > CUBES[k]:
            return False
    return True


def check_game(game):
    for round in game["rounds"]:
        if not valid_round(round):
            return False
    return True


def find_min_power(game):
    from collections import defaultdict

    d = defaultdict(int)

    for round in game["rounds"]:
        for k, v in round.items():
            if v > d[k]:
                d[k] = v
    result = 1
    for v in d.values():
        result *= v
    return result


def part1(input):
    total = 0
    for game in input:
        if check_game(game):
            total += game["game"]

    print("Part 1:  {}".format(str(total)))


def part2(input):
    total = 0
    for game in input:
        total += find_min_power(game)
    print("Part 2:  {}".format(str(total)))


input = get_input()
part1(input)
part2(input)
