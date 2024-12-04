import operator
import re
from functools import reduce

with open('assets/day03.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

product = 0
for line in lines:
    matches = re.findall(r'mul\((?P<a>\d{1,3}),(?P<b>\d{1,3})\)', line)
    for match in matches:
        product += reduce(operator.mul, [int(number) for number in match])

print(f'Sum of mul operations: {product}')

product = 0
enabled = True
for line in lines:
    matches = re.findall(r'''(do\(\)|don't\(\))|(mul\((?P<a>\d{1,3}),(?P<b>\d{1,3})\))''', line)

    for match in matches:
        if match[0] == f'''don't()''':
            enabled = False
        elif match[0] == f'do()':
            enabled = True
        else:
            product += int(match[2]) * int(match[3]) * int(enabled)

print(f'Sum of enabled mul operations: {product}')
