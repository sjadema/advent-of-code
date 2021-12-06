with open('assets/day06.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

states = [int(state) for state in lines[0].split(',')]

days = 80
while 0 < days:
    for i in range(len(states)):
        states[i] -= 1
        if -1 == states[i]:
            states[i] = 6
            states.append(8)

    days -= 1

print(f"Number of fish after 80 days: {len(states)}")
