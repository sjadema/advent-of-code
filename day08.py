with open('assets/day08.txt', 'r') as file:
    trees = [[int(tree) for tree in line] for line in file.read().splitlines()]

rows, columns = len(trees), len(trees[0])
visible_trees, scenic_trees = [[False] * columns for _ in range(rows)], [[1] * columns for _ in range(rows)]

max_top = max_right = max_bottom = max_left = 0
for y in range(rows):
    for lower in range(columns):
        upper = -1 - lower

        tree_top = trees[lower][y]
        tree_right = trees[y][upper]
        tree_bottom = trees[upper][y]
        tree_left = trees[y][lower]

        # Initialize borders
        if lower == 0:
            max_top, max_right, max_bottom, max_left = tree_top, tree_right, tree_bottom, tree_left

            visible_trees[lower][y] = visible_trees[y][upper] = visible_trees[upper][y] = visible_trees[y][lower] = True
            scenic_trees[lower][y] = scenic_trees[y][upper] = scenic_trees[upper][y] = scenic_trees[y][lower] = 0

            continue

        # Visibility
        if tree_top > max_top:
            visible_trees[lower][y] = True
            max_top = tree_top

        if tree_right > max_right:
            visible_trees[y][upper] = True
            max_right = tree_right

        if tree_bottom > max_bottom:
            visible_trees[upper][y] = True
            max_bottom = tree_bottom

        if tree_left > max_left:
            visible_trees[y][lower] = True
            max_left = tree_left

        # View distance
        view_distance_top = view_distance_right = view_distance_bottom = view_distance_left = 0
        view_distance_top_hit = view_distance_right_hit = view_distance_bottom_hit = view_distance_left_hit = False
        for lower_view in range(lower + 1, columns):
            upper_view = -1 - lower_view

            view_distance_top += 1 if not view_distance_top_hit else 0
            view_distance_right += 1 if not view_distance_right_hit else 0
            view_distance_bottom += 1 if not view_distance_bottom_hit else 0
            view_distance_left += 1 if not view_distance_left_hit else 0

            view_distance_top_hit |= (trees[lower_view][y] >= tree_top)
            view_distance_right_hit |= (trees[y][upper_view] >= tree_right)
            view_distance_bottom_hit |= (trees[upper_view][y] >= tree_bottom)
            view_distance_left_hit |= (trees[y][lower_view] >= tree_left)

            if view_distance_top_hit & view_distance_right_hit & view_distance_bottom_hit & view_distance_left_hit:
                break

        scenic_trees[lower][y] *= view_distance_top
        scenic_trees[y][upper] *= view_distance_right
        scenic_trees[upper][y] *= view_distance_bottom
        scenic_trees[y][lower] *= view_distance_left

print(f'''Number of visible trees: {sum([sum(row) for row in visible_trees])}''')
print(f'''Maximum scenic score: {max([max(row) for row in scenic_trees])}''')
