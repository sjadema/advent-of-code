with open('assets/day06.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

states = {state: 0 for state in range(8)}
for state in [int(state) for state in lines[0].split(',')]:
    states[state] += 1


def simulate_fish(days: int) -> int:
    current_states = {state: amount for state, amount in states.items()}

    while 0 < days:
        next_states = {state: 0 for state in range(8)}
        for state, amount in current_states.items():
            if 0 == amount:
                continue

            next_state = state - 1
            if -1 == next_state:
                next_state = 6
                next_states[8] = amount

            next_states[next_state] += amount

        current_states = {state: amount for state, amount in next_states.items()}
        days -= 1

    return sum(current_states.values())


print(f"Number of fish after 80 days: {simulate_fish(80)}")
print(f"Number of fish after 256 days: {simulate_fish(256)}")
