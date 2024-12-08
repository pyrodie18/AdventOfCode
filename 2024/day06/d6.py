def get_data():
    from os import path

    data = []

    with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
        for line in f:
            data.append(list(line.strip()))
    return data

def find_start(grid):
    for i, row in enumerate(grid):
        if "^" in row:
            return (row.index("^"), i)
        
def move_north(grid, cord):
    moves = []
    x, y = cord
    while y >= 0:
        if grid[y][x] == "#":
            return moves, (x, y + 1), "east"
        else:
            moves.append((x,y))
        y -= 1
    return moves, (x, y), "finish"

def move_east(grid, cord):
    moves = [cord]
    x, y = cord
    while x <= len(grid[y]) - 1:
        if grid[y][x] == "#":
            return moves, (x - 1, y), "south"
        else:
            moves.append((x,y))
        x += 1
    return moves, (x, y), "finish"

def move_south(grid, cord):
    moves = [cord]
    x, y = cord
    while y <= len(grid) - 1:
        if grid[y][x] == "#":
            return moves, (x, y - 1), "west"
        else:
            moves.append((x,y))
        y += 1
    return moves, (x, y), "finish"

def move_west(grid, cord):
    moves = [cord]
    x, y = cord
    while x >= 0:
        if grid[y][x] == "#":
            return moves, (x + 1, y), "north"
        else:
            moves.append((x,y))
        x -= 1
    return moves, (x, y), "finish"

def check_loop(history, recent):
    thistory = set(history)
    trecent = set(recent)
    repeat = thistory.intersection(trecent)
    
    return len(repeat) > 0

def navigate (grid, loop_check = False):
    answer = []
    history = {
        "north": [],
        "south": [],
        "east": [],
        "west": []
    }
    
    cord = find_start(grid)
    dir = "north"
    
    while True:
        if dir == "north":
            moves, cord, next_dir = move_north(grid, cord)          
        elif dir == "south":
            moves, cord, next_dir = move_south(grid, cord)
        elif dir == "east":
            moves, cord, next_dir = move_east(grid, cord)
        elif dir == "west":
            moves, cord, next_dir = move_west(grid, cord)
        
        if loop_check and check_loop(history[dir], moves):
            return True
        
        history[dir] += moves
        dir = next_dir
        
        if dir == "finish":
            break
        
    for i in history.keys():
        answer += history[i]
    if loop_check:
        return False
    else:
        return answer


def part1(grid):   
    answer = navigate(grid, False)
    answer = len(set(answer))
    print('Part 1:  {}'.format(str(answer)))

def part2(grid):
    answer = 0
    move_list = set(navigate(grid, False))
    start = find_start(grid)
    move_list.discard(start)
    
    for test_cor in move_list:
        x, y = test_cor
        grid[y][x] = "#"
        if navigate(grid, True):
            answer += 1
        grid[y][x] = "."

    print('Part 2:  {}'.format(str(answer)))

data = get_data()
# part1(data)
part2(data)