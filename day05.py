import re

with open('assets/day05.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

starts = []
ends = []

for line in lines:
    match = re.match(r'^(\d+),(\d+) -> (\d+),(\d+)', line)
    starts.append((int(match.group(1)), int(match.group(2))))
    ends.append((int(match.group(3)), int(match.group(4))))

coordinates_hv = []
coordinates_d = []
for i in range(len(starts)):
    start = starts[i]
    end = ends[i]

    x_sign = 1 if start[0] <= end[0] else -1
    y_sign = 1 if start[1] <= end[1] else -1

    x_range = range(start[0], end[0] + x_sign, x_sign)
    y_range = range(start[1], end[1] + y_sign, y_sign)

    if start[0] == end[0] or start[1] == end[1]:
        for x in x_range:
            for y in y_range:
                coordinates_hv.append((x, y))
    else:
        for j in range(len(x_range)):
            x = x_range[j]
            y = y_range[j]

            coordinates_d.append((x, y))

collection = {}
for coordinate in coordinates_hv:
    if coordinate not in collection:
        collection[coordinate] = 0

    collection[coordinate] += 1

overlapping = [coordinate for coordinate, value in collection.items() if 1 < value]
print(f"Number of overlapping coordinates without diagonals: {len(overlapping)}")

for coordinate in coordinates_d:
    if coordinate not in collection:
        collection[coordinate] = 0

    collection[coordinate] += 1

overlapping = [coordinate for coordinate, value in collection.items() if 1 < value]
print(f"Number of overlapping coordinates with diagonals : {len(overlapping)}")
