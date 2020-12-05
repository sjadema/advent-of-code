with open('assets/problem003.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]


def calculate_trees(right: int, down: int) -> int:
    x = right
    y = down
    trees = 0
    while y < len(lines):
        if '#' == lines[y][x % len(lines[y])]:
            trees += 1

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

total_trees = 1
for i in range(0, len(steps)):
    step = steps[i]
    total_trees *= calculate_trees(step[0], step[1])

print('Total number of trees: {}.'.format(total_trees))
