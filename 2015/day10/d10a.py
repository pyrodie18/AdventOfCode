StartNumber = input("Please enter your starting number:  ")
CurrentNumber = StartNumber

#Controls the number of times you repeat
for x in range (50):
    Length = len(CurrentNumber) 
    NewNumber = ""
    i = 0
    while True:
        Consecutive = 0
        j = i
        while True:
            if CurrentNumber[i] == CurrentNumber[j]:
                Consecutive += 1
            else:
                break
            j += 1
            if j >= Length:
                break
        NewNumber = NewNumber + str(Consecutive) + str(CurrentNumber[i])
        if j >= Length:
            break
        i = j
    CurrentNumber = NewNumber
    print(len(CurrentNumber))
