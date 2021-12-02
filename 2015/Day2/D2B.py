InputFile = open("D2_Input.txt", "r")

Measurements = []
for box in InputFile:
    box = box.strip()
    box = box.split("x")
    for i in range (3):
        box[i] = int(box[i])
    box.sort()
    Measurements.append(box)

i = 0
TotalPaper = 0
TotalRibbon = 0
for box in Measurements:
    paper = (((box[0] * box[1]) + (box[0] * box[2]) + (box[1] * box[2])) * 2) + (box[0] * box[1])
    ribbon = ((box[0] * 2) + (box[1] * 2)) + (box[0] * box[1] * box[2])

    TotalRibbon += ribbon
    TotalPaper += paper

print(TotalRibbon)