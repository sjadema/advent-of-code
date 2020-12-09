with open('assets/problem009.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

xmas = [int(c) for c in lines]

preamble_length = 25
cursor = preamble_length

while True:
    answers = []
    for i in range(cursor - preamble_length, cursor):
        for j in range(i + 1, cursor):
            if xmas[i] != xmas[j]:
                answers.append(xmas[i] + xmas[j])

    current = xmas[cursor]
    if current in answers:
        cursor += 1
        continue

    print('Invalid number: {}.'.format(current))
    break
