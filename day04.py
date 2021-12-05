with open('assets/day04.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

drawn = [int(number) for number in lines[0].split(',')]

puzzles = []
for i in range(2, len(lines), 6):
    puzzle = {
        'puzzle': [],
        'h': [],
        'v': [],
        'found_h': ['.'] * 25,
        'found_v': ['.'] * 25,
    }

    for j in range(5):
        row = [int(number) for number in lines[i + j].split(' ') if len(number)]
        puzzle['puzzle'].append(row)

    for j in range(5):
        for k in range(5):
            puzzle['h'].append(puzzle['puzzle'][j][k])
            puzzle['v'].append(puzzle['puzzle'][k][j])

    puzzles.append(puzzle)

try:
    target = 'xxxxx'
    for number in drawn:
        for puzzle in puzzles:
            if number in puzzle['h']:
                h = puzzle['h'].index(number)
                v = puzzle['v'].index(number)

                puzzle['found_h'][h] = 'x'
                puzzle['found_v'][v] = 'x'

            found_h = ''.join(puzzle['found_h'])
            found_v = ''.join(puzzle['found_v'])

            for direction, found in {'h': found_h, 'v': found_v}.items():
                if target in found and 0 == found.index(target) % 5:
                    unmarked = 0
                    for i in range(len(found)):
                        if '.' == found[i]:
                            unmarked += puzzle[direction][i]

                    print(f"Puzzle score: {unmarked * number}")
                    raise StopIteration
except StopIteration:
    pass

