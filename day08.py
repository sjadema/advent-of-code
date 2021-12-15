with open('assets/day08.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

segments = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
unique_segments = [number for number in segments if 1 == segments.count(number)]

outputs = [line.split('|')[1].strip() for line in lines]

unique_occurrences = 0
for output in outputs:
    for digit in output.split(' '):
        if len(digit) in unique_segments:
            unique_occurrences += 1

print(f"Unique segment occurrences: {unique_occurrences}")
