import copy
from typing import List

with open('assets/day13.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

coordinates = []
instructions = []
for line in lines:
    if not len(line):
        continue

    if line[0].isnumeric():
        x, y = map(int, line.split(','))
        coordinates.append((x, y))

    else:
        parts = line.split(' ')[-1].split('=')
        instructions.append((parts[0], int(parts[1])))


def fold(current_instructions: List[tuple]) -> List[tuple]:
    current_coordinates = copy.deepcopy(coordinates)

    for instruction in current_instructions:
        direction, crease = instruction

        current_coordinates = list(current_coordinates)
        for i in range(len(current_coordinates)):
            x, y = coordinate = current_coordinates[i]
            if 'x' == direction and crease < x:
                amount = (x - crease) * 2
                coordinate = (x - amount, y)
            if 'y' == direction and crease < y:
                amount = (y - crease) * 2
                coordinate = (x, y - amount)

            current_coordinates[i] = coordinate

        current_coordinates = set(current_coordinates)

    return list(current_coordinates)


print(f"Number of dots after first fold: {len(fold(instructions[0:1]))}")
code_coordinates = fold(instructions)
max_x = max([x for x, y in code_coordinates])
max_y = max([y for x, y in code_coordinates])

print("Code after folding:")
for y in range(max_y + 1):
    line = ''
    for x in range(max_x + 1):
        line += '.' if (x, y) in code_coordinates else ' '

    print(line)
