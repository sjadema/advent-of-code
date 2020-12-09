import re

with open('assets/problem008.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

instructions = []
for line in lines:
    parts = re.match(r'^([^\s]+) (.+)$', line)
    instructions.append({'operation': parts[1], 'value': int(parts[2])})

accumulated = 0
visited = set()
line = 0
while line not in visited:
    visited.add(line)
    instruction = instructions[line]

    if 'acc' == instruction['operation']:
        accumulated += instruction['value']
        line += 1
    if 'jmp' == instruction['operation']:
        line += instruction['value']
    if 'nop' == instruction['operation']:
        line += 1

print('Accumulated before infinite loop: {}.'.format(accumulated))
