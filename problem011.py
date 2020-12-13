with open('assets/problem011.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

seats = []
for y in range(0, len(lines)):
    row = []
    for x in range(0, len(lines[y])):
        row.append(lines[y][x])

    seats.append(row)


def count_occupied(seats: list[list[str]], row: int, column: int) -> int:
    occupied = 0
    for y in range(max(row - 1, 0), min(len(seats), row + 2)):
        for x in range(max(column - 1, 0), min(len(seats[row]), column + 2)):
            if y == row and x == column:
                continue

            occupied += int('#' == seats[y][x])

    return occupied


changes = -1
while 0 != changes:
    changes = 0
    new_seats = []

    for row in range(0, len(seats)):
        new_row = []
        for column in range(0, len(seats[row])):
            seat = seats[row][column]

            occupied = count_occupied(seats, row, column)
            if 'L' == seat and 0 == occupied:
                new_row.append('#')
                changes += 1
            elif '#' == seat and 3 < occupied:
                new_row.append('L')
                changes += 1
            else:
                new_row.append(seat)

        new_seats.append(new_row)

    seats = new_seats

print('Total number of occupied seats: {}.'.format(sum([row.count('#') for row in seats])))
