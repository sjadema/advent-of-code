from util.line import Line

file = open('assets/problem1.txt', 'r')
steps = file.read().split(',')

directions = (
    (0, 1),   # N
    (1, 0),   # E
    (0, -1),  # S
    (-1, 0),  # W
)

# Create starting direction (N) and position (0, 0)
positions = [(0, (0, 0))]

for step in steps:
    step = step.strip()
    turn = step[0:1]
    length = int(step[1:])

    direction = positions[-1][0]
    coordinates = positions[-1][1]

    # Calculate new direction and create a new position
    index = (direction - 1 if turn == 'L' else direction + 1) % len(directions)
    positions.append(
        (index, (coordinates[0] + directions[index][0] * length, coordinates[1] + directions[index][1] * length))
    )

coordinates = positions[-1][1]
print('Distance single is: ', abs(coordinates[0]) + abs(coordinates[1]))

lines = []
for index in range(1, len(positions)):
    lines.append(Line(positions[index - 1][1], positions[index][1]))

for index in range(0, len(lines)):
    # Skip touching line, start at index + 2
    for compare in range(index + 2, len(lines)):
        coordinates = lines[compare].has_intersection(lines[index])
        if coordinates is not None:
            print('Distance visited is: ', int(abs(coordinates[0]) + abs(coordinates[1])))
            exit(0)

