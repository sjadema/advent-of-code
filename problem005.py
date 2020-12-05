with open('assets/problem005.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

seating_ids = [int(''.join('1' if c in ['B', 'R'] else '0' for c in boarding_pass), 2) for boarding_pass in lines]

print('Highest seating ID: {}.'.format(max(seating_ids)))

all_seating_ids = list(range(min(seating_ids), max(seating_ids) + 1))
missing_seating_ids = set(all_seating_ids) - set(seating_ids)

print('My seating ID: {}.'.format(missing_seating_ids.pop()))
