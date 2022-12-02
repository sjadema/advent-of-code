with open('assets/day02.txt', 'r') as file:
    matches = [line for line in file.read().splitlines()]

matches = [tuple(match.split(' ')) for match in matches]
shapes = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}
weights = {'person_a': ['C', 'A', 'B'], 'person_b': ['Z', 'X', 'Y']}


def calculate_points(person_a: int, person_b: int) -> int:
    if person_a == person_b:
        return 3
    elif (person_a + 1) % 3 == person_b:
        return 6

    return 0


scores = []
for match in matches:
    shape_a, shape_b = match
    weight_a, weight_b = weights['person_a'].index(shape_a), weights['person_b'].index(shape_b)

    scores.append({'score': shapes[shape_b], 'points': calculate_points(weight_a, weight_b)})

print(f'''Total score strategy I: {sum([sum(score.values()) for score in scores])}''')

weights['person_b'] = ['Y', 'Z', 'X']

scores = []
for match in matches:
    shape_a, shape_b = match
    weight_a, weight_b = weights['person_a'].index(shape_a), weights['person_b'].index(shape_b)

    shape_b = weights['person_a'][(weight_a + weight_b) % 3]
    weight_b = weights['person_a'].index(shape_b)

    scores.append({'score': shapes[shape_b], 'points': calculate_points(weight_a, weight_b)})

print(f'''Total score strategy II: {sum([sum(score.values()) for score in scores])}''')
