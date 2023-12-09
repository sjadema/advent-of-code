import re

with open('assets/day08.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

directions = lines[0]
direction_positions = ['L', 'R']

nodes = {}
for line in lines[2:]:
    name, value = line.split(' = ')
    nodes[name] = tuple(re.findall(r'(\w+)', value))

name = 'AAA'
step = 0
while name != 'ZZZ':
    direction = directions[step % len(directions)]

    current_node = nodes[name]
    name = current_node[direction_positions.index(direction)]

    step += 1

print(f'Node ZZZ reached in {step} steps')
