import operator
from typing import List, Dict

with open('assets/day11.txt', 'r') as file:
    lines = [list(line) for line in file.read().splitlines()]


def inflate_galaxies(scale: int) -> List[tuple]:
    if scale < 1:
        raise Exception("Can't deflate galaxies!")

    scale -= 1

    def inflate_axis(axis: str, galaxies: List[List[str]], scale: int) -> Dict[tuple[int, int], int]:
        inflation_map, offset = {}, 0

        for i in range(len(galaxies)):
            if set(list(galaxies[i])) == {'.'}:
                offset += 1
                continue

            for j in range(len(galaxies[i])):
                if galaxies[i][j] == '#':
                    point = (j, i) if axis == 'y' else (i, j)
                    inflation_map[point] = i + offset * scale

        return inflation_map

    y_axis = inflate_axis('y', lines, scale)
    transposed = [[lines[y][x] for y in range(len(lines))] for x in range(len(lines[0]))]
    x_axis = inflate_axis('x', transposed, scale)

    return [(x_axis[point], y_axis[point]) for point in x_axis.keys()]


def calculate_distances(galaxies: List[tuple]) -> int:
    distances = 0
    for i in range(len(galaxies)):
        for j in range(i, len(galaxies)):
            distance = tuple(map(operator.sub, galaxies[i], galaxies[j]))
            distances += abs(distance[0]) + abs(distance[1])

    return distances


print(f'Sum of shortest paths with 2 inflation: {calculate_distances(inflate_galaxies(2))}')
print(f'Sum of shortest paths with 1000000 inflation: {calculate_distances(inflate_galaxies(1000000))}')
