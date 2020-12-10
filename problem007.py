import re

with open('assets/problem007.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

bags = {}
for line in lines:
    bag = {}
    bag_configuration = re.match(r'^(.+?) bags contain (.+?)\.', line)
    for other_bag in bag_configuration[2].split(','):
        other_bag_configuration = re.match(r' ?(\d+) (.+?) bags?', other_bag)
        if None is not other_bag_configuration:
            bag[other_bag_configuration[2]] = int(other_bag_configuration[1])

    bags[bag_configuration[1]] = bag

target = 'shiny gold'
visit = [target]
for name in visit:
    for bag in bags:
        for inner_bag_name in bags[bag]:
            if name == inner_bag_name and bag not in visit:
                visit.append(bag)

visit.remove(target)
print('Total number of bags containing at least one {:s} bag: {:d}.'.format(target, len(visit)))
