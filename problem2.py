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

corrects = []
for i in range(len(lines)):
    for j in range(i + 1, len(lines)):
        chars_first = list(lines[i])
        chars_second = list(lines[j])

        difference = 0
        for k in range(len(chars_first)):
            if difference > 1:
                break

            if chars_first[k] != chars_second[k]:
                difference += 1

        if difference == 1:
            corrects.append(lines[i])
            corrects.append(lines[j])

correct = []
for i in range(len(corrects)):
    for j in range(i + 1, len(corrects)):
        chars_first = list(corrects[i])
        chars_second = list(corrects[j])

        for k in range(len(chars_first)):
            if chars_first[k] == chars_second[k]:
                correct.append(chars_first[k])

print('Correct: {}'.format(''.join(correct)))
