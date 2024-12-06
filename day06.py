import operator
from collections import OrderedDict

type Coordinate = tuple[int, int]

directions = OrderedDict()
directions['^'] = (0, -1)
directions['>'] = (1, 0)
directions['v'] = (0, 1)
directions['<'] = (-1, 0)

with open('assets/day06.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

grid = {}
for y in range(0, len(lines)):
    for x in range(0, len(lines[y])):
        grid[(x, y)] = lines[y][x]


def __get_character_at(coordinate: Coordinate) -> str:
    try:
        return grid[coordinate]
    except KeyError:
        return ''


def __get_next_coordinate(coordinate: Coordinate, direction: Coordinate) -> Coordinate:
    return tuple(map(operator.add, coordinate, direction))


start = None
for coordinate in grid:
    character = __get_character_at(coordinate)
    if character == '^':
        start = coordinate
        break


visited = []

direction = grid[start]
current_coordinate = start
while (next_cell := __get_character_at(__get_next_coordinate(current_coordinate, directions[direction]))) != '':
    if next_cell == '#':
        direction_order = list(directions.keys())
        direction = direction_order[(direction_order.index(direction) + 1) % len(direction_order)]

    visited.append(current_coordinate)
    current_coordinate = __get_next_coordinate(current_coordinate, directions[direction])

print(f'Number of positions visited: {len(set(visited)) + 1}')
