with open('assets/problem1.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

changes = []
for line in lines:
    change = int(line[1:])
    if line[0:1] == '-':
        change *= -1

    changes.append(change)

print('Frequency after changes: {}'.format(sum(changes)))

frequency = 0
frequencies = {0}
run = True
index = 0
length = len(changes)
while run:
    frequency += changes[index % length]
    if frequency in frequencies:
        run = False

    frequencies.add(frequency)
    index += 1

print('First duplicate frequency: {}'.format(frequency))
