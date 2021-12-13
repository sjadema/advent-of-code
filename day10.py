with open('assets/day10.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]


def _get_states() -> dict:
    return {'(': ')', '[': ']', '{': '}', '<': '>'}


def syntax_error_score(line: str) -> int:
    states = _get_states()
    scores = {')': 3, ']': 57, '}': 1197, '>': 25137}

    state = []
    for c in line:
        if c in states:
            state.append(states[c])
        elif c != state[-1]:
            return scores[c]
        else:
            state.pop()

    return 0


score = 0
for line in lines:
    score += syntax_error_score(line)

print(f"Syntax error score: {score}")
