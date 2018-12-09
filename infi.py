import re

with open('assets/infi.txt', 'r') as file:
    content = file.readline().strip()

bot_string = re.search('^([^\(]+)', content).group()

bots = {}
bot = 0
for match in re.finditer('\[(?P<x>\d+),(?P<y>\d+)\]', bot_string):
    bots[bot] = (int(match.group('x')), int(match.group('y')))
    bot += 1

coordinate_string = content[len(bot_string):]

coordinates = {}
for i in range(len(bots)):
    coordinates[i] = []

bot = 0
for match in re.finditer('\((?P<x>[^,]+),(?P<y>[^\)]+)\)', coordinate_string):
    coordinates[bot % len(bots)].append((int(match.group('x')), int(match.group('y'))))
    bot += 1


paths = {}
for bot, path in bots.items():
    paths[bot] = []
    position = bots[bot]
    for coordinate in coordinates[bot]:
        x = coordinate[0]
        y = coordinate[1]
        position = (position[0] + x, position[1] + y)

        paths[bot].append(position)


collisions = 0
for i in range(len(paths[0])):
    coordinates = set()
    for j in range(len(paths)):
        coordinates.add(paths[j][i])

    if len(coordinates) != len(paths):
        collisions += 1

print('Collisions: ', collisions)
