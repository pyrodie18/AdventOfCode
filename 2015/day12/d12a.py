import re
from os import path

FileInput = open(path.join(path.dirname(__file__), 'input.txt'), "r")
Instructions = FileInput.readline()

regex = re.compile('-?\d+')

Total = 0
Values = regex.findall(Instructions)
for Value in Values:
    Total += int(Value)
    print (Value + "- " + str(Total))

print(Total)
