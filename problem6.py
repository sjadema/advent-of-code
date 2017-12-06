with open('assets/problem6.txt', 'r') as file:
    blocks = [int(block) for block in file.read().strip().split('\t')]

bank = list(blocks)
states = []
cycles = 0
while tuple(bank) not in states:
    states.append(tuple(bank))

    value = max(bank)
    index = bank.index(value)
    bank[index] = 0

    for i in range(value):
        bank[(index + 1 + i) % len(bank)] += 1

    cycles += 1

print('Total cycles: ', cycles)

bank = list(blocks)
states = []
while tuple(bank) not in states:
    states.append(tuple(bank))

    value = max(bank)
    index = bank.index(value)
    bank[index] = 0

    for i in range(value):
        bank[(index + 1 + i) % len(bank)] += 1

index = states.index(tuple(bank))
print('Total cycles in loop: ', len(states) - index)
