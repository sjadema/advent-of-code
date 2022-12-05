import copy
import re

with open('assets/day05.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

delimiter = lines.index('')

# Build containers
match = re.findall(r'(\d+)', lines[delimiter - 1])
number_of_columns = [int(column) for column in match][-1]

containers = [[] for _ in range(number_of_columns)]
for i in range(delimiter - 2, -1, -1):
    line = lines[i]
    for j in range(0, len(line), 4):
        if container := line[j + 1].strip():
            containers[j // 4].append(container)

# Build moves
moves = []
move_pattern = r'^move (?P<move>\d+) from (?P<from>\d+) to (?P<to>\d+)$'

for i in range(delimiter + 1, len(lines)):
    line = lines[i]
    match = re.match(move_pattern, line)
    moves.append({
        'move': int(match.group('move')),
        'from': int(match.group('from')) - 1,
        'to': int(match.group('to')) - 1,
    })

stacked_containers, queued_containers = copy.deepcopy(containers), copy.deepcopy(containers)
for move in moves:
    amount, source, target = move.values()

    stacked_containers[target] += stacked_containers[source][-amount:][::-1]
    stacked_containers[source] = stacked_containers[source][0:len(stacked_containers[source]) - amount]

    queued_containers[target] += queued_containers[source][-amount:]
    queued_containers[source] = queued_containers[source][0:len(queued_containers[source]) - amount]

print(f'''Top containers with a stack: {''.join([column[-1] for column in stacked_containers])}''')
print(f'''Top containers with a queue: {''.join([column[-1] for column in queued_containers])}''')
