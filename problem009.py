with open('assets/problem009.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

xmas = [int(c) for c in lines]

preamble_length = 25
cursor = preamble_length

invalid = 0
while True:
    answers = []
    for i in range(cursor - preamble_length, cursor):
        for j in range(i + 1, cursor):
            if xmas[i] != xmas[j]:
                answers.append(xmas[i] + xmas[j])

    if xmas[cursor] in answers:
        cursor += 1
        continue

    invalid = xmas[cursor]
    break

print('Invalid number: {}.'.format(invalid))

while True:
    for i in range(0, len(xmas)):
        answers = [xmas[i]]
        for j in range(i + 1, len(xmas)):
            answers.append(xmas[j])

            if sum(answers) == invalid:
                print('Sum of invalid range: {}.'.format(min(answers) + max(answers)))
                exit()

            if sum(answers) > invalid:
                break
