starting_nums = [2,15,0,9,1,20]

sequence = []

def get_index_positions(list_of_elems, element):
    index_pos_list = []
    index_pos = 0
    while True:
        try:
            index_pos = list_of_elems.index(element, index_pos)
            index_pos_list.append(index_pos)
            index_pos += 1
        except ValueError as e:
            break
    return index_pos_list

for i in starting_nums:
    sequence.append(i)

for i in range(len(starting_nums), 30000000):
    current_num = sequence[i-1]
    positions = get_index_positions(sequence, current_num)
    if len(positions) > 1:
        distance = (i - positions[-2]) - 1
    else:
        distance = 0
    sequence.append(distance)

print(sequence[-1])