from typing import overload, Literal, Tuple

def get_data():
    from os import path

    data = []

    with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
        for line in f:
            data.append(line.strip())
    return data

def figure_mod(pos: int, move: int, direction: str):
    """
    Rotate the dial n spaces left or right and retun the updated position

    Args:
        pos (int): The starting number of the dial.
        move (int): The number of places to turn the dial.
        direction (str): The direction to turn

    Returns:
        int: The number of times 0 had been passed over
    """    
    zeros = 0
    current_pos = pos
    if direction == "L":
        for _ in range(move):
            current_pos -= 1
            if current_pos == 0:
                zeros += 1
            elif current_pos < 0:
                current_pos = 99
    else:
        for _ in range(move):
            current_pos += 1
            if current_pos == 100:
                zeros += 1
                current_pos = 0
    return zeros

@overload
def turn(pos: int, instruction: str, mod: Literal[False] = False) -> int:
    ...

@overload
def turn(pos: int, instruction: str, mod: Literal[True] = True) -> Tuple[int, int]:
    ...   

def turn (pos: int, instruction: str, mod=False):
    """
   Complete a single turn of the dial

    Args:
        pos (int): The current starting position of the dail
        instruction (str): The combined direction (R or L) along with the number of spaces to move.
        mod (bool, optional): 
            When TRUE:  Count the total number of times 0 is passed over.
            When FALSE:  Return the new position

    Returns:
        if mod = False
            int: The current updated position of the dial
        if mode = True
            tuple (int, int): The current updated position of the dial and the number of times
            that 0 has been passsed over.
    """
    direction = instruction[0]
    spaces = int(instruction[1:])
    
    if direction == "L":
        new_pos = (pos - (spaces % 100))
        if new_pos < 0:
            new_pos = 100 + new_pos
    else:
        new_pos = pos + spaces
        new_pos =  new_pos % 100
        
    if mod:
        return new_pos, figure_mod(pos, spaces, direction)
    else:
        return new_pos

def part1(data):
    answer = 0
    pos = 50
    
    for instruction in data:
        pos = turn(pos, instruction)
        if pos == 0:
            answer += 1
    
    print('Part 1:  {}'.format(str(answer)))

def part2(data):
    answer = 0
    pos = 50
    
    for instruction in data:
        pos, zeros = turn(pos, instruction, True)
        answer += zeros
    
    print('Part 2:  {}'.format(str(answer)))

data = get_data()
# part1(data)
part2(data)