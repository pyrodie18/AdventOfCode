from typing import Tuple

def get_data():
    from os import path

    data = []

    with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
        for line in f:
            line = line.strip()
            the_line = []
            for i in line:
                the_line.append(int(i))
            data.append(the_line)
    return data

def rindex(alist: list[int], value: int) -> int:
    """
    Determine the right most index number of a value in a list

    Args:
        alist (list[int]): A list of integers
        value (int): The value to find the right index for

    Returns:
        int: The index number of the right most instance of the value
    """
    return len(alist) - alist[-1::-1].index(value) -1

def reverse_sort(line: list[int]) -> list[int]:
    """
    Reverse sorted list of unique integers (high -> low)

    Args:
        alist (list[int]): A list of integers to sort

    Returns:
        list[int]: A sorted list of integers
    """
    values = list(set(line))
    return sorted(values, reverse=True)

def find_max(line: list[int]) -> int:
    """
    Determine the largest two digit number possible using a list of integers

    Args:
        line (list[int]): A list of integers

    Returns:
        int: The largest number possible using two numbers (in order) from the list
    """
    sorted_values = reverse_sort(line)
    for i in sorted_values:
        for j in sorted_values:
            if line.index(i) < rindex(line, j):
                return int(f"{i}{j}")

def find_next_max(line: list[int], size: int) -> Tuple[int, list[int]]:
    """
    The function gets called repeatedly to determine the next largest number available
    within the required size.  If the high number is found, but its location is to far
    to allow for sufficient digits, it continues to the next lowest.

    Args:
        line (list[int]): A list of integers
        size (int): How many digits are remaining in the desired number

    Returns:
        Tuple[int, list[int]]: The highest available number from the input and the
        remainder of the unused numbers
    """
    sorted_values = reverse_sort(line)
    length = len(line)
    for i in sorted_values:
        if length - line.index(i) >= size:
            return i, line[line.index(i) + 1:]

def find_mega_max(line: list[int], size: int = 12) -> int:
    """
    Find a multi digit max number of abritrary size from a list of digits

    Args:
        line (list[int]): A list of integers
        size (int, optional): The required size of the number (defaults to 12)

    Returns:
        int: The largest possible number
    """
    max_value = []
    remaining = size
    remaining_line = line
    while remaining > 0:
        value, remaining_line = find_next_max(remaining_line, remaining)
        max_value.append(value)
        remaining -= 1
        
    return int(''.join(f"{i}" for i in max_value))

def part1(data):
    answer = 0
    for line in data:
        answer += find_max(line)
    
    print('Part 1:  {}'.format(str(answer)))

def part2(data):
    answer = 0
    for line in data:
        answer += find_mega_max(line)
        
    print('Part 2:  {}'.format(str(answer)))

data = get_data()
part1(data)
part2(data)