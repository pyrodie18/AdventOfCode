from collections import defaultdict


def get_input():
    from os import path

    with open(path.join(path.dirname(__file__), "input.txt"), "r") as f:
        # Change to my normal input method, this time breaking it up into
        # groups of lines that all relate around a single command, based
        # on code from
        # https://github.com/womogenes/AoC-2022-Solutions/blob/main/day_07/day_07_p1.py
        input = ("\n" + f.read().strip()).split("\n$ ")[1:]
    return input


def parse_blocks(input):
    dir_sizes = defaultdict(int)
    stack = []

    for block in input:
        # Break the block of lines into individual lines
        lines = block.split("\n")
        cmd = lines[0]
        outputs = lines[1:]

        # Breakout the parts of the command
        cmd_parts = cmd.split()
        if cmd_parts[0] == "cd":
            if cmd_parts[1] == "/":
                stack = ["/"]
            elif cmd_parts[1] == "..":
                stack.pop()
            else:
                stack.append(cmd_parts[1])

        # Parse the outputs of the command
        for line in outputs:
            if line[0].isdigit():
                file_size = int(line.split()[0])
                # Cycle through the current and all
                # parent directories and add the file sizes
                for i in range(len(stack)):
                    the_dir_parts = stack[: i + 1]
                    the_dir = "/".join(the_dir_parts)
                    dir_sizes[the_dir] += file_size

    return dir_sizes


def part1(input):
    total = 0
    dir_structure = parse_blocks(input)
    # Find all directories smaller than 100,000
    for key in dir_structure.keys():
        if dir_structure[key] <= 100000:
            total += dir_structure[key]
    print("Part 1:  " + str(total))
    return dir_structure


def part2(dir_structure):
    # Figure out how much more space is needed
    current_size = dir_structure["/"]
    free_space = 70000000 - current_size
    gap = 30000000 - free_space
    available_size = []

    # Find the smallest directory that meets the need
    for key in dir_structure.keys():
        if dir_structure[key] >= gap:
            available_size.append(dir_structure[key])
    print("Part 2:  " + str(min(available_size)))


input = get_input()
dir_structure = part1(input)
part2(dir_structure)
