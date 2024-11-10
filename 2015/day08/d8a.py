from os import path

FileInput = open(path.join(path.dirname(__file__), 'input.txt'), "r")
Instructions = FileInput.readlines()

TotalEvaluated = 0
TotalUnEvaluated = 0
for i in range (len(Instructions)):
    Instructions[i] = Instructions[i].strip()
    TotalUnEvaluated += len(Instructions[i])
    TotalEvaluated += len(eval(Instructions[i]))

print(TotalUnEvaluated - TotalEvaluated)