import time

start = time.process_time()

lower = 146810
upper = 612564

answers = set()
for possibility in range(lower, upper + 1):
    base = [int(c) for c in str(possibility)]
    if base != sorted(base):
        continue

    if len(set(base)) == len(base):
        continue

    for i in range(len(base) - 1):
        double = set(base[i:i + 2])
        if len(double) == 1:
            answers.add(possibility)
            break

print('Possible passwords: {}.'.format(len(answers)))

more_answers = set()
for possibility in answers:
    characters = ([c for c in str(possibility)])
    check = {k: 0 for k in characters}

    for c in str(possibility):
        check[c] += 1

    if 2 in set(check.values()):
        more_answers.add(possibility)

print('Possible stripped passwords: {}.'.format(len(more_answers)))
print(time.process_time() - start)
