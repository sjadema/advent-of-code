with open('assets/day03.txt', 'r') as file:
    numbers = [line for line in file.read().splitlines()]

amount = len(numbers)
length = len(numbers[0])

sequences = [[] for i in range(length)]
for i in range(amount):
    for j in range(length):
        sequences[j].append(int(numbers[i][j]))

decimal_gamma = [1 if sequence > amount / 2 else 0 for sequence in [sum(sequence) for sequence in sequences]]
decimal_epsilon = [1 - i for i in decimal_gamma]
gamma = ''.join([str(i) for i in decimal_gamma])
epsilon = ''.join([str(i) for i in decimal_epsilon])

print(f"Power consumption: {int(gamma, 2) * int(epsilon, 2)}")
