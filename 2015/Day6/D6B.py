InputFile = open(".\Day6\D6_Input.txt", "r")

Directions = InputFile.readlines()

Grid =  [[0 for i in range(1000)] for j in range(1000)]

def toggle(Grid, start, end):
    for i in range(start[0], end[0]+1):
        for j in range(start[1], end[1]+1):
            Grid[i][j] = Grid[i][j] + 2

    return Grid

def off(Grid, start, end):
    for i in range(start[0], end[0]+1):
        for j in range(start[1], end[1]+1):
           Grid[i][j] = Grid[i][j] - 1
           if Grid[i][j] < 0:
               Grid[i][j] = 0
    return Grid

def on(Grid, start, end):
    for i in range(start[0], end[0]+1):
        for j in range(start[1], end[1]+1):
            Grid[i][j] = Grid[i][j] + 1
    return Grid


for Direction in Directions:
    Direction = Direction.split()
    start = Direction[-3].split(",")
    for i in range(2):
        start[i] = int(start[i])
    end = Direction[-1].split(",")
    for i in range(2):
        end[i] = int(end[i])
    if Direction[-4] == "toggle":
        Grid = toggle(Grid, start, end)
    elif Direction[-4] == "off":
        Grid = off(Grid, start, end)
    else:
        Grid = on(Grid, start, end)

TotalOn = 0
for i in range(1000):
    for j in range(1000):
        TotalOn += Grid[i][j]

print(TotalOn)