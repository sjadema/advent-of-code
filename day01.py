import re

with open('assets/day01.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

calibrations_values = []
for line in lines:
    value = re.sub(r'\D', '', line)
    calibrations_values.append(int(value[0] + value[-1]))

print(f'''Sum of calibration values: {sum(calibrations_values)}''')
