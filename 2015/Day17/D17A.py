import itertools


FileInput = open(".\Day17\D17_Input.txt", "r")
InputValues = FileInput.readlines()
Containers = []
ValidCombo = 0

for Value in InputValues:
    Containers.append(int(Value))

for i in range (1, len(Containers)):
    Combinations = list(itertools.combinations(Containers, i))
    for Combination in Combinations:
        if sum(Combination) == 150:
            ValidCombo += 1
print(ValidCombo)