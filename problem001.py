with open('assets/problem001.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

fuels = []
for line in lines:
    fuels.append(int(line) // 3 - 2)

print('Fuel required is {}.'.format(sum(fuels)))

def calculate_fuel(mass: int) -> int:
    fuel = max(mass // 3 - 2, 0)
    if fuel > 0:
        fuel += calculate_fuel(fuel)

    return fuel

fuels = []
for line in lines:
    fuels.append(calculate_fuel(int(line)))

print('Adjusted fuel required is {}.'.format(sum(fuels)))
