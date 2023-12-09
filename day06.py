import math

with open('assets/day06.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

times = [int(time) for time in lines[0].split(':')[1].strip().split(' ') if time != '']
distances = [int(distance) for distance in lines[1].split(':')[1].strip().split(' ') if distance != '']


def solve_equation(time: int, distance: int) -> tuple[int, int]:
    # The equation is in the form ax^2 + bx + c with a = -1, b = time & c = -distance
    a, b, c = -1, time, -distance

    # Solve both intersections for the required distance using the quadratic formula
    discriminant = b ** 2 - 4 * a * c
    first = math.ceil((-b + math.sqrt(discriminant)) / (2 * a))
    second = math.floor((-b - math.sqrt(discriminant)) / (2 * a))

    return first, second


def get_number_of_winning_distances(solutions: tuple[int, int]) -> int:
    # Also include the first match
    return solutions[1] - solutions[0] + 1


winning_distances = []
for i in range(len(times)):
    # We don't want a draw, so increase the minimum required distance
    time, distance = times[i], distances[i] + 1

    solutions = solve_equation(time, distance)
    winning_distances.append(get_number_of_winning_distances(solutions))

print(f'Power of winning distances: {math.prod(winning_distances)}')

time = int(''.join([str(time) for time in times]))
distance = int(''.join([str(distance) for distance in distances]))

# We don't want a draw, so increase the minimum required distance
solutions = solve_equation(time, distance + 1)

print(f'Number of ways to beat the race: {get_number_of_winning_distances(solutions)}')
