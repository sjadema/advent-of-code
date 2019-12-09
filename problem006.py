with open('assets/problem006.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

orbit_map = {}
for line in lines:
    objects = line.split(')')

    try:
        orbit_map[objects[0]].append(objects[1])
    except KeyError:
        orbit_map[objects[0]] = [objects[1]]

orbiting = []
for value in orbit_map.values():
    orbiting += value

center = set(orbit_map.keys()).difference(set(orbiting)).pop()

total_orbits = {}


def determine_orbits(start: str, orbits: int = 0) -> None:
    total_orbits[start] = orbits

    masses = orbit_map[start]
    for mass in masses:
        if mass in orbit_map.keys():
            determine_orbits(mass, orbits + 1)
        else:
            total_orbits[mass] = orbits + 1


determine_orbits(center)
print('Total number of orbits: {}.'.format(sum(total_orbits.values())))
