with open('assets/day02.txt', 'r') as file:
    moves = [line for line in file.read().splitlines()]

x = y = y_with_aim = 0
for move in moves:
    direction, amount = move.split(' ')
    amount = int(amount)

    if 'forward' == direction:
        x += amount
        y_with_aim += amount * y
    else:
        modifier = 1 if 'down' == direction else -1
        y += amount * modifier

print(f"Position reached without aim: ({x}, {y}) with product {x * y}.")
print(f"Position reached with aim: ({x}, {y_with_aim}) with product {x * y_with_aim}.")
