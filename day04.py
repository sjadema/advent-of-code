with open('assets/day04.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

drawn = [int(number) for number in lines[0].split(',')]

row_length = 5
puzzles = []
for i in range(2, len(lines), 6):
    puzzle = {
        'puzzle': [],
        'h': [],
        'v': [],
        'found_h': ['.'] * row_length ** 2,
        'found_v': ['.'] * row_length ** 2,
        'solved': False,
    }

    for j in range(row_length):
        row = [int(number) for number in lines[i + j].split(' ') if len(number)]
        puzzle['puzzle'].append(row)

    for j in range(row_length):
        for k in range(row_length):
            puzzle['h'].append(puzzle['puzzle'][j][k])
            puzzle['v'].append(puzzle['puzzle'][k][j])

    puzzles.append(puzzle)

scores = []
for number in drawn:
    for puzzle in puzzles:
        if puzzle['solved']:
            continue

        if number in puzzle['h']:
            h = puzzle['h'].index(number)
            v = puzzle['v'].index(number)

            puzzle['found_h'][h] = 'x'
            puzzle['found_v'][v] = 'x'

        for direction, found in {'h': puzzle['found_h'], 'v': puzzle['found_v']}.items():
            chunks = [''.join(found[j:j + row_length]) for j in range(0, len(found), row_length)]

            if 'xxxxx' in chunks:
                unmarked = 0
                for j in range(len(found)):
                    if '.' == found[j]:
                        unmarked += puzzle[direction][j]

                scores.append(unmarked * number)
                puzzle['solved'] = True
                break

print(f"First score: {scores[0]}")
print(f"Last score: {scores[-1]}")
