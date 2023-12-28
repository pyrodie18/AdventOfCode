def get_input():
    from os import path

    input = []

    with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
        for line in f:
            line = line.strip()

            line = line.split(":")
            card = int(line[0].split()[1])
            numbers = line[1].split("|")
            winners = set([int(i) for i in numbers[0].split()])
            picks = set([int(i) for i in numbers[1].split()])
            input.append({
                "card": card,
                "winners": winners,
                "picks": picks
            })
    return input


def find_winners(picks, winners):
    return picks.intersection(winners)


def part1(input):
    total = 0
    for card in input:
        matches = find_winners(card["picks"], card["winners"])
        if len(matches) > 0:
            card_total = 1
            for i in range(len(matches) - 1):
                card_total *= 2
            total += card_total
    print("Part 1:  {}".format(str(total)))


def part2(input):
    from collections import defaultdict

    cards = defaultdict(int)

    for card in input:
        card_num = card["card"]
        cards[card_num] += 1

        winners = len(find_winners(card["picks"], card["winners"]))

        for i in range(card_num + 1, card_num + winners + 1):
            cards[i] += cards[card_num]
    print("Part 2:  {}".format(str(sum(cards.values()))))


input = get_input()
part1(input)
part2(input)
