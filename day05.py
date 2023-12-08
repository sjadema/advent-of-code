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
#
#
# def get_location(seed: int, rule: tuple[int]) -> int:
#     if rule[1] <= seed < rule[1] + rule[2]:
#         return seed + rule[0] - rule[1]
#
#     return seed
#
#
# min_location = sys.maxsize
# for seed in seeds:
#     for rules in maps.values():
#         for rule in rules:
#             location = get_location(seed, rule)
#             if location != seed:
#                 seed = location
#                 break
#
#     min_location = min(min_location, seed)
#
# print(f'''Minimum location: {min_location}''')

seed_ranges = []
for i in range(0, len(seeds), 2):
    seed_ranges.append((seeds[i], seeds[i], seeds[i + 1]))

seed_ranges.sort(key=lambda x: x[1])
ranges = list(maps.values())
all_ranges = [seed_ranges] + ranges

solved_ranges = all_ranges[0]
for i in range(1, len(all_ranges)):
    solving_ranges = []
    current_ranges = all_ranges[i]

    for solved_range in solved_ranges:
        for current_range in current_ranges:
            # Calculate destination ranges
            solved_dr_start, solved_dr_end = solved_range[0], solved_range[0] + solved_range[2]
            current_dr_start, current_dr_end = current_range[0], current_range[0] + current_range[2]

            # Calculate source ranges
            solved_sr_start, solved_sr_end = solved_range[1], solved_range[1] + solved_range[2]
            current_sr_start, current_sr_end = current_range[1], current_range[1] + current_range[2]

            # Get ranges
            solved_r = solved_range[2]
            current_r = current_range[2]

            # Previous destination range fits inside current source range
            # Slice current range bound by previous destination range
            if current_sr_start <= solved_dr_start and solved_dr_end <= current_sr_end:
                new_sr_start = solved_dr_start
                new_dr_start = current_dr_start - current_sr_start + new_sr_start
                new_r = solved_r

                solving_ranges.append((new_dr_start, new_sr_start, new_r))

            # Previous destination range covers current source range
            # Create 3 ranges, 1 inside and 2 outside the current source range
            elif solved_dr_start < current_sr_start and solved_dr_end > current_sr_end:
                left_sr_start = solved_dr_start
                left_dr_start = left_sr_start
                left_r = current_sr_start - solved_dr_start

                solving_ranges.append((left_dr_start, left_sr_start, left_r))

                inside_sr_start = current_sr_start
                inside_dr_start = current_dr_start
                inside_r = current_r

                solving_ranges.append((inside_dr_start, inside_sr_start, inside_r))

                right_sr_start = current_sr_end
                right_dr_start = right_sr_start
                right_r = solved_dr_end - current_sr_end

                solving_ranges.append((right_dr_start, right_sr_start, right_r))

            # Start is too low, end fits or start fits, end is too high
            # Create 2 ranges, 1 inside and 1 outside the current source range
            elif (
                    solved_dr_start < current_sr_start < solved_dr_end <= current_sr_end or
                    solved_dr_end > current_sr_end > solved_dr_start >= current_sr_start
            ):
                # Create parts (outside with same destination, inside with new destination)
                if solved_dr_start < current_sr_start:
                    inside_sr_start = current_sr_start
                    inside_r = solved_dr_end - current_sr_start

                    outside_sr_start = solved_dr_start

                else:
                    inside_sr_start = solved_dr_start
                    inside_r = current_sr_end - solved_dr_start

                    outside_sr_start = current_sr_end

                inside_dr_start = current_dr_start

                outside_dr_start = outside_sr_start
                outside_r = solved_r - inside_r

                solving_ranges.append((inside_dr_start, inside_sr_start, inside_r))
                solving_ranges.append((outside_dr_start, outside_sr_start, outside_r))

            # Previous destination range is completely outside current source range
            else:
                solving_ranges.append((solved_dr_start, solved_sr_start, solved_r))

    solved_ranges = list(set(solving_ranges))

solved_ranges.sort(key=lambda x: x[0])
print(solved_ranges)

# def map_range(range: tuple, step: int) ->
#
#
# print(all_ranges)
# exit()
#
#
# def get_seed(location: int, rule: tuple[int]) -> int:
#     seed = location + rule[1] - rule[0]
#     if rule[1] <= seed < rule[1] + rule[2]:
#         return seed
#
#     return location
#
#
# print(f'''Starting seed ranges ...''')
#
# min_location = 1
# found = False
# while not found:
#     location = min_location
#     for rules in reversed(maps.values()):
#         for rule in rules:
#             seed = get_seed(location, rule)
#             if seed != location:
#                 location = seed
#                 break
#
#     for seed_range in seed_ranges:
#         if seed_range[0] <= location < seed_range[1]:
#             found = True
#             break
#
#     if min_location % 1000000 == 0:
#         print(f'Location checked: {min_location}')
#
#     min_location += 1
#
# print(f'''Minimum location: {min_location - 1}''')
# print(f'Done in {time.time() - start} seconds')
