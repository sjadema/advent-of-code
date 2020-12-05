import re

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

valid_passports = 0
for passport in passports:
    birth_year = int(passport['byr']) if 'byr' in passport else 0
    issue_year = int(passport['iyr']) if 'iyr' in passport else 0
    expiration_year = int(passport['eyr']) if 'eyr' in passport else 0
    height = passport['hgt'] if 'hgt' in passport else '0cm'
    hair_color = passport['hcl'] if 'hcl' in passport else ''
    eye_color = passport['ecl'] if 'ecl' in passport else ''
    passport_id = passport['pid'] if 'pid' in passport else ''

    if 1920 <= birth_year <= 2002 and 2010 <= issue_year <= 2020 <= expiration_year <= 2030:
        if 9 == len(passport_id) and eye_color in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            if re.compile('^#[0-9a-f]{6}$').match(hair_color):
                real_height = int(height.replace('cm', '').replace('in', ''))
                if ('cm' in height and 150 <= real_height <= 193) or ('in' in height and 59 <= real_height <= 76):
                    valid_passports += 1

print('Number of valid passports: {}.'.format(valid_passports))
