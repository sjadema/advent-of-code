import math

with open('assets/day06.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

times = [int(time) for time in lines[0].split(':')[1].strip().split(' ') if time != '']
distances = [int(distance) for distance in lines[1].split(':')[1].strip().split(' ') if distance != '']

winning_distances = []
for i in range(len(times)):
    # We don't want a draw, so increase the minimum required distance
    time, distance = times[i], distances[i] + 1

    # The equation is in the form ax^2 + bx + c with a = -1, b = time & c = -distance
    # Solve both intersections for the required distance using the quadratic formula
    d = time ** 2 - 4 * -1 * -distance
    first = math.ceil((-time + math.sqrt(d)) / (-1 * 2))
    second = math.floor((-time - math.sqrt(d)) / (-1 * 2))

    # Also include the first match
    winning_distances.append(second - first + 1)

print(f'Power of winning distances: {math.prod(winning_distances)}')
