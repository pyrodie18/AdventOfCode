FileInput = open(".\Day16\D16_Input.txt", "r")
FileData = FileInput.readlines()
Aunts = {}
Facts = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0, 'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}

for Aunt in FileData:
    Aunt = Aunt.replace(',', '')
    Aunt = Aunt.split()
    CurrentAunt = {}
    for i in range(2, (len(Aunt)), 2):
        CurrentAunt[Aunt[i][:-1]] = int(Aunt[i + 1])
    CurrentAunt["Excluded"] = 0
    Aunts[Aunt[1]] = CurrentAunt

for Aunt in Aunts:
    for Fact in Facts:
        if Fact in list(Aunts[Aunt].keys()):
            if Fact == 'cats' or Fact == 'trees':
                if Facts[Fact] > Aunts[Aunt][Fact]:
                    Aunts[Aunt]["Excluded"] = 1
                    break
            elif Fact == 'pomeranians' or Fact == 'goldfish':
                if Facts[Fact] < Aunts[Aunt][Fact]:
                    Aunts[Aunt]["Excluded"] = 1
                    break
            else:
                if Facts[Fact] != Aunts[Aunt][Fact]:
                    Aunts[Aunt]["Excluded"] = 1
                    break

for Aunt in Aunts:
    if Aunts[Aunt]["Excluded"] == 0:
        print(Aunt)