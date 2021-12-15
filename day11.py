with open('assets/day11.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

octopuses = {}
for y in range(len(lines)):
    for x in range(len(lines)):
        octopuses[(x, y)] = int(lines[y][x])


def count_flashes(steps: int) -> int:
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]

    flashes = 0
    for step in range(steps):
        for coordinate in octopuses.keys():
            octopuses[coordinate] += 1

        flashed = []
        while 0 != len([e for c, e in octopuses.items() if 9 < e and c not in flashed]):
            for coordinate in octopuses.keys():
                if 9 < octopuses[coordinate] and coordinate not in flashed:
                    neighbors = [tuple(c + d for c, d in zip(coordinate, direction)) for direction in directions]
                    for neighbor in neighbors:
                        try:
                            octopuses[neighbor] += 1
                        except KeyError:
                            pass

                    flashed.append(coordinate)
                    flashes += 1

        for coordinate, energy in octopuses.items():
            if 9 < energy:
                octopuses[coordinate] = 0

    return flashes


print(f"Number of flashes after 100 steps: {count_flashes(100)}")
