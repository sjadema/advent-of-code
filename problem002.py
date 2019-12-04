from util.intcode import IntCode

with open('assets/problem002.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

instructions = []
for line in lines:
    instructions = [int(code) for code in line.split(',')]

instructions[1] = 12
instructions[2] = 2

program = IntCode(instructions)
print('After executing: {}.'.format(program.run()))

try:
    answer = 19690720
    for noun in range(0, 100):
        for verb in range(0, 100):
            instructions[1] = noun
            instructions[2] = verb

            program = IntCode(instructions)
            if answer == program.run():
                raise StopIteration(noun, verb)

except StopIteration as e:
    args = e.args
    print('After executing: {}.'.format(100 * args[0] + args[1]))
