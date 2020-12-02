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

layer_range = range(99, -1, -1)
data_range = range(6 * 25)

restored = ['0'] * (6 * 25)
for index in data_range:
    for layer in layer_range:
        data = layers[layer]
        pixel = data[index]

        if '2' != pixel:
            restored[index] = pixel

for i in range(0, len(restored), 25):
    print(''.join([str(p).replace('0', ' ').replace('1', 'x') for p in restored[i:i+25]]))
