from functools import reduce

with open('assets/problem005.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

boarding_passes = []
for line in lines:
    row = int(line[0:7].replace('F', '0').replace('B', '1'), 2)
    column = int(line[7:].replace('L', '0').replace('R', '1'), 2)
    boarding_passes.append([row, column])

combined = [reduce(lambda r, c: r * 8 + c, boarding_pass) for boarding_pass in boarding_passes]

print('Highest seating ID: {}.'.format(max(combined)))
