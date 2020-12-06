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
for i in range(0, len(groups)):
    anyone.append(set(list(''.join(groups[i]))))

print('Sum of all answered questions: {}.'.format(reduce(lambda total, group: total + len(group), anyone, 0)))
