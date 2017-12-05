with open('assets/problem5.txt', 'r') as file:
    instructions = [int(row.strip()) for row in file.readlines()]

print(instructions)
