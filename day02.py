with open('assets/day02.txt', 'r') as file:
    legs = [line for line in file.read().splitlines()]

x = y = aim = y_aim = 0
for leg in legs:
    direction, amount = tuple(leg.split(' '))
    amount = int(amount)

    if 'forward' == direction:
        x += amount
        y_aim += (amount * aim)
    else:
        modifier = 1 if 'down' == direction else -1
        y += (amount * modifier)
        aim += (amount * modifier)

print("Position reached without aim: ({:d}, {:d}) with product {:d}.".format(x, y, x * y))
print("Position reached with aim: ({:d}, {:d}) with product {:d}.".format(x, y_aim, x * y_aim))
