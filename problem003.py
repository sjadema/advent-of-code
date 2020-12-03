import math

with open('assets/problem003.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

fraction = 3 / 1
multiplier = math.ceil(len(lines) * fraction / len(lines[0]))

grid = []
for y in range(0, len(lines)):
    grid.append([])
    for x in (lines[y] * multiplier):
        grid[y].append(x)

x = y = 0
trees = 0
while True:
    y += 1
    x += 3

    try:
        if '#' == grid[y][x]:
            trees += 1
    except IndexError:
        break

print('Number of trees: {}.'.format(trees))
