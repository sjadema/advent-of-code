with open('assets/day09.txt', 'r') as file:
    lines = [[int(value) for value in line.split(' ')] for line in file.read().splitlines()]

collections = []
for line in lines:
    collection = [[value for value in line]]

    while len(set(values := [value for value in collection[-1]]).difference({0})) != 0:
        new_values = []
        for i in range(1, len(values)):
            new_values.append(values[i] - values[i - 1])

        collection.append(new_values)

    collections.append(collection)

for collection in collections:
    differences = collection[::-1]
    differences[0].append(0)

    for i in range(1, len(differences)):
        difference = differences[i]
        difference.append(difference[-1] + differences[i - 1][-1])

all_differences = [differences[0][-1] for differences in collections]
print(f'Sum of added differences: {sum(all_differences)}')


