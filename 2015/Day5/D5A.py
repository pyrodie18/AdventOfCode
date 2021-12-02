

Vowels = [ 'a', 'e', 'i', 'o', 'u']
Blacklist = ['ab', 'cd', 'pq', 'xy']
TotalValidCodes = 0

FileInput = open(".\Day5\D5_Input.txt", "r")
Codes = FileInput.readlines()

for Code in Codes:
    VowelCount = 0
    DoubleLetterCount = 0
    BadPair = 0

    #Check rules for Vowels
    for Vowel in Vowels:
        VowelCount += Code.count(Vowel)
    if VowelCount < 3:
        continue

    #Check rules for bad pairs
    for Pair in Blacklist:
        BadPair += Code.count(Pair)
    if BadPair > 0:
        continue

    for i in range (len(Code)-1):
        if Code[i] == Code[i+1]:
            DoubleLetterCount += 1
    if DoubleLetterCount == 0:
        continue

    TotalValidCodes += 1
    
print(TotalValidCodes)