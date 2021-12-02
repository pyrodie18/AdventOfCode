B_Damage = 8
B_Armor = 2
High_Price = 0


Weapons = [
    {'Name': 'none', 'Price': 0, 'Damage': 0, 'Armor': 0},
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

for w in Weapons:
    for a in Armor:
        for r1 in Ring:
            for r2 in Ring:
                P_HP = 100
                B_HP = 109
                
                if r1['Name'] == r2['Name']:
                    pass

                P_Turn_Change = (w['Damage'] + r1['Damage'] + r2['Damage']) - B_Armor
                if P_Turn_Change <= 1:
                    P_Turn_Change = 1

                B_Turn_Change = B_Damage - (a['Armor'] + r1['Armor'] + r2['Armor'])
                if B_Turn_Change <= 1:
                    B_Turn_Change = 1

                while True:
                    B_HP = B_HP - P_Turn_Change
                    if B_HP <= 0:  #Win
                        break

                    P_HP = P_HP - B_Turn_Change
                    if P_HP <= 0:
                        Price = (w['Price'] + a['Price'] + r1['Price'] + r2['Price'])
                        if Price > High_Price:
                            High_Price = Price
                            print(Price)
                        break

print(High_Price)