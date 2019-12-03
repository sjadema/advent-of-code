import math

with open('assets/problem001.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

fuel = []
for line in lines:
    fuel.append(math.floor(int(line) / 3) - 2)

print('Fuel required is {}.'.format(sum(fuel)))

def calculate_fuel(mass: int) -> int:
    fuel = max(math.floor(mass / 3) - 2, 0)
    if fuel > 0:
        fuel += calculate_fuel(fuel)

    return fuel

fuel = []
for line in lines:
    fuel.append(calculate_fuel(int(line)))

print('Adjusted fuel required is {}.'.format(sum(fuel)))

