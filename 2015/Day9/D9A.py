import itertools

FileInput = open(".\Day9\D9_Input.txt", "r")
Distances = FileInput.readlines()

Pairs = {}
LowDistance = 0

# Ingest all distance pairs
for Pair in Distances:
    Set = Pair.split()
    if Set[0] not in Pairs:
        Pairs[Set[0]] = {}

    if Set[2] not in Pairs[Set[0]]:
        Pairs[Set[0]][Set[2]] = int(Set[4])
    
    if Set[2] not in Pairs:
        Pairs[Set[2]] = {}

    if Set[0] not in Pairs[Set[2]]:
        Pairs[Set[2]][Set[0]] = int(Set[4])

Permutations = list(itertools.permutations(list(Pairs.keys())))
NumOfStations = len(list(Pairs.keys()))

for Perm in Permutations:
    Total = 0
    for i in range (NumOfStations - 1):
        Total += Pairs[Perm[i]][Perm[i + 1]]
    if Total > LowDistance:
        LowDistance = Total

print(LowDistance)