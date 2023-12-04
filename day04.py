import re

with open('assets/day04.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

cards = {}
for line in lines:
    match = re.search(r'^Card\s+(?P<card>\d+):(?P<winning_numbers>[^|]+)\|(?P<present_numbers>.+)$', line)

    card = {
        'winning_numbers': [
            int(number) for number in match.group('winning_numbers').strip().replace('  ', ' ').split(' ')
        ],
        'present_numbers': [
            int(number) for number in match.group('present_numbers').strip().replace('  ', ' ').split(' ')
        ],
    }

    cards[int(match.group('card'))] = card

scores = []
for card in cards.values():
    numbers = set(card['winning_numbers']).intersection(set(card['present_numbers']))

    score = len(numbers)
    if score > 0:
        scores.append(2 ** (score - 1))

print(f'''Sum of all scores: {sum(scores)}''')

earned_cards = {card: 1 for card in cards.keys()}
for i in earned_cards.keys():
    card = cards[i]
    numbers = set(card['winning_numbers']).intersection(set(card['present_numbers']))
    score = len(numbers)

    for j in range(0, earned_cards[i]):
        for k in range(i + 1, i + score + 1):
            earned_cards[k] += 1

print(f'''Sum of all cards: {sum(earned_cards.values())}''')
