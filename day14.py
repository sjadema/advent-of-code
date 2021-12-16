with open('assets/day14.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

insertions = {}
for line in lines[2:]:
    pair, insert = line.split('->')
    insertions[pair.strip()] = insert.strip()


def react(steps: int) -> str:
    polymer = lines[0]
    for _ in range(steps):
        pairs = []
        for i in range(len(polymer) - 1):
            pairs.append(polymer[i:i + 2])

        last = polymer[-1]

        polymer = ''
        for pair in pairs:
            if pair in insertions:
                pair = pair[0] + insertions[pair]

            polymer += pair

        polymer += last

    return polymer


def count_elements(polymer: str) -> dict:
    return {e: polymer.count(e) for e in set(polymer)}


collection = count_elements(react(10))
print(f"10 steps polymer: {max(collection.values()) - min(collection.values())}")
