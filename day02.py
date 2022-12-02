with open('assets/day02.txt', 'r') as file:
    matches = [line for line in file.read().splitlines()]

shapes = {'A': 1, 'B': 2, 'C': 3}
shapes = shapes | dict(zip(['X', 'Y', 'Z'], shapes.values()))

scores = []
for match in matches:
    person_a, person_b = tuple(match.split(' '))
    score = {'shape': shapes[person_b]}

    weights = {'person_a': ['C', 'A', 'B'], 'person_b': ['Z', 'X', 'Y']}
    weight_a, weight_b = weights['person_a'].index(person_a), weights['person_b'].index(person_b)

    points = 0
    if weight_a == weight_b:
        points = 3
    elif (weight_a + 1) % 3 == weight_b:
        points = 6

    score['points'] = points
    scores.append(score)

print(f'''Total score: {sum([sum(score.values()) for score in scores])}''')


#
# calories_per_elf = ' '.join(calories).split('  ')
#
# total_calories_per_elf = []
# for elf in calories_per_elf:
#     total_calories_per_elf.append(sum([int(calorie) for calorie in elf.split(' ')]))
#
# print(f'''Maximum total amount of calories: {max(total_calories_per_elf)}''')
#
# ordered_calories = sorted(total_calories_per_elf, reverse=True)
#
# print(f'''Top 3 of calories: {sum(ordered_calories[0:3])}''')
