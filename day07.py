with open('assets/day07.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

positions = [int(position) for position in lines[0].split(',')]
vessels = [0] * (max(positions) + 1)
costs = vessels.copy()

for position in positions:
    vessels[position] += 1

for i in range(len(vessels)):
    for j in range(len(vessels)):
        if i == j:
            continue

        costs[i] += abs(i - j) * vessels[j]

print(f"Minimum required fuel: {min(costs)}")
