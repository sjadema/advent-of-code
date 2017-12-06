with open('assets/problem5.txt', 'r') as file:
    instructions = [int(row.strip()) for row in file.readlines()]

jumps = list(instructions)
steps = position = 0
while position < len(jumps):
    jumps[position] += 1
    position += jumps[position] - 1
    steps += 1

print('Total steps: ', steps)

jumps = list(instructions)
steps = position = 0
offset = jumps[0]
while position < len(jumps):
    if offset > 2:
        jumps[position] -= 1
        position += jumps[position] + 1
    else:
        jumps[position] += 1
        position += jumps[position] - 1

    steps += 1

    try:
        offset = jumps[position]
    except IndexError:
        break

print('Total steps: ', steps)
