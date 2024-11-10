from os import path

FileInput = open(path.join(path.dirname(__file__), 'input.txt'), "r")
Instructions = FileInput.readlines()

Total = 0

for i in range (len(Instructions)):
    Instructions[i] = Instructions[i].strip()
    Total += Instructions[i].count('\\') + Instructions[i].count('"') + 2

print(Total)