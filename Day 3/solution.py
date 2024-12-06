import re
from faulthandler import is_enabled

with open('input.txt', 'r') as file: # Another way to open file
    data = file.read()

def part1():
    pattern = r"mul\(\d+,\d+\)" # r means raw string for \ characters
    matches = re.findall(pattern, data)

    total = 0

    for match in matches:
        num1, num2 = get_numbers(match)
        total += num1 * num2

    print(total)

def part2():
    pattern = r"do\(\)|don't\(\)|mul\(\d+,\d+\)" # Pattern to match "do()", "don't()", or "mul(x, y)"
    matches = re.findall(pattern, data)

    total = 0
    enable = True

    for match in matches:
        if match == "do()":
            enable = True
        elif match == "don't()":
            enable = False
        elif match.startswith("mul") and enable:
            num1, num2 = get_numbers(match)
            total += num1 * num2

    print(total)

def get_numbers(case):
    numbers = re.findall(r"\d+", case)
    return int(numbers[0]), int(numbers[1])

part1()
part2()