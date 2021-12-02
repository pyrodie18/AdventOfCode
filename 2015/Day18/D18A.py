FileInput = open(".\Day18\D18_Input.txt", "r")
InputValues = FileInput.readlines()
CurrentBoard = []

for InputRow in InputValues:
    Row = []
    InputRow = str(InputRow).strip()
    for Cell in InputRow:
        Row.append(Cell)
    CurrentBoard.append(Row)

NumCols = len(Row)
NumRows = len(CurrentBoard)

for c in range(100):
    CurrentBoard[0][0] = '#'
    CurrentBoard[0][99] = '#'
    CurrentBoard[99][0] = '#'
    CurrentBoard[99][99] = '#'
    NewBoard = []
    for r in range (NumRows):
        NewRow = []
        for c in range (NumCols):
            Neighbors = []
            if r >= 1:
                if c >= 1:
                    Neighbors.append(CurrentBoard[r-1][c-1])
                Neighbors.append(CurrentBoard[r-1][c])
                if c < NumCols - 1:
                    Neighbors.append(CurrentBoard[r-1][c+1])
            if r < NumRows - 1:
                if c >= 1:
                    Neighbors.append(CurrentBoard[r+1][c-1])
                Neighbors.append(CurrentBoard[r+1][c])
                if c < NumCols - 1:
                    Neighbors.append(CurrentBoard[r+1][c+1])
            if c >= 1:
                Neighbors.append(CurrentBoard[r][c-1])
            if c < NumCols - 1: 
                Neighbors.append(CurrentBoard[r][c+1])

            CountOn = Neighbors.count('#')
            if (CurrentBoard[r][c] == '#') and (CountOn == 2 or CountOn == 3):
                NewRow.append('#')
            elif (CurrentBoard[r][c] == '.') and CountOn == 3:
                NewRow.append('#')
            else:
                NewRow.append('.')
        NewBoard.append(NewRow)
    CurrentBoard = NewBoard
    CurrentBoard[0][0] = '#'
    CurrentBoard[0][99] = '#'
    CurrentBoard[99][0] = '#'
    CurrentBoard[99][99] = '#'

LightsOn = 0
for row in CurrentBoard:
    LightsOn += row.count('#')

print(LightsOn)

