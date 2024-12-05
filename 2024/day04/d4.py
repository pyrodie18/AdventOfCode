WORD = list("XMAS")

def get_data():
    from os import path

    data = []

    with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
        for line in f:
            line = line.strip()
            data.append(list(line))
    return data

L = (-1,0)
R = (1,0)
U = (0,-1)
D = (0,1)
UL = (-1,-1)
UR = (1,-1)
DL = (-1,1)
DR = (1,1)
SEQUENCES = [L, R, U, D, UL, UR, DL, DR]
 
def find_xmas(grid, x, y):
    total = 0
    
    for sequence in SEQUENCES:
        valid = True
        for i in range(len(WORD)):
            cx = i * sequence[0]
            cy = i * sequence[1]
            if (0<= x + cx < len(grid[0])) and (0 <= y + cy < len(grid)):
                if grid[y + cy][x + cx] != WORD[i]:
                    valid = False
                    break
            else:
                valid = False
                break
        if valid:
            total += 1
    return total
        
def find_x_mas(grid, x, y):
    total = 0
    
    if y < 1 or y > (len(grid) - 2) or x < 1 or x > (len(grid[0]) - 2):
        return 0 
    
    tmp = []
    tmp.append(grid[y - 1][x - 1])
    tmp.append(grid[y + 1][x + 1])
    if (not 'M' in tmp) or (not 'S' in tmp):
        return 0
    
    tmp = []
    tmp.append(grid[y + 1][x - 1])
    tmp.append(grid[y - 1][x + 1])
    if (not 'M' in tmp) or (not 'S' in tmp):
        return 0
    else:
        return 1
        
def part1(data):
    answer = 0
    
    for y, line in enumerate(data):
        indeces = [i for i, y in enumerate(line) if y == "X"]
        for x in indeces:
            answer += find_xmas(data, x, y)
    
    print('Part 1:  {}'.format(str(answer)))

def part2(data):
    answer = 0
    
    for y, line in enumerate(data):
        indeces = [i for i, y in enumerate(line) if y == "A"]
        for x in indeces:
            answer += find_x_mas(data, x, y)
            
    print('Part 2:  {}'.format(str(answer)))

data = get_data()
part1(data)
part2(data)