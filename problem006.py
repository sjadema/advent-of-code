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

center = set(orbit_map.keys()).difference(set(orbiting))


print(center)
