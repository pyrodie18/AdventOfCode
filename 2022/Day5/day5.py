import os
from collections import deque
import cProfile


def prepare():
    input = []
    tmp_stack = []
    with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as f:
        for line in f:
            if "move" in line:
                input.append(line.strip().split())
            elif "[" in line:
                tmp_stack.append(line)
    return input, tmp_stack


def build_stack(tmp_stack):
    stack = [
        deque(),
        deque(),
        deque(),
        deque(),
        deque(),
        deque(),
        deque(),
        deque(),
        deque(),
        deque(),
    ]
    tmp_stack.reverse()
    for line in tmp_stack:
        j = 0
        for i in range(1, len(line), 4):
            j += 1
            if line[i].isupper():
                stack[j].append(line[i])

    return stack


def get_move(line):
    cnt = int(line[1])
    frm = int(line[3])
    to = int(line[5])
    return cnt, frm, to


def move(input, stack, multi):
    for line in input:
        if multi:
            tmp = deque()
        cnt, frm, to = get_move(line)
        for i in range(cnt):
            if not multi:
                stack[to].append(stack[frm].pop())
            else:
                tmp.append(stack[frm].pop())
        if multi:
            for i in range(len(tmp)):
                stack[to].append(tmp.pop())

    answer = ""
    for i in range(1, len(stack)):
        try:
            answer = answer + stack[i].pop()
        except:
            continue
    return answer


input, tmp_stack = prepare()
print("Part 1:  " + str(move(input, build_stack(tmp_stack), False)))
print("Part 2:  " + str(move(input, build_stack(tmp_stack), True)))
