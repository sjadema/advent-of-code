from math import sqrt, ceil

target_square = 265149
dimension = ceil(sqrt(target_square))
if dimension % 2 == 0:
    dimension += 1

radius = int((dimension - 1) / 2)
radius_previous = radius - 1

current_square = (dimension - 2) ** 2 + 1
current_position = (radius, radius_previous * -1)
while current_square < target_square:
    x = current_position[0]
    y = current_position[1]

    if x == radius and y < radius:
        # fill right
        y += 1
    elif x > radius * -1 and y == radius:
        # fill top
        x -= 1
    elif x == radius * -1 and y > radius * -1:
        # fill left
        y -= 1
    elif x < radius and y == radius * -1:
        # fill bottom
        x += 1

    current_position = (x, y)
    current_square += 1

distance = abs(current_position[0]) + abs(current_position[1])
if target_square == 1:
    distance = 0

print('Distance: ', distance)

dimension = 3
radius = int((dimension - 1) / 2)

current_position = (radius, radius * -1)

coordinates = {
    (0, 0): 1
}

possibilities = (
    (1, 0),
    (1, 1),
    (0, 1),
    (-1, 1),
    (-1, 0),
    (-1, -1),
    (0, -1),
    (1, -1)
)

maximum_value = sorted(coordinates.values())[-1]
steps = dimension ** 2 - (dimension - 2) ** 2
step = 0
while maximum_value <= target_square:
    x = current_position[0]
    y = current_position[1]

    if step == steps:
        # add row
        radius += 1
        x += 1
        steps = (radius * 2 + 1) ** 2 - ((radius * 2 + 1) - 2) ** 2
        step = 0
    elif x == radius and y < radius:
        # fill right
        y += 1
    elif x > radius * -1 and y == radius:
        # fill top
        x -= 1
    elif x == radius * -1 and y > radius * -1:
        # fill left
        y -= 1
    elif x < radius and y == radius * -1:
        # fill bottom
        x += 1

    current_position = (x, y)

    total = 0
    for possibility in possibilities:
        try:
            total += coordinates[(x + possibility[0], y + possibility[1])]

        except KeyError:
            continue

    coordinates[current_position] = total
    maximum_value = total
    step += 1

print('Stress test: ', sorted(coordinates.values())[-1])
