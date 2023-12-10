from functools import reduce

with open('assets/day09.txt', 'r') as file:
    lines = [[int(value) for value in line.split(' ')] for line in file.read().splitlines()]

collections = []
for line in lines:
    collection = [[value for value in line]]

    while len(set(values := collection[-1]).difference({0})) != 0:
        new_values = []
        for i in range(1, len(values)):
            new_values.append(values[i] - values[i - 1])

        collection.append(new_values)

    collection.reverse()

    historic_value = reduce(lambda a, b: b - a, [differences[0] for differences in collection])
    future_value = sum([differences[-1] for differences in collection])
    collections.append([historic_value, future_value])

print(f'Sum of future values: {sum([collection[1] for collection in collections])}')
print(f'Sum of historic values: {sum([collection[0] for collection in collections])}')
