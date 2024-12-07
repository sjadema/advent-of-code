import copy
from typing import List

with open('assets/day02.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

reports = [[int(level) for level in line.split(' ')] for line in lines]


def __get_directions(report: List[int]) -> List[str]:
    directions = []
    for i in range(0, len(report) - 1):
        a = report[i]
        b = report[i + 1]

        if a < b:
            directions.append('+')
        elif a > b:
            directions.append('-')
        else:
            directions.append('0')

    return directions


def __valid_direction(report: List[int]) -> bool:
    return len(set(__get_directions(report))) == 1


def __get_gaps(report: List[int]) -> List[int]:
    gaps = []
    for i in range(0, len(report) - 1):
        a = report[i]
        b = report[i + 1]

        gaps.append(max(a, b) - min(a, b))

    return gaps


def __valid_gaps(report: List[int]) -> bool:
    valid = 0
    for gap in __get_gaps(report):
        if 1 <= gap <= 3:
            valid += 1

    return valid == len(report) - 1


safe_reports = 0
dampened_reports = 0
for report in reports:
    if __valid_direction(report) and __valid_gaps(report):
        safe_reports += 1
        continue

    for i in range(0, len(report)):
        modified_report = copy.deepcopy(report)
        del modified_report[i]

        if __valid_direction(modified_report) and __valid_gaps(modified_report):
            dampened_reports += 1
            break

print(f'Number of safe reports: {safe_reports}')
print(f'Number of safe reports (with dampening): {safe_reports + dampened_reports}')
