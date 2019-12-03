with open('assets/problem6.txt', 'r') as file:
    coordinates = [([int(coordinate) for coordinate in line.split(', ')]) for line in file.read().splitlines()]

xs = [c[0] for c in coordinates]
x_min = min(xs)
x_max = max(xs)

ys = [c[1] for c in coordinates]
y_min = min(ys)
y_max = max(ys)

grid = [['.' for j in range(y_min, y_max + 1)] for i in range(x_min, x_max + 1)]
for i, coordinate in enumerate(coordinates):
    x = coordinate[0] - x_min
    y = coordinate[1] - y_min

    grid[x][y] = str(i)






print(grid[258 - x_min][50 - y_min])
exit()




print(grid)
exit()


print(y_max)

grid = []
# for i in range(x_min, x_max + 1):
#     for j in range(y_min, y_max + 1):




# print(lines)
#
# for coordinates in lines:
#     xs[] =
#
#
#
#
#
# print(lines)