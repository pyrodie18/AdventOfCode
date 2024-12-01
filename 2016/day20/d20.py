import numpy as np

def get_data():
    from os import path

    data = []

    with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
        for line in f:
            data.append(line.strip().split('-'))
    
    data = np.array(data, dtype=np.uint32)
    return data

def summarize_ranges(data):
    the_data = data
    the_data.sort(axis=0)
    i = 0
    while i + 1 < len(the_data):
        # Check to see if next element starts within and ends pass the current end
        if the_data[i][0] < the_data[i + 1][0] < the_data[i][1]:
            if the_data[i + 1][1] > the_data[i][1]:
                the_data[i][1] = the_data[i + 1][1]
                the_data = np.delete(the_data, i + 1, 0)
        # Continious Sequence
        elif the_data[i][1] + 1 == the_data[i + 1][0]:
            the_data[i][1] = the_data[i + 1][1]
            the_data = np.delete(the_data, i + 1, 0)
        else:
            i += 1
    return the_data
    

def part1(data):
    print('Part 1:  {}'.format(str(data[0][1] + 1)))

def part2(data):
    answer = 0
    for i in range(len(data) - 1):
        answer += int((data[i + 1][0] - (data[i][1] + 1)))
    print('Part 2:  {}'.format(str(answer)))

data = get_data()
sum_data = summarize_ranges(data)
part1(sum_data)
part2(sum_data)