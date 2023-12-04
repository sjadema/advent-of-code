import re

with open('assets/day03.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

numbers = {}
symbols = {}
for y in range(0, len(lines)):
    line = lines[len(lines) - 1 - y]

    matches = re.finditer(r'(\d+)', line)
    for match in matches:
        x = match.start()
        numbers[(x, y)] = int(match.group())

        for dx in range(x + 1, match.end()):
            numbers[(dx, y)] = (dx - 1, y)

    symbol_line = re.sub(r'\d', '.', line)
    for x in range(0, len(symbol_line)):
        symbol = symbol_line[x]
        if symbol != '.':
            symbols[(x, y)] = symbol


def resolve_part_numbers() -> list[int]:
    looked_at = []
    part_numbers = []

    def resolve_coordinate(coordinate: tuple) -> None:
        if coordinate not in numbers or coordinate in looked_at:
            return

        looked_at.append(coordinate)
        if type(numbers[coordinate]) is tuple:
            resolve_coordinate(numbers[coordinate])
        else:
            part_numbers.append(numbers[coordinate])

    for symbol_coordinate in symbols.keys():
        symbol_x, symbol_y = symbol_coordinate
        x_axis = range(symbol_x - 1, symbol_x + 2)
        y_axis = range(symbol_y - 1, symbol_y + 2)

        for y_coordinate in y_axis:
            for x_coordinate in x_axis:
                resolve_coordinate((x_coordinate, y_coordinate))

    return part_numbers


print(f'''Sum of part numbers: {sum(resolve_part_numbers())}''')
