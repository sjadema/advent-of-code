content = None
with open('assets/problem1.txt', 'r') as file:
    content = file.read().strip()

chars = []
for char in content:
    chars.append(char)

length = len(chars)
neighbouring_chars = chars[1:] + chars[0:1]

total = 0
for i in range(length - 1):
    if neighbouring_chars[i] == neighbouring_chars[i + 1]:
        total += int(neighbouring_chars[i])

print('Total neighbouring: ', total)

total = 0
center = int(length / 2)
for i in range(length):
    if chars[i] == chars[(center + i) % length]:
        total += int(chars[i])

print('Total halfway: ', total)
