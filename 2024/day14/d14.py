X = 101
Y = 103

def get_data():
    from os import path

    data = []

    with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
        for line in f:
            line = line.strip().split()
            tmp = line[0].split(",")
            tmp2 = line[1].split(",")
            data.append(((int(tmp[0][2:]),int(tmp[1])),(int(tmp2[0][2:]),int(tmp2[1]))))
    return data

def navigate(robot, moves):
    x, y = robot[0]
    vx, vy = robot[1]
    
    xx = (x + (vx * moves)) % X
    yy = (y + (vy * moves)) % Y
    
    return (xx, yy)
        

def part1(data):
    answer = {1: [], 2: [], 3: [], 4: []}
    
    for robot in data:
        xx, yy = navigate(robot, 100)
        if xx < (X // 2) and yy < (Y // 2):
            answer[1].append((xx, yy))
        elif xx < (X // 2) and yy > (Y // 2):
            answer[3].append((xx, yy))
        elif xx > (X // 2) and yy < (Y // 2):
            answer[2].append((xx, yy))
        elif xx > (X // 2) and yy > (Y // 2):
            answer[4].append((xx, yy))
    
    a = 1
    for value in answer.values():
        a *= len(value)
        
    print('Part 1:  {}'.format(str(a)))

def part2(data):
    i = 1
    while True:
        locations = []
        for robot in data:
            locations.append(navigate(robot, i))
        for y in range(Y):
            for x in range(X):
                if ((y, x) in locations and
                    (y + 1, x) in locations and
                    (y + 2, x) in locations and
                    (y + 3, x) in locations and
                    (y + 4, x) in locations and
                    (y, x + 1) in locations and
                    (y, x + 2) in locations and
                    (y, x + 3) in locations and
                    (y, x + 4) in locations ):
                    print('Part 2:  {}'.format(str(i)))
                    return
        i += 1
                
                    

data = get_data()
part1(data)
part2(data)