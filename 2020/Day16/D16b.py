from collections import defaultdict
all_fields = []
my_ticket = [113,53,97,59,139,73,89,109,67,71,79,127,149,107,137,83,131,101,61,103]

with open('./Day16/D16_FieldList.txt') as f:
    lines = [line.rstrip() for line in f]

values = []
for i in range (1000):
    values.append([])

# Load the possible field names into each value column
for line in lines:
    line = line.split(':')
    field = line[0]
    all_fields.append(field)
    line = line[1].split()
    field_values = [(line[0].split("-")[0], line[0].split("-")[1]), (line[2].split("-")[0], line[2].split("-")[1])]

    for ranges in field_values:
        start = int(ranges[0])
        stop = int(ranges[1])
        i = start
        while i <= stop:
            values[i].append(field)
            i += 1

# Convert list of field names into set
for i, field_names in enumerate(values):
    values[i] = set(field_names)
all_fields = set(all_fields)

with open('./Day16/D16_NearByList.txt') as f:
    lines = [line.rstrip().split(",") for line in f]

# Load all field names into each possible field
possible_fields = []
for j in range(20):
    possible_fields.append(all_fields)


for line in lines:
    valid = True
    for field in line:
        if len(values[int(field)]) < 1:
            valid = False
            break
    if valid:
        for i, field in enumerate(line):
            if len(values[int(field)]) < 20:
                intersection_of_fields = possible_fields[i].intersection(values[int(field)])
                possible_fields[i] = intersection_of_fields


while True:
    more_to_go = False
    for i, values_set in enumerate(possible_fields):
        if len(values_set) > 1:
            more_to_go = True
            continue
        else:
            for j, values_to_diff in enumerate(possible_fields):
                if j == i:
                    continue
                else:
                    values_diff = values_to_diff.difference(values_set)
                    possible_fields[j] = values_diff
    if not more_to_go:
        break

running_total = 1
for i, values_set in enumerate(possible_fields):
    for j in values_set:
        if j.split()[0] == "departure":
            running_total *= my_ticket[i]

print(running_total)