import re

with open('assets/day04.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

cards = []
for line in lines:
    match = re.search(r'^Card\s+(?P<card>\d+):(?P<winning_numbers>[^|]+)\|(?P<present_numbers>.+)$', line)

    card = {
        'card': int(match.group('card')),
        'winning_numbers': [
            int(number) for number in match.group('winning_numbers').strip().replace('  ', ' ').split(' ')
        ],
        'present_numbers': [
            int(number) for number in match.group('present_numbers').strip().replace('  ', ' ').split(' ')
        ],
    }

    cards.append(card)

scores = []
for card in cards:
    numbers = set(card['winning_numbers']).intersection(set(card['present_numbers']))

    score = len(numbers)
    if score > 0:
        scores.append(2 ** (score - 1))

print(f'''Sum of all scores: {sum(scores)}''')
