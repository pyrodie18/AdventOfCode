from collections import defaultdict

def get_data():
    from os import path

    data = []

    with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
        for line in f:
            data = line.strip().split()
    return data

def blink(stone):
    if stone == "0":
        return ["1"]
    elif len(stone) % 2 == 0:
        mid_number = len(stone) // 2
        return [str(int(stone[:mid_number])), str(int(stone[mid_number:]))]
    else:
        return [str(int(stone) * 2024)]
                       
def blinking(tmp_stones, blinks):
    stones = defaultdict(int)
    
    for stone in tmp_stones:
        stones[stone] += 1
        
    for i in range(blinks):
        new_stones = defaultdict(int)
        for stone in stones.keys():
            ans = blink(stone)
            for a_stone in ans:
                new_stones[a_stone] += stones[stone]
        stones = new_stones
        
    return sum(stones.values())

def part1(data):
    answer = blinking(data, 25)
       
    print('Part 1:  {}'.format(str(answer)))

def part2(data):
    answer = blinking(data, 75)
       
    print('Part 2:  {}'.format(str(answer)))

data = get_data()
# part1(data)
part2(data)
