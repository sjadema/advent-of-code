from util.graph import Vertex, Graph

with open('assets/problem010.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

jolts = [0] + sorted([int(line) for line in lines])
jolts += [jolts[-1] + 3]

differences = dict(zip(range(1, 4), [0] * 3))

for i in range(0, len(jolts) - 1):
    differences[jolts[i + 1] - jolts[i]] += 1

print('Difference product: {}'.format(differences[1] * differences[3]))

connections = 0
stripped_jolts = jolts[1:len(jolts) - 1]

# jolts = [0, 1, 4, 5, 6, 7]

cursor = 0
while jolts.index(cursor) < len(jolts) - 1:
    window = list(range(cursor + 1, cursor + 4))
    visible = jolts[jolts.index(cursor) + 1:jolts.index(cursor) + 4]
    # print(window, visible)

    existing = list(set(window).intersection(visible))
    if 1 < len(existing):
        connections += len(existing)

    print(existing)

    cursor = existing[0]

print(connections + 1)
# for i in range(0, len(jolts)):
#     for j in range(i, i + 3):
#
#
#
#
#     for test in [jolt + 3, jolt + 2, jolt + 1]:
#         if test in jolts:






#
#
# vertices = {}
# for jolt in jolts:
# # for jolt in jolts[::-1]:
#     if jolt not in vertices:
#         vertices[jolt] = Vertex(jolt)
#
#     vertex = vertices[jolt]
#
#     for test in [jolt + 1, jolt + 2, jolt + 3]:
#         if test in jolts:
#             if test not in vertices:
#                 vertices[test] = Vertex(test)
#
#             vertex.add_edge(vertices[test])
#
# graph = Graph.create(list(vertices.values()))
# connections = 0
# for jolt in jolts:
#
#
#
#
# jolts_length = len(jolts)
# # connections_one = graph.count_all_paths(vertices[jolts[0]], vertices[jolts[-1]])
# # connections_two = 1
# print(jolts_length, jolts_length // 4)
# connections_one = graph.count_all_paths(vertices[jolts[0]], vertices[jolts[jolts_length // 4]])
# connections_two = graph.count_all_paths(vertices[jolts[jolts_length // 4]], vertices[jolts[jolts_length // 2]])
# connections_three = graph.count_all_paths(vertices[jolts[jolts_length // 2]], vertices[jolts[jolts_length // 4 * 3]])
# connections_four = graph.count_all_paths(vertices[jolts[jolts_length // 4 * 3]], vertices[jolts[-1]])
#
# print(connections_one, connections_two, connections_three, connections_four)
#
# print('Number of distinct connections: {}.'.format(connections_one * connections_two * connections_three * connections_four))
