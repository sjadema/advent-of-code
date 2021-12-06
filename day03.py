import operator
from typing import Callable

with open('assets/day03.txt', 'r') as file:
    numbers = [line for line in file.read().splitlines()]

number_of_rows = len(numbers)
number_of_cols = len(numbers[0])

rows = [[] for i in range(number_of_rows)]
columns = [[] for j in range(number_of_cols)]
for i in range(number_of_rows):
    for j in range(number_of_cols):
        rows[i].append(int(numbers[i][j]))
        columns[j].append(int(numbers[i][j]))

gamma_list = [1 if column > number_of_rows / 2 else 0 for column in [sum(column) for column in columns]]
epsilon_list = [1 - i for i in gamma_list]
gamma = ''.join([str(i) for i in gamma_list])
epsilon = ''.join([str(i) for i in epsilon_list])

print(f"Power consumption: {int(gamma, 2) * int(epsilon, 2)}")

def calculate_rating(comparator: Callable) -> str:
    report = [[bit for bit in row] for row in rows]

    for i in range(number_of_cols):
        rating_column = []
        for row in report:
            rating_column.append(row[i])

        rating_bit = 1 if comparator(sum(rating_column), len(report) / 2) else 0

        filtered_report = []
        for row in report:
            if row[i] == rating_bit:
                filtered_report.append(row)

        report = filtered_report
        if 1 == len(report):
            return ''.join([str(bit) for bit in report[0]])

print(f"Life support rating: {int(calculate_rating(operator.ge), 2) * int(calculate_rating(operator.lt), 2)}")
