with open('assets/problem002.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

passwords = []
for line in lines:
    parts = line.split(':')
    policy = parts[0].split(' ')
    passwords.append({
        'range': policy[0],
        'char': policy[1],
        'password': parts[1].strip()
    })

valid = 0
for password in passwords:
    boundaries = [int(boundary) for boundary in password['range'].split('-')]
    delta = len(password['password']) - len(password['password'].replace(password['char'], ''))
    if boundaries[0] <= delta <= boundaries[1]:
        valid += 1

print('Valid passwords: {}'.format(valid))
