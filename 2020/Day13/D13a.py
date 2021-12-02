with open('./Day13/D13_Input.txt') as f:
    lines = [line.rstrip() for line in f]

arrival_time = int(lines[0])
departures = lines[1].split(',')
answer = [arrival_time, 0]

for i in range(len(departures)):
    if departures[i].isnumeric():
        departure = int(departures[i])
        wait_time = (((((arrival_time // departure) * departure) + departure) - arrival_time))
        if wait_time < answer[0]:
            answer = [wait_time,departure]
print(answer[0] * answer[1])
