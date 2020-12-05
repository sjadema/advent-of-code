with open('assets/problem004.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

passports = ['']
i = 0
for line in lines:
    if '' == line:
        i += 1
        passports.append('')

    passports[i] += ' ' + line

for i in range(0, len(passports)):
    passport = {}
    sections = passports[i].strip().split(' ')
    for section in passports[i].strip().split(' '):
        parts = section.split(':')
        passport[parts[0]] = parts[1]

    passports[i] = passport

valid_passports = 0
for passport in passports:
    if 8 == len(passport) or (7 == len(passport) and 'cid' not in passport):
        valid_passports += 1

print('Number of valid passports: {}.'.format(valid_passports))
