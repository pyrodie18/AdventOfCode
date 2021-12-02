with open('./Day05/D05_Input.txt') as f:
    lines = [line.rstrip() for line in f]
seat_ids = []

for line in lines:
    line = line.replace("F", "0")
    line = line.replace("B", "1")
    line = line.replace("R", "1")
    line = line.replace("L", "0")

    row = line[0:7]
    row = int(row, 2)
    seat = line[7:10]
    seat = int(seat, 2)
    seat_id = (row * 8) + seat
    seat_ids.append(seat_id)

seat_ids.sort()

for i in range (len(seat_ids)):
    if seat_ids[i] + 1 != seat_ids[i + 1]:
        print(seat_ids[i] + 1)
        break