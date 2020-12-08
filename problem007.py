import re

from util.dependency import Vertex, Graph, Resolver

with open('assets/problem007.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

bag_configurations = {}
for line in lines:
    bag = {}
    bag_configuration = re.match(r'^(.+?) bags contain (.+?)\.', line)
    for other_bag in bag_configuration[2].split(','):
        other_bag_configuration = re.match(r' ?(\d+) (.+?) bags?', other_bag)
        if None is not other_bag_configuration:
            bag[other_bag_configuration[2]] = int(other_bag_configuration[1])

    bag_configurations[bag_configuration[1]] = bag

bags = {}
for name in bag_configurations:
    bags[name] = Vertex(name)

    for dependency in bag_configurations[name]:
        if dependency not in bags:
            bags[dependency] = Vertex(dependency)

for name in bag_configurations:
    for dependency in bag_configurations[name]:
        bags[name].add_edge(bags[dependency])

graph = Graph.create(list(bags.values()))

downstream_graph = Graph.filter(graph, [bags['shiny gold']], True)
order = [vertex.name for vertex in Resolver(downstream_graph).resolve()]

print('Total number of bags containing at least one shiny gold bag: {}.'.format(len(order) - 1))
