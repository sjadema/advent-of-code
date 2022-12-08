with open('assets/day08.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

trees, visible_trees = [], []
for y in range(len(lines)):
    columns, row = len(lines[y]), []
    for x in range(columns):
        row.append(int(lines[y][x]))

    trees.append(row)
    visible_trees.append([False] * columns)

for i in range(4):
    # Rotate matrix 90 degrees clockwise
    rotated_trees, rotated_visible_trees = [], []
    for x in range(len(trees[0])):
        trees_column, visible_trees_column = [], []
        for y in range(len(trees)):
            trees_column.append(trees[y][x])
            visible_trees_column.append(visible_trees[y][x])

        rotated_trees.append(trees_column[::-1])
        rotated_visible_trees.append(visible_trees_column[::-1])

    # Check tree visibility
    for y in range(len(rotated_trees)):
        max_height = 0
        for x in range(len(rotated_trees[y])):
            tree = rotated_trees[y][x]
            if x == 0:
                rotated_visible_trees[y][x] = True
                max_height = tree

                continue

            if tree > max_height:
                rotated_visible_trees[y][x] = True
                max_height = tree

    trees = rotated_trees
    visible_trees = rotated_visible_trees

number_of_visible_trees = 0
for y in range(len(visible_trees)):
    for x in range(len(visible_trees[y])):
        if visible_trees[y][x]:
            number_of_visible_trees += 1

print(f'''Number of visible trees: {number_of_visible_trees}''')
