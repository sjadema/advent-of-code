from util.intcode import IntCode

with open('assets/problem005.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

instructions = []
for line in lines:
    instructions = [int(code) for code in line.split(',')]

inputs = [1]

program = IntCode(instructions, inputs)
print('Diagnostic code for airco: {}.'.format(program.run().get_output()))

inputs = [5]

program = IntCode(instructions, inputs)
print('Diagnostic code for thermal radiators: {}.'.format(program.run().get_output()))
