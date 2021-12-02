

TotalValidCodes = 0

FileInput = open(".\Day5\D5_Input.txt", "r")
Codes = FileInput.readlines()

for Code in Codes:
    LetterRepeat = 0
    PairRepeat = 0
    CodeLen = len(Code)
    for i in range (CodeLen-2):
        if Code[i] == Code[i+2]:
            LetterRepeat += 1
    if LetterRepeat == 0:
        continue

    for i in range (CodeLen-4):
        for j in range (i+2, CodeLen-2):
            if Code[i] == Code[j]:
                if Code[i+1] == Code[j+1]:
                    PairRepeat += 1
    if PairRepeat < 1:
        continue

    TotalValidCodes += 1
    
print(TotalValidCodes)