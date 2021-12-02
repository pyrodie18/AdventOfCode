from collections import deque

with open('./Day22/D22_Input.txt') as f:
    lines = [line.rstrip() for line in f]
cards = [[],[]]

player = ''
for line in lines:
    if len(line) < 1:
        continue
    elif not line.isnumeric():
        player = int(line.split()[1][0])
    else:
        cards[player-1].append(int(line))


def play_game(cards, game_num):
    past_hands = set()
    move = 0
    while len(cards[0]) > 0 and len(cards[1]) > 0:
        move += 1
        if (tuple(cards[0]), tuple(cards[0])) in past_hands:
            cards = [cards[0], []]
            print("match", game_num, move, cards[0], cards[1])
            return cards
        else:
            past_hands.add((tuple(cards[0]), tuple(cards[0])))
        current_cards = [cards[0].popleft(), cards[1].popleft()]
        if (len(cards[0]) >= current_cards[0]) and (len(cards[1]) >= current_cards[1]):
            new_hand = [[],[]]
            for i in (0, 1):
                for j in range(current_cards[i]):
                    new_hand[i].append(cards[i][j])
            new_hand[0] = deque(new_hand[0])
            new_hand[1] = deque(new_hand[1])
            print("recurse", game_num, move, new_hand)
            next_game = play_game(new_hand, game_num + 1)
            if len(next_game[0]) > len(next_game[1]):
                cards[0].append(current_cards[0])
                cards[0].append(current_cards[1])
            else:
                cards[1].append(current_cards[1])
                cards[1].append(current_cards[0])
        else:
            if current_cards[0] > current_cards[1]:
                cards[0].append(current_cards[0])
                cards[0].append(current_cards[1])
            else:
                cards[1].append(current_cards[1])
                cards[1].append(current_cards[0])
    print(game_num, move, cards[0], cards[1])
    return cards
    
cards[0] = deque(cards[0])
cards[1] = deque(cards[1])
cards = play_game(cards, 1)

if len(cards[0]) > 1:
    winner = list(cards[0])
else:
    winner = list(cards[1])
winner = winner[::-1]
total = 0

for i, num in enumerate(winner):
    total += (num * (i + 1))
print(total)