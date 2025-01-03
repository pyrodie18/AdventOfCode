import itertools
from os import path


FileInput = open(path.join(path.dirname(__file__), 'input.txt'), "r")
IngredientList = FileInput.readlines()

Ingredients = {}
MyIngredients = []
HighScore = 0
Measurements = ["capacity", "durability", "flavor", "texture"]

for Ingredient in IngredientList:
    Ingredient = Ingredient.strip()
    Ingredient = Ingredient.split()
    if Ingredient[0][:-1] not in Ingredients:
        Ingredient[0] = Ingredient[0][:-1]
        Ingredients[Ingredient[0]] = {}
        Ingredients[Ingredient[0]]["capacity"] = int(Ingredient[2][:-1])
        Ingredients[Ingredient[0]]["durability"] = int(Ingredient[4][:-1])
        Ingredients[Ingredient[0]]["flavor"] = int(Ingredient[6][:-1])
        Ingredients[Ingredient[0]]["texture"] = int(Ingredient[8][:-1])
        Ingredients[Ingredient[0]]["calories"] = int(Ingredient[10])
#        for i in range (100):
#            MyIngredients.append(Ingredient[0])

PossibleCombinations = list(itertools.combinations_with_replacement(list(Ingredients.keys()), 100))
for Combination in PossibleCombinations:
    Total = 1
    for Measurement in Measurements:
        MeasurementTotal = 0
        for Ingredient in list(Ingredients.keys()):
            CountIngredients = Combination.count(Ingredient)
            MeasurementTotal += (Ingredients[Ingredient][Measurement] * CountIngredients)
        if MeasurementTotal <= 0:
            MeasurementTotal = 0
        Total = Total * MeasurementTotal
    if Total > HighScore:
        HighScore = Total




print(HighScore)