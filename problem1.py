with open('assets/problem1.txt', 'r') as file:
    chars = [int(char) for char in file.read().strip()]

length = len(chars)

total = 0
for i in range(length):
    if chars[i] == chars[(i + 1) % length]:
        total += int(chars[i])

print('Total neighbouring: ', total)

total = 0
center = int(length / 2)
for i in range(length):
    if chars[i] == chars[(center + i) % length]:
        total += int(chars[i])

print('Total halfway: ', total)
