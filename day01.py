with open('assets/day01.txt', 'r') as file:
    calories = [line for line in file.read().splitlines()]

calories_per_elf = ' '.join(calories).split('  ')

total_calories_per_elf = []
for elf in calories_per_elf:
    total_calories_per_elf.append(sum([int(calorie) for calorie in elf.split(' ')]))

print(f'''Maximum total amount of calories: {max(total_calories_per_elf)}''')

ordered_calories = sorted(total_calories_per_elf, reverse=True)

print(f'''Top 3 of calories: {sum(ordered_calories[0:3])}''')
