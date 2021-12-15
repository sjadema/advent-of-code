import copy
import sys

with open('assets/day11.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

octopuses = {}
for y in range(len(lines)):
    for x in range(len(lines)):
        octopuses[(x, y)] = int(lines[y][x])


def count_flashes(steps: int, break_on_synchronized: bool = False) -> int:
    current_octopuses = copy.deepcopy(octopuses)

    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]

    flashes = 0
    for step in range(steps):
        for coordinate in current_octopuses.keys():
            current_octopuses[coordinate] += 1

        flashed = []
        while 0 != len([e for c, e in current_octopuses.items() if 9 < e and c not in flashed]):
            for coordinate in current_octopuses.keys():
                if 9 < current_octopuses[coordinate] and coordinate not in flashed:
                    neighbors = [tuple(c + d for c, d in zip(coordinate, direction)) for direction in directions]
                    for neighbor in neighbors:
                        try:
                            current_octopuses[neighbor] += 1
                        except KeyError:
                            pass

                    flashed.append(coordinate)
                    flashes += 1

        if break_on_synchronized and len(flashed) == len(current_octopuses):
            return step + 1

        for coordinate, energy in current_octopuses.items():
            if 9 < energy:
                current_octopuses[coordinate] = 0

    return flashes


print(f"Number of flashes after 100 steps: {count_flashes(100)}")
print(f"Number of flashes after 100 steps: {count_flashes(sys.maxsize, True)}")
