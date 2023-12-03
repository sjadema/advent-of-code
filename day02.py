import re

with open('assets/day02.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

pattern = r'^Game (?P<game>\d+): (?P<grabs>.*)$'

games = []
for line in lines:
    match = re.search(pattern, line)
    grabs = []

    for grab in match.group('grabs').split(';'):
        collection = [color.strip() for color in grab.split(',')]

        cubes = {'red': 0, 'green': 0, 'blue': 0}
        for combination in collection:
            number, color = combination.split(' ')
            cubes[color] = int(number)

        grabs.append(cubes)

    games.append({
        'number': int(match.group('game')),
        'grabs': grabs,
    })

maximum_cubes = {'red': 12, 'green': 13, 'blue': 14}

possible_games = []
for game in games:
    valid = 0
    for cubes in game['grabs']:
        result = {color: maximum_cubes[color] - cubes[color] for color in maximum_cubes.keys()}
        if min(result.values()) >= 0:
            valid += 1

    if valid == len(game['grabs']):
        possible_games.append(game['number'])

print(f'''Sum of possible games: {sum(possible_games)}''')
