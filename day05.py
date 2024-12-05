with open('assets/day05.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

orders = []
for line in [line for line in lines if '|' in line]:
    before, after = line.split('|')
    orders.append((int(before), int(after)))

instructions = []
for line in [line for line in lines if ',' in line]:
    instructions.append([int(page) for page in line.split(',')])

valid_instructions = []
for instruction in instructions:
    instruction_valid = True
    for order in orders:
        if (
                len(set(order).intersection(set(instruction))) == 2 and
                instruction.index(order[0]) > instruction.index(order[1])
        ):
            instruction_valid = False
            break

    if instruction_valid:
        valid_instructions.append(instruction)

middle_pages = []
for instruction in valid_instructions:
    middle_pages.append(instruction[len(instruction) // 2])

print(f'Sum of middle pages: {sum(middle_pages)}')
