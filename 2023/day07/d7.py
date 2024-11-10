def get_input():
    from os import path

    input = []

    with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
        for line in f:
            line = line.strip().split()
            hand = {
                "hand": line[0],
                "bid": int(line[1]),
                "score": hand_to_int(line[0])
            }
            input.append(hand)
    return input


def categorize_hand(hand, round2=False):
    from collections import Counter

    if round2:
        ctr_hand = Counter(hand)
        if "J" in ctr_hand.elements():
            j_count = ctr_hand["J"]
            common = ctr_hand.most_common()
            if common[0][0] != "J":
                hand = hand.replace("J", common[0][0])
            else:
                if j_count != 5:
                    hand = hand.replace("J", common[1][0])

    hand = list(Counter(hand).values())
    hand.sort(reverse=True)

    if hand[0] == 5:
        return "5ofKind"
    elif hand[0] == 4:
        return "4ofKind"
    elif hand[0] == 3 and hand[1] == 2:
        return "fullhouse"
    elif hand[0] == 3:
        return "3ofKind"
    elif hand[0] == 2 and hand[1] == 2:
        return "2pair"
    elif hand[0] == 2:
        return "pair"
    else:
        return "high"


def hand_to_int(hand, round2=False):
    hand = hand.replace("A", "E")
    hand = hand.replace("K", "D")
    hand = hand.replace("Q", "C")
    if round2:
        hand = hand.replace("J", "0")
    else:
        hand = hand.replace("J", "B")
    hand = hand.replace("T", "A")
    score = int(hand, 16)
    return score


def sort_hands(hands):
    newlist = sorted(hands, key=lambda d: d['score'])
    return newlist


def part1(input):
    from collections import defaultdict

    breakdown = defaultdict(list)
    for hand in input:
        breakdown[categorize_hand(hand["hand"])].append(hand)

    ordered_hands = []
    for cat in ["high", "pair", "2pair", "3ofKind", "fullhouse", "4ofKind", "5ofKind"]:
        ordered_hands += sort_hands(breakdown[cat])

    total = 0

    for i, hand in enumerate(ordered_hands):
        total += ((i+1) * hand["bid"])

    print('Part 1:  {}'.format(str(total)))


def part2(input):
    from collections import defaultdict

    breakdown = defaultdict(list)
    for hand in input:
        hand["score"] = hand_to_int(hand["hand"], True)
        breakdown[categorize_hand(hand["hand"], True)].append(hand)

    ordered_hands = []
    for cat in ["high", "pair", "2pair", "3ofKind", "fullhouse", "4ofKind", "5ofKind"]:
        ordered_hands += sort_hands(breakdown[cat])

    total = 0

    for i, hand in enumerate(ordered_hands):
        total += ((i+1) * hand["bid"])

    print('Part 2:  {}'.format(str(total)))


input = get_input()
part1(input)
part2(input)
