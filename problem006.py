from functools import reduce

with open('assets/problem006.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

groups = [[]]
i = 0
for line in lines:
    if '' == line:
        i += 1
        groups.append([])
        continue

    groups[i].append(line)

anyone = []
for group in groups:
    anyone.append(set(list(''.join(group))))

print('Sum of questions answered by anyone: {}.'.format(reduce(lambda total, group: total + len(group), anyone, 0)))

everyone = []
for group in groups:
    everyone.append(set(group[0]).intersection(*[set(part) for part in group[1:]]))

print('Sum of questions answered by everyone: {}.'.format(reduce(lambda total, group: total + len(group), everyone, 0)))
