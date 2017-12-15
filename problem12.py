import re

from util.graphnode import GraphNode

with open('assets/problem12.txt', 'r') as file:
    definitions = [row.strip() for row in file.readlines()]

# definitions = [
#     '0 <-> 2',
#     '1 <-> 1',
#     '2 <-> 0, 3, 4',
#     '3 <-> 2, 4',
#     '4 <-> 2, 3, 6',
#     '5 <-> 6',
#     '6 <-> 4, 5',
# ]

graph = {}
for definition in definitions:
    match = re.search('^(?P<program>[\d]+)[^\d]+(?P<connections>[\d,\s]+)$', definition)

    program = match.group('program')
    try:
        node = graph[program]
    except KeyError:
        graph[program] = GraphNode(program)
        node = graph[program]

    for connection in match.group('connections').split(','):
        program = connection.strip()

        try:
            child = graph[program]
        except KeyError:
            graph[program] = GraphNode(program)
            child = graph[program]

        node.add_node(child)

print('Total programs in group "0": ', graph['0'].count_nodes(True))


# groups = {}
# for node in graph.values():
#     groups[node.get_name()] =


# for node in graph.values():
#     print(node.get_name())
#     for child in node.get_nodes():
#         print(child.get_name())
#
#     print()
# print(graph['2'].get_nodes())
