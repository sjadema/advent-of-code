import re

from util.instruction import Instruction

with open('assets/problem8.txt', 'r') as file:
    rows = [row.strip() for row in file.readlines()]

instructions = []
for row in rows:
    match = re.search('^(?P<register>[\w]+) (?P<operation>[\w]+) (?P<value>[-\d]+) if (?P<condition>.+)$', row)
    register = match.group('register')

    instructions.append(
        Instruction(
            match.group('register'),
            match.group('operation'),
            int(match.group('value')),
            match.group('condition')
        )
    )

registers = {}
for i in range(len(rows)):
    register = instructions[i].get_register()

    if register not in registers:
        registers[register] = 0

max_value = 0
for instruction in instructions:
    operator = instruction.get_operator()
    target_register = registers[instruction.get_target_register()]

    if operator(target_register, instruction.get_target_value()):
        register = instruction.get_register()
        if instruction.get_operation() == 'dec':
            registers[register] -= instruction.get_value()
        else:
            registers[register] += instruction.get_value()

        max_value = max(max_value, max(registers.values()))

print('Max register value: ', max(registers.values()))
print('Max value: ', max_value)
