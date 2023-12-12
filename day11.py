import operator

with open('assets/day11.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

universe = []

# Expand horizontal
y = 0
while y < len(lines):
    line = lines[y]

    universe.append(line)
    if set(list(line)) == {'.'}:
        universe.append(line)

    y += 1

# Expand vertical
x, offset = 0, 0
while x < len(lines[0]):
    line = [line[x] for line in lines]

    if set(line) == {'.'}:
        for i in range(len(universe)):
            row = list(universe[i])
            row.insert(x + offset, '.')

            universe[i] = ''.join(row)

        offset += 1

    x += 1

galaxies = []
for y in range(height := len(universe)):
    row = universe[height - y - 1]
    for x in range(len(row)):
        if row[x] == '#':
            galaxies.append((x, y))

distances = 0
for i in range(len(galaxies)):
    for j in range(i, len(galaxies)):
        distance = tuple(map(operator.sub, galaxies[i], galaxies[j]))
        distances += abs(distance[0]) + abs(distance[1])

print(f'Sum of shortest paths: {distances}')
