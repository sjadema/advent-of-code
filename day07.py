from collections import Counter
from typing import Dict, List

with open('assets/day07.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]
hands = [(line.split(' ')[0], int(line.split(' ')[1])) for line in lines]

alphabets = {
    'normal': ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A'],
    'joker': ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A'],
}

hand_types = [
    (5,),
    (4, 1),
    (3, 2),
    (3, 1, 1),
    (2, 2, 1),
    (2, 1, 1, 1),
    (1, 1, 1, 1, 1),
]


def combination_to_decimal(combination: str, alphabet: List) -> int:
    value = 0
    for i in range(len(combination := combination[::-1])):
        value += alphabet.index(combination[i]) * len(alphabet) ** i

    return value


def get_ranking(hand_type_scores: Dict[tuple, List[tuple]], alphabet: List[str]) -> List[tuple]:
    ranking = []
    for combinations in hand_type_scores.values():
        type_combinations = sorted(
            combinations,
            key=lambda combination: combination_to_decimal(combination[0], alphabet),
            reverse=True
        )

        ranking += type_combinations

    return ranking


def get_winnings(ranking: List[tuple]) -> List[int]:
    number_of_hands = len(ranking)
    total_winnings = []
    for i in range(number_of_hands):
        rank = ranking[i]
        total_winnings.append(rank[1] * (number_of_hands - i))

    return total_winnings


scores = {hand_type: [] for hand_type in hand_types}
for hand in hands:
    hand_type = tuple(sorted(Counter(hand[0]).values(), reverse=True))

    scores[hand_type].append(hand)

ranking = get_ranking(scores, alphabets['normal'])
winnings = get_winnings(ranking)

print(f'Total winnings: {sum(winnings)}')

scores = {hand_type: [] for hand_type in hand_types}
for hand in hands:
    score = dict(Counter(hand[0]))
    jokers = 0
    if 'J' in score:
        jokers = score['J']
        del score['J']

    hand_type = list(sorted(score.values(), reverse=True))
    if not hand_type:
        hand_type = [0]

    hand_type[0] += jokers

    scores[tuple(hand_type)].append(hand)

ranking = get_ranking(scores, alphabets['joker'])
winnings = get_winnings(ranking)

print(f'Total winnings: {sum(winnings)}')
