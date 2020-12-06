from functools import reduce

with open('assets/problem003.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]


def calculate_trees(right: int, down: int) -> int:
    x = right
    y = down
    trees = 0
    while y < len(lines):
        trees += int('#' == lines[y][x % len(lines[y])])

        y += down
        x += right

    return trees


print('Number of trees: {}.'.format(calculate_trees(3, 1)))

steps = [
    [1, 1],
    [3, 1],
    [5, 1],
    [7, 1],
    [1, 2],
]

print('Total number of trees: {}.'.format(reduce(lambda t, s: t * calculate_trees(s[0], s[1]), steps, 1)))
