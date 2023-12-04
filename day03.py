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


def resolve_parts() -> list[int]:
    looked_at = []
    resolved_parts = []

    def resolve_part(coordinate: tuple) -> None:
        if coordinate not in numbers or coordinate in looked_at:
            return

        looked_at.append(coordinate)
        if type(numbers[coordinate]) is tuple:
            resolve_part(numbers[coordinate])
        else:
            resolved_parts.append(numbers[coordinate])

    for symbol_coordinate in symbols.keys():
        symbol_x, symbol_y = symbol_coordinate
        x_axis = range(symbol_x - 1, symbol_x + 2)
        y_axis = range(symbol_y - 1, symbol_y + 2)

        for y_coordinate in y_axis:
            for x_coordinate in x_axis:
                resolve_part((x_coordinate, y_coordinate))

    return resolved_parts


print(f'''Sum of part numbers: {sum(resolve_parts())}''')


def resolve_gear_ratios() -> list[int]:
    looked_at = []
    resolved_parts = []

    def resolve_part(coordinate: tuple) -> None:
        if coordinate not in numbers or coordinate in looked_at:
            return

        looked_at.append(coordinate)
        if type(numbers[coordinate]) is tuple:
            resolve_part(numbers[coordinate])
        else:
            resolved_parts.append(numbers[coordinate])

    gear_ratios = []
    gear_symbols = {k: v for k, v in symbols.items() if v == '*'}
    for gear_symbol_coordinate in gear_symbols.keys():
        symbol_x, symbol_y = gear_symbol_coordinate
        x_axis = range(symbol_x - 1, symbol_x + 2)
        y_axis = range(symbol_y - 1, symbol_y + 2)

        resolved_parts = []
        looked_at = []

        for y_coordinate in y_axis:
            for x_coordinate in x_axis:
                resolve_part((x_coordinate, y_coordinate))

        if len(resolved_parts) == 2:
            gear_ratios.append(resolved_parts[0] * resolved_parts[1])

    return gear_ratios


print(f'''Sum of gear ratios: {sum(resolve_gear_ratios())}''')
