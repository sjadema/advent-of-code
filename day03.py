import string

with open('assets/day03.txt', 'r') as file:
    rucksacks = [line for line in file.read().splitlines()]

matching_items = []
for rucksack in rucksacks:
    items_per_compartment = len(rucksack) // 2
    matching_item = set(rucksack[0:items_per_compartment]).intersection(set(rucksack[items_per_compartment:])).pop()
    matching_items.append(matching_item)

scores = list(string.ascii_lowercase + string.ascii_uppercase)

print(f'''Matching items priorities: {sum([scores.index(matching_item) + 1 for matching_item in matching_items])}''')
