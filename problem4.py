import itertools

with open('assets/problem4.txt', 'r') as file:
    rows = [list(row.strip().split(' ')) for row in file.readlines()]

total = 0
for row in rows:
    unique = set(row)
    if len(unique) == len(row):
        total += 1

print('Valid passwords (unique): ', total)

total = len(rows)
for row in rows:
    permutations = []
    for part in row:
        permutations.append(set([''.join(p) for p in itertools.permutations(part)]))

    valid = True
    for i in range(len(row)):
        for j in range(i + 1, len(row)):
            if row[i] in permutations[j]:
                total -= 1
                valid = False
                break

        if not valid:
            break

print('Valid passwords (permutations): ', total)
