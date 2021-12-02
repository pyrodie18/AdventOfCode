with open('./Day05/D05_Input.txt') as f:
    lines = [line.rstrip() for line in f]
high_seat = 0

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
    if seat_id > high_seat:
        high_seat = seat_id

print(high_seat)