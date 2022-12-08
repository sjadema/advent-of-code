with open('assets/day08.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

rows, columns = len(lines), len(lines[0])
visible_trees, scenic_trees = [[False] * columns for _ in range(rows)], [[1] * columns for _ in range(rows)]

trees = []
for y in range(rows):
    row = []
    for x in range(columns):
        row.append(int(lines[y][x]))

    trees.append(row)

for i in range(4):
    # Rotate tree matrices 90 degrees clockwise
    rotated_trees, rotated_visible_trees, rotated_scenic_trees = [], [], []
    for x in range(columns):
        trees_column, visible_trees_column, scenic_trees_column = [], [], []
        for y in range(rows):
            trees_column.append(trees[y][x])
            visible_trees_column.append(visible_trees[y][x])
            scenic_trees_column.append(scenic_trees[y][x])

        rotated_trees.append(trees_column[::-1])
        rotated_visible_trees.append(visible_trees_column[::-1])
        rotated_scenic_trees.append(scenic_trees_column[::-1])

    # Calculate tree visibility and scenic score
    for y in range(rows):
        max_height = 0
        for x in range(columns):
            tree = rotated_trees[y][x]

            # First column
            if x == 0:
                max_height = tree

                rotated_visible_trees[y][x] = True
                rotated_scenic_trees[y][x] = 0

                continue

            # Visibility
            if tree > max_height:
                rotated_visible_trees[y][x] = True
                max_height = tree

            # View distance
            view_distance = 0
            for view_x in range(min(x + 1, columns), columns):
                view_distance += 1

                if rotated_trees[y][view_x] >= tree:
                    break

            rotated_scenic_trees[y][x] *= view_distance

    trees = rotated_trees
    visible_trees = rotated_visible_trees
    scenic_trees = rotated_scenic_trees

print(f'''Number of visible trees: {sum([sum(row) for row in visible_trees])}''')
print(f'''Maximum scenic score: {max([max(row) for row in scenic_trees])}''')
