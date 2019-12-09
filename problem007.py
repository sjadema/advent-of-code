from util.intcode import IntCode

with open('assets/problem007.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

instructions = []
for line in lines:
    instructions = [int(code) for code in line.split(',')]

maximum = 0
for one in range(5):
    for two in range(5):
        for three in range(5):
            for four in range(5):
                for five in range(5):
                    check = [one, two, three, four, five]
                    if len(set(check)) != len(check):
                        continue

                    first = IntCode(instructions, [one, 0])
                    second = IntCode(instructions, [two, int(first.run().get_output())])
                    third = IntCode(instructions, [three, int(second.run().get_output())])
                    fourth = IntCode(instructions, [four, int(third.run().get_output())])
                    fifth = IntCode(instructions, [five, int(fourth.run().get_output())])

                    current = fifth.run().get_output()

                    maximum = max(maximum, int(current))

print('Max thrust: {}.'.format(maximum))


# maximum = 0
# for five in range(5, 10):
#     for six in range(5, 10):
#         for seven in range(5, 10):
#             for eight in range(5, 10):
#                 for nine in range(5, 10):
#                     check = [five, six, seven, eight, nine]
#                     if len(set(check)) != len(check):
#                         continue
#
#                     first = IntCode
