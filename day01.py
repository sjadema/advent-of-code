import re

with open('assets/day01.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

calibrations_values = []
for line in lines:
    value = re.sub('\D', '', line)
    if '' == value:
        continue

    calibrations_values.append(int(value[0] + value[-1]))

print(f'''Sum of calibration values: {sum(calibrations_values)}''')

numbers = [str(number) for number in range(1, 10)]
letters = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
numbers_as_int = dict(zip(numbers, letters))
numbers_as_str = dict(zip(letters, numbers))

calibrations_values = []
for line in lines:
    prepared_line = line.translate(str.maketrans(numbers_as_int))

    capture_group = '|'.join(letters)

    first_number = re.search(f'''({capture_group})''', prepared_line).group()
    last_number = re.search(f'''({capture_group[::-1]})''', prepared_line[::-1]).group()[::-1]

    calibrations_values.append(int(numbers_as_str[first_number] + numbers_as_str[last_number]))

print(f'''Sum of calibration values: {sum(calibrations_values)}''')
