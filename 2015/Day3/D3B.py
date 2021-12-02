InputFile = open("D3_Input.txt", "r")

Directions = InputFile.read()

Grid =  [[0 for i in range(250)] for j in range(250)]
SantaCol = 125
SantaRow = 125
RobotCol = 125
RobotRow = 125
Houses = 1

Grid[SantaCol][SantaRow] += 1
Counter = 1

for Step in Directions:
    if Counter % 2 == 1:
        if Step == "^":
            SantaRow += 1
        elif Step == ">":
            SantaCol += 1
        elif Step == "v":
            SantaRow -= 1
        else:
            SantaCol -= 1
        if Grid[SantaRow][SantaCol] == 0:
            Houses += 1
        Grid[SantaRow][SantaCol] += 1
    else:
        if Step == "^":
            RobotRow += 1
        elif Step == ">":
            RobotCol += 1
        elif Step == "v":
            RobotRow -= 1
        else:
            RobotCol -= 1
        if Grid[RobotRow][RobotCol] == 0:
            Houses += 1
        Grid[RobotRow][RobotCol] += 1
    Counter += 1
print(Houses)
