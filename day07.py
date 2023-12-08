from collections import Counter

with open('assets/day07.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]
hands = [(line.split(' ')[0], int(line.split(' ')[1])) for line in lines]

alphabet = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

combinations = [
    (5,),
    (4, 1),
    (3, 2),
    (3, 1, 1),
    (2, 2, 1),
    (2, 1, 1, 1),
    (1, 1, 1, 1, 1),
]


def pentadecimal_to_decimal(number: str) -> int:
    value = 0
    for i in range(len(number := number[::-1])):
        value += alphabet.index(number[i]) * len(alphabet) ** i

    return value


scores = {combination: [] for combination in combinations}
for hand in hands:
    combination = tuple(sorted(Counter(hand[0]).values(), reverse=True))

    scores[combination].append(hand)

ranks = []
for combinations in scores.values():
    combinations.sort(key=lambda combination: pentadecimal_to_decimal(combination[0]), reverse=True)
    ranks += combinations

number_of_hands = len(ranks)
total_winnings = []
for i in range(len(ranks)):
    rank = ranks[i]
    total_winnings.append(rank[1] * (number_of_hands - i))

print(f'Total winnings: {sum(total_winnings)}')
