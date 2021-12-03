with open('assets/problem011.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

seats = []
for y in range(0, len(lines)):
    row = []
    for x in range(0, len(lines[y])):
        row.append(lines[y][x])

    seats.append(row)


def count_occupied_adjacent(seats: list[list[str]], row: int, column: int) -> int:
    occupied_adjacent = 0
    for y in range(max(row - 1, 0), min(len(seats), row + 2)):
        for x in range(max(column - 1, 0), min(len(seats[row]), column + 2)):
            if y == row and x == column:
                continue

            occupied_adjacent += int('#' == seats[y][x])

    return occupied_adjacent


seats_adjacent = seats
changes = -1
while 0 != changes:
    changes = 0
    new_seats = []

    for row in range(0, len(seats_adjacent)):
        new_row = []
        for column in range(0, len(seats_adjacent[row])):
            seat = seats_adjacent[row][column]

            occupied = count_occupied_adjacent(seats_adjacent, row, column)
            if 'L' == seat and 0 == occupied:
                new_row.append('#')
                changes += 1
            elif '#' == seat and 3 < occupied:
                new_row.append('L')
                changes += 1
            else:
                new_row.append(seat)

        new_seats.append(new_row)

    seats_adjacent = new_seats

print('Total number of occupied seats: {}.'.format(sum([row.count('#') for row in seats_adjacent])))


def count_occupied_seen(seats: list[list[str]], row: int, column: int) -> int:
    occupied_seen = 0
    for y in range(0, len(seats)):
        delta = abs(y - row)
        if 0 == delta:
            columns = range(0, len(seats[row]))
        else:
            columns = range(max(column - delta, 0), min(len(seats[row]), column + delta + 1), delta)

        for x in columns:
            if y == row and x == column:
                continue

            if ()
            occupied_seen =




        for x in range()
    return occupied_seen

seats_seen = seats
changes = -1
while 0 != changes:
    changes = 0
    new_seats = []

    for row in range(0, len(seats_seen)):
        new_row = []
        for column in range(0, len(seats_seen[row])):
            seat = seats_seen[row][column]

            occupied = count_occupied_adjacent(seats_seen, row, column)
            if 'L' == seat and 0 == occupied:
                new_row.append('#')
                changes += 1
            elif '#' == seat and 3 < occupied:
                new_row.append('L')
                changes += 1
            else:
                new_row.append(seat)

        new_seats.append(new_row)

    seats_adjacent = new_seats

print('Total number of occupied seats: {}.'.format(sum([row.count('#') for row in seats_seen])))
