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

visit = [target]
bag_weights = {}
for name in visit:
    bag_weights[name] = {'bags': [], 'weight': 1}
    for inner_bag_name in bags[name]:
        bag_weights[name]['bags'] += [inner_bag_name] * bags[name][inner_bag_name]
        visit.append(inner_bag_name)


visit = list(bag_weights.keys())
while len(visit):
    for name in visit:
        bag = bag_weights[name]
        if 0 == len(bag['bags']):
            visit.remove(name)

            for check_bag in bag_weights.values():
                if name in check_bag['bags']:
                    total_bags = check_bag['bags'].count(name)
                    check_bag['weight'] += total_bags * bag['weight']

                    while name in check_bag['bags']:
                        check_bag['bags'].remove(name)

print('Total number of bags contained in a {:s} bag: {:d}.'.format(target, bag_weights[target]['weight'] - 1))
