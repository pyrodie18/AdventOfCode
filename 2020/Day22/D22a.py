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
    
player1 = deque(cards[0])
player2 = deque(cards[1])

while len(player1) > 0 and len(player2) > 0:
    card1 = player1[0]
    card2 = player2[0]
    if card1 > card2:
        player1.append(card1)
        player1.append(card2)
    else:
        player2.append(card2)
        player2.append(card1)
    player1.popleft()
    player2.popleft()

if len(player1) > 1:
    winner = list(player1)
else:
    winner = list(player2)
winner = winner[::-1]
total = 0

for i, num in enumerate(winner):
    total += (num * (i + 1))
print(total)