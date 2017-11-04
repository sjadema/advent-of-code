file = open('assets/problem1.txt', 'r')
directions = file.read().split(',')
positions = [('n', (0, 0))]

def calculate_position(position, direction, length):
    orientations = ['n', 'e', 's', 'w']
    current_orientation = orientations.index(position[0])

    index = (current_orientation - 1 if direction == 'L' else current_orientation + 1) % len(orientations)

    x = position[1][0]
    y = position[1][1]

    if index == 0:
        y += length
    elif index == 1:
        x += length
    elif index == 2:
        y -= length
    else:
        x -= length

    return (orientations[index], (x, y))


for direction in directions:
    direction = direction.strip()
    length = direction[1:]
    direction = direction[0:1]

    position = calculate_position(positions[-1], direction, int(length))

    positions.append(position)

coordinates = positions[-1][1]

print('Distance is: ', abs(coordinates[0]) + abs(coordinates[1]))

