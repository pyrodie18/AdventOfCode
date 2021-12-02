import hashlib

PuzzleInput = "ckczppom"
i = 0

while True:
    String = PuzzleInput + str(i)
    hash = hashlib.md5(String.encode()).hexdigest()
    start = hash[0:6]
    if start.count("0") == 6:
        print(i)
        break
    i += 1
