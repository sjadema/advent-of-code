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

targets = ['shiny gold']
possible_bags = set(bags.keys())
while len(possible_bags):
    for target in targets:
        visited_bags = []
        for bag in bags:
            if bag in visited_bags:
                continue

            visited_bags.append(bag)
            for containing_bag in bags[bag]:
                if containing_bag == target:
                    targets.append(bag)

        possible_bags = possible_bags.difference(set(visited_bags))

print('Total number of bags containing at least a single bag: {}.'.format(len(set(targets)) - 1))
