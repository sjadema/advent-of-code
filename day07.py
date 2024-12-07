import operator
import re
from typing import List

with open('assets/day07.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

calculations = []
for line in lines:
    match = re.match(r'^(?P<result>\d+): (?P<numbers>.+)$', line)
    calculation = {
        'result': int(match.group('result')),
        'numbers': [int(number) for number in match.group('numbers').split(' ')],
    }

    calculations.append(calculation)


def __to_binary(decimal: int, size: int) -> str:
    return f'{decimal:b}'.rjust(size, '0')


def __to_ternary(decimal: int, size: int) -> str:
    def __to_raw_ternary(n: int) -> str:
        if n == 0:
            return '0'

        remainders = []
        while n:
            n, r = divmod(n, 3)
            remainders.append(str(r))

        return ''.join(reversed(remainders))

    return __to_raw_ternary(decimal).rjust(size, '0')


def __concat_int(a: int, b: int) -> int:
    return int(str(a) + str(b))


operations = [operator.add, operator.mul, __concat_int]


def __has_valid_result(r: int, n_s: List[int], o_s: List[str]) -> bool:
    for o in o_s:
        p_r = n_s[0]

        for i in range(0, len(o)):
            operation = operations[int(o[i])]
            p_r = operation(p_r, n_s[i + 1])

        if p_r == r:
            return True

    return False


valid_results_binary = []
valid_results_ternary = []

for calculation in calculations:
    result = calculation['result']
    numbers = calculation['numbers']
    number_of_operations = len(numbers) - 1

    binary_operations = []
    for b in range(0, 2 ** number_of_operations):
        binary_operations.append(__to_binary(b, number_of_operations))

    if __has_valid_result(result, numbers, binary_operations):
        valid_results_binary.append(result)
        continue

    ternary_operations = []
    for t in range(0, 3 ** number_of_operations):
        ternary_operations.append(__to_ternary(t, number_of_operations))

    if __has_valid_result(result, numbers, ternary_operations):
        valid_results_ternary.append(result)
        continue

print(f'Sum of valid binary results: {sum(valid_results_binary)}')
print(f'Sum of valid ternary results: {sum(valid_results_ternary)}')
print(f'Sum of all valid results: {sum(valid_results_binary) + sum(valid_results_ternary)}')
