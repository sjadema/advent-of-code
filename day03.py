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

print(f'Sum of valid mul operations: {product}')
