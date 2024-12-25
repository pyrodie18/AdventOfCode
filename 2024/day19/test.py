#!/bin/python3

import sys
from typing import List
from functools import cache
from os import path

sys.setrecursionlimit(100000)
FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"


def read_lines_to_list() -> List[str]:
    lines: List[str] = []
    with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
        for line in f:
            line = line.strip()
            lines.append(line)

    return lines


@cache
def possible(design: str, patterns: frozenset[str]) -> bool:
    # print(design)
    if design == "":
        return True

    return any(
        (
            possible(design[len(pattern) :], patterns)
            if design.startswith(pattern)
            else False
        )
        for pattern in patterns
    )


def part_one():
    lines = read_lines_to_list()
    answer = 0

    patterns = lines[0].split(", ")
    designs = []

    for line in lines[2:]:
        if len(line.strip()) > 0:
            designs.append(line)

    patterns = frozenset(patterns)
    for design in designs:
        if possible(design, patterns):
            answer += 1
            print(design)
            
        # else:
            # print (design)

    print(f"Part 1: {answer}")


@cache
def possible_two(design: str, patterns: frozenset[str]) -> int:
    if design == "":
        return 1

    result = 0
    for pattern in patterns:
        if design.startswith(pattern):
            result += possible_two(design[len(pattern) :], patterns)

    return result


def part_two():
    lines = read_lines_to_list()
    answer = 0

    patterns = lines[0].split(", ")
    designs = []

    for line in lines[2:]:
        if len(line.strip()) > 0:
            designs.append(line)

    patterns = frozenset(patterns)
    for design in designs:
        results = possible_two(design, patterns)
        answer += results

    print(f"Part 2: {answer}")


part_one()
part_two()
