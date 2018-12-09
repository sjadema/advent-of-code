with open('assets/problem2.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

twos = 0
threes = 0
for line in lines:
    occurrences = dict((char, line.count(char)) for char in line)

    two = {key: value for key, value in occurrences.items() if value == 2}
    if len(two) > 0:
        twos += 1

    three = {key: value for key, value in occurrences.items() if value == 3}
    if len(three) > 0:
        threes += 1

print('Checksum: {}'.format(twos * threes))

for i in range(len(lines)):
    for j in range(i + 1, len(lines)):
        print(lines[i], lines[j])
        exit()

