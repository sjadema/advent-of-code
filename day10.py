import operator

with open('assets/day10.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

grid = {}
for y in range(height := len(lines)):
    line = lines[height - y - 1]
    for x in range(len(line)):
        grid[(x, y)] = line[x]

pipes = {
    '|': [(0, -1), (0, 1)],
    '-': [(-1, 0), (1, 0)],
    'L': [(0, 1), (1, 0)],
    'J': [(0, 1), (-1, 0)],
    '7': [(0, -1), (-1, 0)],
    'F': [(0, -1), (1, 0)],
}

start = list(grid.keys())[list(grid.values()).index('S')]
directions = []
for x in range(max(0, start[0] - 1), min(start[0] + 2, len(lines[0]))):
    for y in range(max(0, start[1] - 1), min(start[1] + 2, len(lines))):

        pipe = grid[point := (x, y)]
        try:
            connections = pipes[pipe]
        except KeyError:
            continue

        for connection in connections:
            if start == tuple(map(operator.add, point, connection)):
                directions.append([start, point])
                break

        if len(directions) == 2:
            break

while directions[0][-1] != directions[1][-1]:
    for direction in directions:
        connections = pipes[grid[point := direction[-1]]]
        for connection in connections:
            next_point = tuple(map(operator.add, point, connection))
            if next_point not in direction:
                direction.append(next_point)

print(f'Steps to farthest point: {len(directions[0]) - 1}')
