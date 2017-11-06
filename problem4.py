import operator
import re
import string

file = open('assets/problem4.txt', 'r')
lines = file.readlines()

codes = []
# lines = ['qzmt-zixmtkozy-ivhz-343[test]']
for line in lines:
    match = re.search('^(?P<hash>[^\d]+)-(?P<sector_id>[\d]+)\[(?P<checksum>[a-z]+)\]$', line)
    groups = match.groupdict()

    codes.append({
        'hash_parts': tuple(groups['hash'].split('-')),
        'sector_id': int(groups['sector_id']),
        'checksum': groups['checksum']
    })

sector_ids = []
for code in codes:
    occurrences = dict(zip(string.ascii_lowercase, [0]*26))

    for char in ''.join(code['hash_parts']):
        occurrences[char] += 1

    sorted_occurrences = sorted(occurrences.items(), key=operator.itemgetter(1), reverse=True)[0:5]

    checksum = ''
    for occurrence in sorted_occurrences:
        checksum += occurrence[0]

    if checksum == code['checksum']:
        sector_ids.append(code['sector_id'])

print('Sector ID sum: ', sum(sector_ids))

alphabet = list(string.ascii_lowercase)
for code in codes:
    if len(code['hash_parts']) != 3:
        continue

    words = []
    for part in code['hash_parts']:
        word = ''
        for char in part:
            index = alphabet.index(char)
            word += alphabet[(index + code['sector_id']) % len(alphabet)]

        if 'northpole' == word:
            print('Sector ID sleigh: ', code['sector_id'])
            exit()
