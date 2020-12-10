with open('assets/problem010.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

jolts = [0] + sorted([int(line) for line in lines])

differences = {1: 0, 3: 1}

for i in range(0, len(jolts) - 1):
    differences[jolts[i + 1] - jolts[i]] += 1

print('Difference product: {}'.format(differences[1] * differences[3]))
