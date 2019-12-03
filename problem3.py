import re

with open('assets/problem3.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

fabric = [['.'] * 1000 for i in range(1001)]

operations = []
for line in lines:
    match = re.search('^#(?P<id>[^\s]+)\s@\s(?P<left>[\d]+),(?P<top>[\d]+):\s(?P<width>[\d]+)x(?P<height>[\d]+)', line)

    box_id = match.group('id')
    left = int(match.group('left'))
    top = int(match.group('top'))
    width = int(match.group('width'))
    height = int(match.group('height'))

    operation = {
        'id': box_id,
        'left': left,
        'top': top,
        'width': width,
        'height': height,
    }

    operations.append(operation)

collisions = set()
for operation in operations:
    for i in range(operation['left'], operation['left'] + operation['width']):
        for j in range(operation['top'], operation['top'] + operation['height']):
            if fabric[i][j] == 'x':
                collisions.add((i, j))

            fabric[i][j] = 'x'

print('Amount of collisions: {}'.format(len(collisions)))

for operation in operations:
    collision = 0
    for i in range(operation['left'], operation['left'] + operation['width']):
        if collision < 0:
            break

        for j in range(operation['top'], operation['top'] + operation['height']):
            if (i, j) in collisions:
                collision += 1
                break

    if collision == 0:
        print('Free fabric has ID: {}'.format(operation['id']))
