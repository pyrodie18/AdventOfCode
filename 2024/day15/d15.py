def get_data():
    from os import path
    moves = ""
    data = []
    

    with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
        lines = f.read()
        lines = lines.split("\n\n")
        grid = lines[0].split("\n")
        for line in grid:
            line = list(line.strip())
            data.append(line)
            
        tmp_moves = lines[1].split("\n")
        for line in tmp_moves:
            line = line.strip()
            moves += line
        
    return data, moves

def find_start(grid):
    for i, row in enumerate(grid):
        if "@" in row:
            return (row.index("@"), i)
        
def get_next_location(direction):
    if direction == "^":
        return (0, -1)
    elif direction == "v":
        return (0, 1)
    elif direction == ">":
        return (1, 0)
    else:
        return (-1, 0)
    
def push_box(location, grid, direction):
    found = False
    x, y = location
    nx, ny = get_next_location(direction)
    xx = x + nx
    yy = y +ny
    while yy in range(len(grid)) and xx in range(len(grid[0])):
        if grid[yy][xx] == ".":
            found = True
            break
        elif grid[yy][xx] == "#":
            break
        else:
            xx += nx
            yy += ny
    if found:
        grid[yy][xx], grid[y][x] = grid[y][x], grid[yy][xx]
        return True, grid
    else:
        return False, grid

def score(grid):
    score = 0
    for y, line in enumerate(grid):
        for x, val in enumerate(line):
            if val == "O":
                score += ((100 * y) + x)
    return score

def modify_grid(grid):
    new_grid = []
    new_line = []
    
    for y, line in enumerate(grid):
        for x, val in enumerate(line):
            if val == "#":
                new_line += ["#","#"]
            elif val == "O":
                new_line += ["[","]"]
            elif val == ".":
                new_line += [".","."]
            elif val == "@":
                new_line += ["@","."]
        new_grid.append(new_line)
        new_line = []
        
    return new_grid

def part1(grid, moves, start_loc):
    answer = None
    x, y = start_loc
    
    for i in moves:
        nx, ny = get_next_location(i)
        xx = x + nx
        yy = y + ny
        if grid[yy][xx] == "O":
            success, grid = push_box((xx, yy), grid, i)
            if success:
                x, y = xx, yy
        elif grid[yy][xx] == "#":
            continue
        else:
            x, y = xx, yy
    
    answer = score(grid)
    
    print('Part 1:  {}'.format(str(answer)))

def part2(grid, moves):
    grid = modify_grid(grid)
    x, y = find_start(grid)
    
    for i in moves:
        nx, ny = get_next_location(i)
        xx = x + nx
        yy = y + ny
        if grid[yy][xx] == "[" or grid[yy][xx] == "]":
            success, grid = push_box((xx, yy), grid, i)
            if success:
                x, y = xx, yy
        elif grid[yy][xx] == "#":
            continue
        else:
            x, y = xx, yy
    
    answer = score(grid)
    answer = None
    # print('Part 2:  {}'.format(str(answer)))

grid, moves = get_data()
start_loc = find_start(grid)
# part1(grid, moves, start_loc)
part2(grid, moves)