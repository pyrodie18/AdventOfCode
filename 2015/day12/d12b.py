import json
from os import path

FileInput = open(path.join(path.dirname(__file__), 'input.txt'), "r")
data = json.load(FileInput)

print(data)