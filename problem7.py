import re
from collections import Counter

from util.node import Node

with open('assets/problem7.txt', 'r') as file:
    rows = [row.strip() for row in file.readlines()]

# rows = [
#     'pbga (66)',
#     'xhth (57)',
#     'ebii (61)',
#     'havc (66)',
#     'ktlj (57)',
#     'fwft (72) -> ktlj, cntj, xhth',
#     'qoyq (66)',
#     'padx (45) -> pbga, havc, qoyq',
#     'tknk (41) -> ugml, padx, fwft',
#     'jptl (61)',
#     'ugml (68) -> gyxo, ebii, jptl',
#     'gyxo (61)',
#     'cntj (57)',
# ]

tree = {}
for row in rows:
    match = re.search('^(?P<name>[^\s]+)\s?\((?P<weight>[\d]+)\)', row)
    node = Node(match.group('name'), int(match.group('weight')))
    tree[node.get_name()] = node

for row in rows:
    match = re.search('^(?P<name>[^\s]+)[^-]+->\s(?P<children>[a-z,\s]+)$', row)
    if match:
        node = tree[match.group('name')]
        children = [child.strip() for child in match.group('children').split(',')]
        for child in children:
            node.add_child(tree[child])

source = filter(lambda x: x.get_parent() is None, tree.values()).__next__()
print('Source: ', source.get_name())


def get_imbalanced_child(node: 'Node'):
    weights = {}
    for child in node.get_children():
        weights[child.get_name()] = child.get_weight(True)

    occurrences = Counter(weights.values())
    if len(set(occurrences)) == 1:
        child_weights = []
        child_total_weights = []
        for child in node.get_parent().get_children():
            child_weights.append(child.get_weight())
            child_total_weights.append(child.get_weight(True))

        maximum = max(child_total_weights)
        index = child_total_weights.index(maximum)
        difference = maximum - (min(child_total_weights) % maximum)
        child_weights[index] -= difference

        print('Corrected weight: ', child_weights[index])
        return

    value = [(name, occurrences[name]) for name in sorted(occurrences, key=occurrences.get)][0][0]
    name = list(weights.keys())[list(weights.values()).index(value)]
    return get_imbalanced_child(tree[name])


get_imbalanced_child(source)
