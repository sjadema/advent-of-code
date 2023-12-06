import sys
import time

start = time.time()

with open('assets/day05.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

seeds = [int(seed) for seed in lines[0].split(':')[1].strip().split(' ')]

maps = {
    'seed-to-soil': [],
    'soil-to-fertilizer': [],
    'fertilizer-to-water': [],
    'water-to-light': [],
    'light-to-temperature': [],
    'temperature-to-humidity': [],
    'humidity-to-location': [],
}

i, header = 1, -1
while i < len(lines):
    if lines[i] == '':
        header += 1
        i += 2

        continue

    sections = list(maps.keys())
    maps[sections[header]].append(tuple([int(i) for i in lines[i].split(' ')]))

    i += 1

for rules in maps.values():
    rules.sort(key=lambda x: x[1])


def get_location(seed: int, rule: tuple[int]) -> int:
    if rule[1] <= seed < rule[1] + rule[2]:
        return seed + rule[0] - rule[1]

    return seed


min_location = sys.maxsize
for seed in seeds:
    for rules in maps.values():
        for rule in rules:
            location = get_location(seed, rule)
            if location != seed:
                seed = location
                break

    min_location = min(min_location, seed)

print(f'''Minimum location: {min_location}''')

seed_ranges = []
for i in range(0, len(seeds), 2):
    seed_ranges.append((seeds[i], seeds[i] + seeds[i + 1]))


def get_seed(location: int, rule: tuple[int]) -> int:
    seed = location + rule[1] - rule[0]
    if rule[1] <= seed < rule[1] + rule[2]:
        return seed

    return location


print(f'''Starting seed ranges ...''')

min_location = 1
found = False
while not found:
    location = min_location
    for rules in reversed(maps.values()):
        for rule in rules:
            seed = get_seed(location, rule)
            if seed != location:
                location = seed
                break

    for seed_range in seed_ranges:
        if seed_range[0] <= location < seed_range[1]:
            found = True
            break

    if min_location % 1000000 == 0:
        print(f'Location checked: {min_location}')

    min_location += 1

print(f'''Minimum location: {min_location - 1}''')
print(f'Done in {time.time() - start} seconds')
