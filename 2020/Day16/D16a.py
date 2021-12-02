with open('./Day16/D16_FieldList.txt') as f:
    lines = [line.rstrip() for line in f]

values = []
for i in range (1000):
    values.append([])

for line in lines:
    line = line.split(':')
    field = line[0]
    line = line[1].split()
    field_values = [(line[0].split("-")[0], line[0].split("-")[1]), (line[2].split("-")[0], line[2].split("-")[1])]

    for range in field_values:
        start = int(range[0])
        stop = int(range[1])
        i = start
        while i <= stop:
            values[i].append(field)
            i += 1

with open('./Day16/D16_NearByList.txt') as f:
    lines = [line.rstrip().split(",") for line in f]

rejects = []

for line in lines:
    for field in line:
        if len(values[int(field)]) < 1:
            rejects.append(int(field))

print(sum(rejects))
