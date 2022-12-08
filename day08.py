with open('assets/day08.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

trees = []
for y in range(len(lines)):
    row = []
    for x in range(len(lines[y])):
        row.append(int(lines[y][x]))

    trees.append(row)

