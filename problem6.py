import operator
import string

file = open('assets/problem6.txt', 'r')
lines = file.readlines()

char_sets = []
for line in lines:
    chars = []
    for char in line.replace('\n', ''):
        chars.append(char)

    char_sets.append(tuple(chars))


columns = []
for i in range(0, len(char_sets[0])):
    column = ''
    for j in range(0, len(char_sets)):
        column += char_sets[j][i]

    columns.append(column)

message_most = ''
message_least = ''
for column in columns:
    occurrences = dict(zip(string.ascii_lowercase, [0] * 26))

    for char in column:
        occurrences[char] += 1

    sorted_occurrences = sorted(occurrences.items(), key=operator.itemgetter(1))
    message_most += sorted_occurrences[-1][0]
    message_least += sorted_occurrences[0][0]


print('Message (most occurrences): ', message_most)
print('Message (least occurrences): ', message_least)
