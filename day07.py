import operator
import re

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

operations = [operator.add, operator.mul]

valid_results = []
for calculation in calculations:
    result = calculation['result']
    numbers = calculation['numbers']
    number_of_operations = len(numbers) - 1

    possible_operations = []
    for i in range(0, 2 ** number_of_operations):
        possible_operations.append(f'{i:b}'.rjust(number_of_operations, '0'))

    for possible_operation in possible_operations:
        possible_result = numbers[0]
        for i in range(0, len(possible_operation)):
            operation = operations[int(possible_operation[i])]
            possible_result = operation(possible_result, numbers[i + 1])

        if possible_result == result:
            valid_results.append(result)
            break

print(f'Sum of valid results: {sum(valid_results)}')
