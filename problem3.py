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

print(valid)

