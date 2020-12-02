from functools import reduce

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

range_valid = 0
position_valid = 0
for password in passwords:
    boundaries = [int(boundary) for boundary in password['range'].split('-')]
    delta = len(password['password']) - len(password['password'].replace(password['char'], ''))
    if boundaries[0] <= delta <= boundaries[1]:
        range_valid += 1

    positions = boundaries
    delta = [password['password'][position - 1] == password['char'] for position in positions]
    if bool(reduce(lambda x, y: x ^ y, delta)):
        position_valid += 1

print('Valid range passwords: {}.'.format(range_valid))
print('Valid position passwords: {}.'.format(position_valid))
