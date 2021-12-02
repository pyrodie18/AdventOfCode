FileInput = open(".\Day14\D14_Input.txt", "r")
Animals = FileInput.readlines()
HighSpeed = 0

for Raindeer in Animals:
    Raindeer = Raindeer.split()
    Distance = 0
    Speed = int(Raindeer[3])
    Time = int(Raindeer[6])
    Rest = int(Raindeer[13])
    TotalTime = Time + Rest

    Rounds = 2503 // TotalTime
    Remainder = 2503 % Rounds

    if Remainder >= Time:
        Distance = Speed * Time
    else:
        Distance = Speed * Remainder

    Distance += (Speed * Time * Rounds)
    if Distance > HighSpeed:
        HighSpeed = Distance

print(HighSpeed)