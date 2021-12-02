Directions = open("D1_Input.txt", "r")
steps = Directions.read()
CurrentFloor = 0
CurrentStep = 1

for i in steps:
    if i == "(":
        CurrentFloor += 1
    else:
        CurrentFloor -= 1
    if CurrentFloor < 0:
        break

    CurrentStep += 1

print(CurrentStep)
