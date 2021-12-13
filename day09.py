with open('assets/day09.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

depths = [[9] + [int(d) for d in line] + [9] for line in lines]
depths = [[9] * len(depths[0])] + depths + [[9] *  len(depths[0])]

minimums = []
for y in range(1, len(depths) - 1):
    for x in range(1, len(depths[y]) - 1):
        depth = depths[y][x]
        minimum_depth = min(depths[y - 1][x], depths[y + 1][x], depths[y][x - 1], depths[y][x + 1])
        if depth < minimum_depth:
            minimums.append(depth)

print(f"Minimum risk level: {sum(minimums) + len(minimums)}")
