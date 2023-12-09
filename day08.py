import re

with open('assets/day08.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

directions = lines[0]
direction_positions = ['L', 'R']

nodes = {}
for line in lines[2:]:
    name, value = line.split(' = ')
    nodes[name] = tuple(re.findall(r'(\w+)', value))

# current_node = nodes['AAA']
# step = 0
# while current_node != nodes['ZZZ']:
#     direction = directions[step % len(directions)]
#     name = current_node[direction_positions.index(direction)]
#
#     current_node = nodes[name]
#     step += 1
#
# print(f'Node ZZZ reached in {step} steps')

current_names = [name for name in nodes.keys() if name[-1] == 'A']
target_names = [name for name in nodes.keys() if name[-1] == 'Z']

columns = [[]] * len(current_names)


print(columns)

# print(current_names)
# print(target_names)
# exit()


step = 0
while ''.join([current_name[-1] for current_name in current_names]) != 'Z' * len(current_names):
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
            columns[i].append(current_name)

    if step == 10000000:
        break

print(columns)

print(f'Nodes ending in Z reached simultaneous in {step} steps')
