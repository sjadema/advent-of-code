with open('assets/problem003.txt', 'r') as file:
    sequences = [line for line in file.read().splitlines()]

sequence_amount = len(sequences)
sequence_length = len(sequences[0])

binary_sequences = [''] * sequence_length
for i in range(0, sequence_amount):
    for j in range(0, sequence_length):
        binary_sequences[j] += sequences[i][j]

decimal_sequences = [[int(i) for i in sequence[0::]] for sequence in binary_sequences]
summed_sequences = [sum(sequence) for sequence in decimal_sequences]

decimal_gamma = [1 if sequence > sequence_amount / 2 else 0 for sequence in summed_sequences]
decimal_epsilon = [1 - i for i in decimal_gamma]
gamma = ''.join([str(i) for i in decimal_gamma])
epsilon = ''.join([str(i) for i in decimal_epsilon])

print(f"Power consumption: {int(gamma, 2) * int(epsilon, 2)}")
