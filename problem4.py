import re

with open('assets/problem4.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

schedule = {}
for line in lines:
    match = re.search('\[(?P<datetime>[^\]]+)\]', line)
    schedule[match.group('datetime')] = line

ordered = {key: schedule[key] for key in sorted(schedule)}


print(ordered)