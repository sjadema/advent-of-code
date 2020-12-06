with open('assets/problem006.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

groups = ['']
i = 0
for line in lines:
    if '' == line:
        i += 1
        groups.append('')

    groups[i] += line

for i in range(0, len(groups)):
    groups[i] = set(list(groups[i]))

total = 0
for group in groups:
    total += len(group)

print('Sum of all answered questions: {}.'.format(total))
