import re

FileInput = open(".\Day12\D12_Input.txt", "r")
Instructions = FileInput.readline()

regex = re.compile('-?\d+')

Total = 0
Values = regex.findall(Instructions)
for Value in Values:
    Total += int(Value)
    print (Value + "- " + str(Total))

print(Total)
