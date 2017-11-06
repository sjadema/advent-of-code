file = open('assets/problem3.txt', 'r')
lines = file.readlines()

triangles = []
for line in lines:
    sides = [x for x in line.replace('\n', '').split(' ') if '' != x]
    triangles.append((int(sides[0]), int(sides[1]), int(sides[2])))

valid = 0
for triangle in triangles:
    sides = sorted(triangle)
    if sides[0] + sides[1] > sides[2]:
        valid += 1

print('Horizontal number of triangles: ', valid)

vertical_triangles = []
for index in range(0, len(triangles), 3):
    vertical_triangles.append((triangles[index][0], triangles[index + 1][0], triangles[index + 2][0]))
    vertical_triangles.append((triangles[index][1], triangles[index + 1][1], triangles[index + 2][1]))
    vertical_triangles.append((triangles[index][2], triangles[index + 1][2], triangles[index + 2][2]))

valid = 0
for triangle in vertical_triangles:
    sides = sorted(triangle)
    if sides[0] + sides[1] > sides[2]:
        valid += 1

print('Vertical number of triangles: ', valid)
