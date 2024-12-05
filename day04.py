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


def get_next_coordinate(coordinate: Coordinate, direction: Coordinate) -> Coordinate:
    return tuple(map(operator.add, coordinate, direction))


def get_coordinate_difference(a: Coordinate, b: Coordinate) -> Coordinate:
    difference = tuple(map(operator.sub, a, b))

    return (abs(difference[0]), abs(difference[1]))


def get_character_at(coordinate: Coordinate) -> str:
    try:
        return characters[coordinate]
    except KeyError:
        return ''


def search_word(start: Coordinate, direction: str, length: int) -> str:
    word = get_character_at(start)

    coordinate = start
    for i in range(0, length - 1):
        coordinate = get_next_coordinate(coordinate, directions[direction])
        word += get_character_at(coordinate)

    return word


found_words = 0
for coordinate in characters:
    if get_character_at(coordinate) != 'X':
        continue

    for direction in directions.keys():
        word = search_word(coordinate, direction, 4)
        if word == 'XMAS':
            found_words += 1

print(f'Number of times XMAS in puzzle: {found_words}')

found_coordinates = []
for coordinate in characters:
    if get_character_at(coordinate) != 'M':
        continue

    for direction in directions.keys():
        word = search_word(coordinate, direction, 3)

        if word == 'MAS':
            coordinates = [coordinate]
            for i in range(0, 2):
                coordinates.append(get_next_coordinate(coordinates[-1], directions[direction]))

            found_coordinates.append(coordinates)

found_crosses = 0
for i in range(0, len(found_coordinates) - 1):
    for j in range(i + 1, len(found_coordinates)):
        a, b = found_coordinates[i], found_coordinates[j]
        if a[1] == b[1]:
            difference = get_coordinate_difference(a[0], b[0])
            if difference in [(2, 0), (0, 2)]:
                found_crosses += 1

print(f'Number of times X-MAS in puzzle: {found_crosses}')
