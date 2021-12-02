FileInput = open(".\Day8\D8_Input.txt", "r")
Instructions = FileInput.readlines()

TotalEvaluated = 0
TotalUnEvaluated = 0
for i in range (len(Instructions)):
    Instructions[i] = Instructions[i].strip()
    TotalUnEvaluated += len(Instructions[i])
    TotalEvaluated += len(eval(Instructions[i]))

print(TotalUnEvaluated - TotalEvaluated)