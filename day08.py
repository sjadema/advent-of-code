with open('assets/day08.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

collection = []
for line in lines:
    inputs, outputs = tuple(line.split('|'))

    collection.append({
        'input': [digit for digit in inputs.strip().split(' ')],
        'output': [digit for digit in outputs.strip().split(' ')],
    })

segments = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
unique_segments = [number for number in segments if 1 == segments.count(number)]

unique_occurrences = 0
outputs = []
for input_output in collection:
    inputs = sorted(input_output['input'], key=len)
    one, seven, four, eight = tuple([
        set(list(inputs[0])),
        set(list(inputs[1])),
        set(list(inputs[2])),
        set(list(inputs[9])),
    ])

    possibilities = [set(list(inputs[6])), set(list(inputs[7])), set(list(inputs[8]))]
    for possibility in possibilities:
        if 2 == len(eight.difference(four).intersection(possibility)):
            nine = possibility
        elif 2 == len(one.intersection(possibility)):
            zero = possibility
        else:
            six = possibility

    possibilities = [set(list(inputs[3])), set(list(inputs[4])), set(list(inputs[5]))]
    for possibility in possibilities:
        if 4 == len(nine.intersection(possibility)):
            two = possibility
        elif 5 == len(six.intersection(possibility)):
            five = possibility
        else:
            three = possibility

    resolved = [zero, one, two, three, four, five, six, seven, eight, nine]

    output = ''
    for digit in input_output['output']:
        if len(digit) in unique_segments:
            unique_occurrences += 1

        output += str(resolved.index(set(list(digit))))

    outputs.append(int(output))

print(f"Unique segment occurrences: {unique_occurrences}")
print(f"Combined output values: {sum(outputs)}")
