import re

with open('assets/problem008.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

instructions = []
for line in lines:
    parts = re.match(r'^([^\s]+) (.+)$', line)
    instructions.append({'operation': parts[1], 'value': int(parts[2])})


def execute(instructions: list) -> int:
    accumulated = 0
    visited = set()
    line = 0
    while True:
        if line in visited:
            raise ValueError(accumulated)
        if line >= len(instructions):
            return accumulated

        visited.add(line)

        instruction = instructions[line]
        if 'acc' == instruction['operation']:
            accumulated += instruction['value']
            line += 1
        if 'jmp' == instruction['operation']:
            line += instruction['value']
        if 'nop' == instruction['operation']:
            line += 1


try:
    execute(instructions)
except ValueError as e:
    print('Accumulated before infinite loop: {}.'.format(e))


for line in range(0, len(instructions)):
    instruction = instructions[line]

    operation = instruction['operation']
    if ('nop' == operation and 0 != instruction['operation']) or 'jmp' == operation:
        instructions[line]['operation'] = 'nop' if 'jmp' == operation else 'jmp'

        try:
            print('Accumulated after fixed: {}.'.format(execute(instructions)))
            break
        except ValueError:
            instructions[line]['operation'] = operation
