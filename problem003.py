import math

with open('assets/problem003.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]


def calculate_trees(right: int, down: int) -> int:
    fraction = right / down
    multiplier = math.ceil(len(lines) * fraction / len(lines[0]))

    grid = []
    for y in range(0, len(lines)):
        grid.append([])
        for x in (lines[y] * multiplier):
            grid[y].append(x)

    x = y = 0
    trees = 0
    while True:
        y += down
        x += right

        try:
            if '#' == grid[y][x]:
                trees += 1
        except IndexError:
            break

    return trees


print('Number of trees: {}.'.format(calculate_trees(3, 1)))

steps = [
    [1, 1],
    [3, 1],
    [5, 1],
    [7, 1],
    [1, 2],
]

for i in range(0, len(steps)):
    step = steps[i]
    steps[i] = calculate_trees(step[0], step[1])

print('Total number of trees: {}.'.format(math.prod(steps)))
