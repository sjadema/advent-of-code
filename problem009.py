from util.intcode import IntCode

with open('assets/problem009.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

instructions = []
for line in lines:
    instructions = [int(code) for code in line.split(',')]

inputs = [1]

# instructions = [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99]
# instructions = [1102, 34915192, 34915192, 7, 4, 7, 99, 0]
# instructions = [104, 1125899906842624, 99]
# inputs = []

program = IntCode(instructions, inputs)

print('BOOST code: {}.'.format(program.run().get_output()))
