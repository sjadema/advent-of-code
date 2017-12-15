with open('assets/problem10.txt', 'r') as file:
    lengths = [int(length) for length in file.read().strip().split(',')]

elements = list(range(256))
current_position = skip_size = 0

for i in range(len(lengths)):
    length = lengths[i]

    # Todo: Do this in 1 loop?
    sub_elements = []
    for j in range(current_position, current_position + length):
        sub_elements.append(elements[j % len(elements)])

    twisted = sub_elements[::-1]
    for j in range(len(twisted)):
        elements[(j + current_position) % len(elements)] = twisted[j]

    current_position += (length + skip_size) % len(elements)
    skip_size += 1

print('Multiple: ', elements[0] * elements[1])

with open('assets/problem10.txt', 'r') as file:
    asciis = [ord(char) for char in file.read().strip()]

hard_coded = [17, 31, 73, 47, 23]
asciis += hard_coded

elements = list(range(256))
current_position = skip_size = 0
for i in range(0, 64):
    for j in range(len(lengths)):
        length = lengths[j]

        # Todo: Do this in 1 loop?
        sub_elements = []
        for k in range(current_position, current_position + length):
            sub_elements.append(elements[k % len(elements)])

        twisted = sub_elements[::-1]
        for k in range(len(twisted)):
            elements[(k + current_position) % len(elements)] = twisted[k]

        current_position += (length + skip_size) % len(elements)
        skip_size += 1

blocks = []
for i in range(0, len(elements), 16):
    block = elements[i:i+16]


    blocks.append(block)

print(blocks)



print(elements, len(elements))
