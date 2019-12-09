with open('assets/problem008.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

image_data = list(lines[0])
data_first = image_data.copy()[::-1]

total_layers = len(data_first) // (6 * 25)

layers = {}
for i in range(total_layers):
    for y in range(6):
        for x in range(25):
            pixel = data_first.pop()

            try:
                layers[i].append(pixel)
            except KeyError:
                layers[i] = [pixel]

checksums = []
for layer in layers:
    data = layers[layer]
    checksums.append(''.join(data).replace('0', ''))

checksums.sort(key=len, reverse=True)
shortest = list(checksums[0])
occurrences = {'1': 0, '2': 0}
for char in shortest:
    occurrences[char] += 1

print('Checksum: {}.'.format(occurrences['1'] * occurrences['2']))
