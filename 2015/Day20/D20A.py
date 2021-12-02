House = 332376
DesiredPresents = 34000000 / 10

while True:
    TotalPresents = 0
    for Elf in range (1, House + 1):
        if House %  Elf == 0:
            TotalPresents += Elf
    print(str(House) + "  -  " + str(TotalPresents))
    if TotalPresents >= DesiredPresents:
        print("Found - " + str(House))
        break
    House += 1