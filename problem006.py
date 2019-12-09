from util.node import Node

with open('assets/problem006.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

nodes = {}
for line in lines:
    masses = line.split(')')

    for mass in masses:
        if mass not in nodes:
            nodes[mass] = Node(mass)

for line in lines:
    masses = line.split(')')

    nodes[masses[0]].add_child(nodes[masses[1]])

total_depth = 0
for node in nodes.values():
    total_depth += node.depth()

print('Total number of orbits: {}.'.format(total_depth))

ancestors_you = set([node.value for node in nodes['YOU'].get_ancestors()])
ancestors_san = set([node.value for node in nodes['SAN'].get_ancestors()])
ancestors_common = ancestors_you.intersection(ancestors_san)

difference_you = ancestors_you.difference(ancestors_common)
difference_san = ancestors_san.difference(ancestors_common)

print('Total number of transfers: {}.'.format(len(difference_you) + len(difference_san)))
