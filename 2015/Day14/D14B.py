FileInput = open(".\Day14\D14_Input.txt", "r")
Animals = FileInput.readlines()
Position = []

for Raindeer in Animals:
    Raindeer = Raindeer.split()
    Speed = int(Raindeer[3])
    Time = int(Raindeer[6])
    Rest = int(Raindeer[13])

    CurrentAnimal = []
    CurrentPosition = 0

    while True:
        for i in range (CurrentPosition, min((CurrentPosition + Time), 2503)):
            if i == 0:
                CurrentAnimal.append(Speed)
            else:
                CurrentAnimal.append(CurrentAnimal[i - 1] + Speed)
            CurrentPosition += 1

        for i in range (CurrentPosition, min((CurrentPosition + Rest), 2503)):
            CurrentAnimal.append(CurrentAnimal[i - 1])
            CurrentPosition += 1
        
        if CurrentPosition >= 2503:
            break
    Position.append(CurrentAnimal)

for i in range(2503):
    HighPosition = 0
    for j in range(len(Position)):
        if Position[j][i] > HighPosition:
            HighPosition = Position[j][i]
    for j in range(len(Position)):
        if Position[j][i] == HighPosition:
            Position[j][i] = 1
        else:
            Position[j][i] = 0

HighPoints = 0
for i in range(len(Position)):
    if sum(Position[i]) > HighPoints:
        HighPoints = sum(Position[i])

print(HighPoints)
