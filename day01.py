import re
from collections import defaultdict

with open('assets/day01.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

location_ids_first = []
location_ids_second = []
for line in lines:
    value = re.match(r'(?P<first>\d+)\s+(?P<second>\d+)', line)
    location_ids_first.append(int(value.group('first')))
    location_ids_second.append(int(value.group('second')))

location_ids_first.sort()
location_ids_second.sort()

distance = 0
for i in range(0, len(location_ids_first)):
    first_location = location_ids_first[i]
    second_location = location_ids_second[i]

    distance += max(first_location, second_location) - min(first_location, second_location)

print(f'Sum of all distances: {distance}')


occurrences = defaultdict(int)
for location_id in location_ids_second:
    occurrences[location_id] += 1

distance = 0
for location_id in location_ids_first:
    distance += location_id * occurrences[location_id]

print(f'Sum of all distances: {distance}')
