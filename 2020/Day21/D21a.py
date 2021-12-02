from collections import defaultdict
all_ingredients = defaultdict(int)
all_allergents = defaultdict(int)
possibles = {}
kitchen_sink = []

with open('./Day21/D21_Input.txt') as f:
    lines = [line.rstrip() for line in f]

for line in lines:
    line = line.split("(")
    ingredients = line[0].split()
    for i in ingredients:
        all_ingredients[i] += 1
    ingredients = set(ingredients) 
    allergens = line[1].split()
    allergens.pop(0)
    for i, a in enumerate(allergens):
        allergens[i] = a[0:-1]
        all_allergents[allergens[i]] += 1
    kitchen_sink.append([ingredients, allergens])

ingredient_list = list(all_ingredients.keys())
allergents_list = list(all_allergents.keys())

for a in allergents_list:
    possible_ingredients = set(ingredient_list)
    for dish in kitchen_sink:
        if a in dish[1]:
            possible_ingredients = possible_ingredients.intersection(set((dish[0])))
    possibles[a] = possible_ingredients

for a in allergents_list:
    for b in possibles[a]:
        all_ingredients[b] = 0

total = 0
for i in ingredient_list:
    total += all_ingredients[i]

print(total)


while True:
    more_to_go = False
    for a in allergents_list:
        if len(possibles[a]) > 1:
            more_to_go = True
            continue
        else:
            for j in allergents_list:
                if j == a:
                    continue
                else:
                    values_diff = possibles[j].difference(possibles[a])
                    possibles[j] = values_diff
    if not more_to_go:
        break
print(possibles)