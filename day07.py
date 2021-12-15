from typing import List

with open('assets/day07.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

positions = [int(position) for position in lines[0].split(',')]


def _create_list() -> List[int]:
    return [0] * (max(positions) + 1)


vessels = _create_list()
for position in positions:
    vessels[position] += 1

constant_rates = _create_list()
for i in range(len(vessels)):
    constant_rates[i] = i

growing_rates = _create_list()
for i in range(1, len(vessels)):
    growing_rates[i] = i + growing_rates[i - 1]

constant_costs = _create_list()
growing_costs = _create_list()
for i in range(len(vessels)):
    for j in range(len(vessels)):
        steps = abs(i - j)
        constant_costs[i] += constant_rates[steps] * vessels[j]
        growing_costs[i] += growing_rates[steps] * vessels[j]

print(f"Minimum required fuel with constant rate: {min(constant_costs)}")
print(f"Minimum required fuel with growing rate: {min(growing_costs)}")
