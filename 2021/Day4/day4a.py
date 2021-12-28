import os
input = []
numbers = []

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), "r") as f:
    for line in f:
        input.append(line.strip())

tmp = input[0].split(',')
for i in tmp:
    numbers.append(int(i))

boards = []
tmp = []
for line in input[2:]:
    if line == '':
        boards.append(tmp)
        tmp = []
    else:
        line = line.split()
        for i in line:
            tmp.append(int(i))
boards.append(tmp)

def check_board(board) -> bool:
    patterns = [
        # [0, 6, 12, 18, 24], 
        # [4, 8, 12, 16, 20],
        [0, 1, 2, 3, 4],
        [5, 6, 7, 8, 9],
        [10, 11, 12, 13, 14],
        [15, 16, 17, 18, 19],
        [20, 21, 22, 23, 24],
        [0, 5, 10, 15, 20],
        [1, 6, 11, 16, 21],
        [2, 7, 12, 17, 22],
        [3, 8, 13, 18, 23],
        [4, 9, 14, 19, 24]    
    ]
    for direction in patterns:
        total = 0
        for i in direction:
            if board[i] != 100:
                break
            else:
                total += board[i]
        if total == 500:
            return True
    return False

def get_score(board) -> int:
    for i, number in enumerate(numbers):
        try:
            index = board.index(number)
            board[index] = 100
            if check_board(board):
                score = 0
                for j in board:
                    if j != 100:
                        score += j
                return (i, score * number)
        except:
            continue

    return (100, 0)


low_move_count = 0
low_score = 0

for board in boards:
    results = get_score(board)
    if results[0] > low_move_count:
        low_move_count = results[0]
        low_score = results[1]

print(low_score)