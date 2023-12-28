B_HP = 109
B_DAMAGE = 8
B_ARMOR = 2

Weapons = [
    {'Name': 'dagger', 'Price': 8, 'Damage': 4, 'Armor': 0},
    {'Name': 'shortsword', 'Price': 10, 'Damage': 5, 'Armor': 0},
    {'Name': 'warhammer', 'Price': 25, 'Damage': 6, 'Armor': 0},
    {'Name': 'longsword', 'Price': 40, 'Damage': 7, 'Armor': 0},
    {'Name': 'greataxe', 'Price': 74, 'Damage': 8, 'Armor': 0}
]

Armor = [
    {'Name': 'none', 'Price': 0, 'Damage': 0, 'Armor': 0},
    {'Name': 'leather', 'Price': 13, 'Damage': 0, 'Armor': 1},
    {'Name': 'chainmail', 'Price': 31, 'Damage': 0, 'Armor': 2},
    {'Name': 'splintmail', 'Price': 53, 'Damage': 0, 'Armor': 3},
    {'Name': 'bandedmail', 'Price': 75, 'Damage': 0, 'Armor': 4},
    {'Name': 'platemail', 'Price': 102, 'Damage': 0, 'Armor': 5}
]

Ring = [
    {'Name': 'none1', 'Price': 0, 'Damage': 0, 'Armor': 0},
    {'Name': 'none2', 'Price': 0, 'Damage': 0, 'Armor': 0},
    {'Name': 'D1', 'Price': 25, 'Damage': 1, 'Armor': 0},
    {'Name': 'D2', 'Price': 50, 'Damage': 2, 'Armor': 0},
    {'Name': 'D3', 'Price': 100, 'Damage': 3, 'Armor': 0},
    {'Name': 'A1', 'Price': 20, 'Damage': 0, 'Armor': 1},
    {'Name': 'A2', 'Price': 40, 'Damage': 0, 'Armor': 2},
    {'Name': 'A3', 'Price': 80, 'Damage': 0, 'Armor': 3}
]


def fight(armor, damage):
    p_ph = 100
    b_ph = B_HP

    while True:
        b_ph -= (1 if damage - B_ARMOR < 1 else damage - B_ARMOR)
        if b_ph <= 0:
            return "player"
        p_ph -= (1 if B_DAMAGE - armor < 1 else B_DAMAGE - armor)
        if p_ph <= 0:
            return "boss"


def play():
    cheapest = 10000000
    expensive = 0
    prices = []
    for w in Weapons:
        for a in Armor:
            for r1 in Ring:
                for r2 in Ring:
                    if r1['Name'] == r2['Name']:
                        continue
                    damage = w['Damage'] + r1['Damage'] + r2['Damage']
                    armor = a['Armor'] + r1['Armor'] + r2['Armor']
                    cost = w['Price'] + r1['Price'] + r2['Price'] + a['Price']

                    winner = fight(armor, damage)

                    if winner == "player":
                        cheapest = min(cheapest, cost)
                    elif w["Name"] != "none":
                        expensive = max(expensive, cost)
                        # prices.append(cost)
                        # prices = sorted(prices, reverse=True)

    print('Part 1  {}'.format(str(cheapest)))
    print('Part 2  {}'.format(str(expensive)))


play()
