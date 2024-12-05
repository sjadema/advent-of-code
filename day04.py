import operator

with open('assets/day04.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

puzzle = [list(line) for line in lines]

type Coordinate = tuple[int, int]

directions = {
    'n': (0, 1),
    'e': (1, 0),
    's': (0, -1),
    'w': (-1, 0),
    'ne': (1, 1),
    'se': (1, -1),
    'sw': (-1, -1),
    'nw': (-1, 1),
}

characters = {}
for y in range(0, len(puzzle)):
    for x in range(0, len(puzzle[y])):
        characters[(x, y)] = puzzle[y][x]


def get_character_at(coordinate: Coordinate) -> str:
    try:
        return characters[coordinate]
    except KeyError:
        return ''


def search_word(start: Coordinate, direction: str) -> str:
    word = get_character_at(start)

    coordinate = start
    for i in range(0, 3):
        coordinate = tuple(map(operator.add, coordinate, directions[direction]))
        word += get_character_at(coordinate)

    return word


found_words = 0
for coordinate in characters:
    for direction in directions.keys():
        word = search_word(coordinate, direction)

        if word == 'XMAS':
            found_words += 1

print(f'Number of times XMAS in puzzle: {found_words}')
