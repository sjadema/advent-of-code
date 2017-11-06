file = open('assets/problem2.txt', 'r')
steps = file.readlines()

directions = {
    'U': (0, -1),
    'R': (1, 0),
    'D': (0, 1),
    'L': (-1, 0),
}

keypad = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

code = ''
location = (1, 1)
for step in steps:
    for move in step:
        try:
            x = location[0] + directions[move][0]
            y = location[1] + directions[move][1]

            if 0 <= x <= 2 and 0 <= y <= 2:
                location = (x, y)

        except KeyError:
            continue

    code += str(keypad[location[1]][location[0]])

print('Code normal: ', code)

keypad = [
    [None, None, 1, None, None],
    [None, 2, 3, 4, None],
    [5, 6, 7, 8, 9],
    [None, 'A', 'B', 'C', None],
    [None, None, 'D', None, None]
]

code = ''
location = (0, 2)
for step in steps:
    for move in step:
        try:
            x = location[0] + directions[move][0]
            y = location[1] + directions[move][1]

            if 0 <= y <= 4 and 0 <= x <= 4 and keypad[y][x] is not None:
                location = (x, y)

        except KeyError:
            continue

    code += str(keypad[location[1]][location[0]])

print('Code not normal: ', code)
