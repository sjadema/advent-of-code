with open('assets/day14.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

insertions = {}
for line in lines[2:]:
    pair, insert = line.split('->')
    insertions[pair.strip()] = insert.strip()


def react(steps: int) -> dict:
    pairs = {}

    def add_pair(pair: str, amount: int) -> None:
        if pair not in pairs:
            pairs[pair] = 0

        pairs[pair] += amount

    polymer = lines[0]
    for i in range(len(polymer) - 1):
        add_pair(polymer[i:i + 2], 1)

    for _ in range(steps):
        reacting_pairs = {pair: amount for pair, amount in pairs.items() if pair in insertions and 0 < amount}
        for pair, amount in reacting_pairs.items():
            add_pair(pair[0] + insertions[pair], amount)
            add_pair(insertions[pair] + pair[1], amount)
            pairs[pair] -= amount

    occurrences = {}
    for pair, amount in pairs.items():
        for element in pair:
            if element not in occurrences:
                occurrences[element] = 0

            occurrences[element] += amount

    for element, occurrence in occurrences.items():
        occurrences[element] = occurrence // 2 + (1 if 1 == occurrence % 2 else 0)

    return occurrences


for steps in [10, 40]:
    occurrences = react(steps)
    print(f"{steps} steps polymer: {max(occurrences.values()) - min(occurrences.values())}")
