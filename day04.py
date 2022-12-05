with open('assets/day04.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

assignment_collection = []
for line in lines:
    elfs = line.split(',')

    assignments = []
    for elf in elfs:
        boundaries = tuple([int(boundary) for boundary in elf.split('-')])
        assignments.append(set(range(boundaries[0], boundaries[1] + 1)))

    assignment_collection.append(tuple(assignments))

overlapping_assignments = intersecting_assignments = 0
for assignments in assignment_collection:
    elf_a, elf_b = assignments
    if len(elf_b) == len(elf_a.intersection(elf_b)) or len(elf_a) == len(elf_b.intersection(elf_a)):
        overlapping_assignments += 1
    elif elf_a.intersection(elf_b):
        intersecting_assignments += 1

print(f'''Number of overlapping assignments: {overlapping_assignments}''')
print(f'''Number of intersecting assignments: {overlapping_assignments + intersecting_assignments}''')
