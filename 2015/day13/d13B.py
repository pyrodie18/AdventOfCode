import itertools
from os import path

FileInput = open(path.join(path.dirname(__file__), 'input.txt'), "r")
GuestList = FileInput.readlines()

Guests = {}
HighJoy = 0

for Guest in GuestList:
    Guest = Guest.strip()[:-1]
    Set = Guest.split()
    if Set[0] not in Guests:
        Guests[Set[0]] = {}

    if Set[10] not in Guests[Set[0]]:
        if Set[2] == "lose":
            Value = int(Set[3]) * -1
        else:
            Value = int(Set[3])
        Guests[Set[0]][Set[10]] = Value

MyGuests = list(Guests.keys())

print(MyGuests)
#Add Me
Guests["Me"] = {}
for Guest in MyGuests:
    Guests['Me'][Guest] = 0
    Guests[Guest]["Me"] = 0

MyGuests = list(Guests.keys())

Permutations = list(itertools.permutations(MyGuests))
NumOfGuests = len(MyGuests)

for Perm in Permutations:
    Total = 0
    for i in range (NumOfGuests):
        if i == 0:
            Total += Guests[Perm[i]][Perm[NumOfGuests - 1]]
        else:
            Total += Guests[Perm[i]][Perm[i - 1]]

        if i == NumOfGuests - 1:
            Total += Guests[Perm[i]][Perm[0]]
        else:
            Total += Guests[Perm[i]][Perm[i + 1]]
    if Total > HighJoy:
        HighJoy = Total
print(HighJoy)