with open('assets/problem003.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

wired = []
wires = [line.split(',') for line in lines]
for wire in wires:
    y = x = 0
    coordinates = [(0, 0)]

    for instruction in wire:
        coordinates.pop()

        direction = instruction[0:1]
        amount = int(instruction[1:])

        x_args = (x, x + 1)
        y_args = (y, y + 1)

        if 'U' == direction:
            y_args = (y, y + amount + 1, 1)
            y += amount
        elif 'D' == direction:
            y_args = (y, y - amount - 1, -1)
            y -= amount
        elif 'R' == direction:
            x_args = (x, x + amount + 1, 1)
            x += amount
        elif 'L' == direction:
            x_args = (x, x - amount - 1, -1)
            x -= amount

        for i in range(*x_args):
            for j in range(*y_args):
                coordinates.append((i, j))

    wired.append(coordinates)

wire_1 = wired[0]
wire_2 = wired[1]

intersection = set(wire_1).intersection(set(wire_2))
intersection.remove((0, 0))

manhattan = [abs(coordinate[0]) + abs(coordinate[1]) for coordinate in intersection]

print('Minimum Manhattan distance: {}'.format(min(manhattan)))

steps = []
for coordinate in intersection:
    i_1 = 0
    while coordinate != wire_1[i_1]:
        i_1 += 1

    i_2 = 0
    while coordinate != wire_2[i_2]:
        i_2 += 1

    steps.append(i_1 + i_2)

print('Minimum number of combined steps: {}.'.format(min(steps)))
