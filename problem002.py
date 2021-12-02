with open('assets/problem002.txt', 'r') as file:
    legs = [line for line in file.read().splitlines()]

x = y = 0
for leg in legs:
    direction, amount = tuple(leg.split(' '))
    amount = int(amount)

    if 'forward' == direction:
        x += amount
    else:
        modifier = 1 if 'down' == direction else -1
        y += (amount * modifier)

print("Position reached: ({:d}, {:d}) with product {:d}.".format(x, y, x * y))
