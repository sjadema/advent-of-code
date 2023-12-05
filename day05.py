import operator
from typing import Optional

with open('assets/day05.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

seeds = [int(seed) for seed in lines[0].split(':')[1].strip().split(' ')]

maps = {
    'seed-to-soil': set(),
    'soil-to-fertilizer': set(),
    'fertilizer-to-water': set(),
    'water-to-light': set(),
    'light-to-temperature': set(),
    'temperature-to-humidity': set(),
    'humidity-to-location': set(),
}

i, header = 1, -1
while i < len(lines):
    if lines[i] == '':
        header += 1
        i += 2

        continue

    sections = list(maps.keys())
    maps[sections[header]].add(tuple([int(i) for i in lines[i].split(' ')]))

    i += 1


def get_rule_value(seed: int, rule: tuple) -> Optional[int]:
    result = operator.and_(operator.ge(seed, rule[1]), operator.lt(seed, rule[1] + rule[2]))

    return seed + rule[0] - rule[1] if result else None


def get_value(seed: int, rules: set) -> int:
    for rule in rules:
        value = get_rule_value(seed, rule)
        if type(value) is int:
            return value

    return seed


locations = set()
for seed in seeds:
    for rules in maps.values():
        seed = get_value(seed, rules)

    locations.add(seed)

print(f'''Minimum location: {min(locations)}''')
