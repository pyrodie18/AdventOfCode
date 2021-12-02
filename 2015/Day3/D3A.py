InputFile = open("D3_Input.txt", "r")

Directions = InputFile.read()

Grid =  [[0 for i in range(250)] for j in range(250)]
Col = 125
Row = 125
Houses = 1

Grid[Row][Col] += 1

for Step in Directions:
    if Step == "^":
        Row = Row + 1
    elif Step == ">":
        Col = Col + 1
    elif Step == "v":
        Row = Row - 1
    else:
        Col = Col - 1

    if Grid[Row][Col] == 0:
        Houses += 1
    Grid[Row][Col] += 1

print(Houses)
