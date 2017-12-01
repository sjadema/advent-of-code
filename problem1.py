file = open('assets/problem1.txt', 'r')
chars = file.read()

parsed_chars = []
for char in chars:
    parsed_chars.append(char)

neighbouring_chars = parsed_chars[1:] + parsed_chars[0:1]

total = 0
for i in range(0, len(neighbouring_chars) - 1):
    if neighbouring_chars[i] == neighbouring_chars[i + 1]:
        total += int(neighbouring_chars[i])

print('Total neighbouring: ', total)

total = 0
for i in range(0, len(parsed_chars)):
    if parsed_chars[i] == parsed_chars[int(len(parsed_chars) / 2 + i) % len(parsed_chars)]:
        total += int(parsed_chars[i])

print('Total halfway: ', total)
