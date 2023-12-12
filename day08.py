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

current_names = [name for name in nodes.keys() if name[-1] == 'A']
target_names = [name for name in nodes.keys() if name[-1] == 'Z']

intervals = [0] * 6
step = 0
while not all(intervals):
    direction = directions[step % len(directions)]

    current_nodes = [nodes[current_name] for current_name in current_names]
    current_names = []

    for current_node in current_nodes:
        name = current_node[direction_positions.index(direction)]

        current_names.append(name)

    step += 1
    for i in range(len(current_names)):
        current_name = current_names[i]
        if current_name[-1] == 'Z':
            intervals[i] = step


def lcm(a: int, b: int) -> int:
    largest, smallest = max(a, b), min(a, b)

    def gcd(largest: int, smallest: int) -> int:
        if smallest == 0:
            return largest

        return gcd(smallest, largest % smallest)

    return smallest * (largest // gcd(largest, smallest))


k = 1
for interval in intervals:
    k = lcm(k, interval)

print(f'Nodes **Z reached simultaneously in {k} steps')
