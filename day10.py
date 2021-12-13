with open('assets/day10.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]


def syntax_error(line: str) -> tuple:
    pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}

    state = []
    for c in line:
        if c in pairs:
            state.append(pairs[c])
        elif c != state[-1]:
            return 'corrupt', c, f"Expected {state[-1]}, but found {c} instead."
        else:
            state.pop()

    return 'incomplete', ''.join(reversed(state)), f"Complete by adding {''.join(reversed(state))}"


syntax_errors = [syntax_error(line) for line in lines]

corrupted = [syntax_error[1] for syntax_error in syntax_errors if 'corrupt' == syntax_error[0]]
penalties = {')': 3, ']': 57, '}': 1197, '>': 25137}

print(f"Corrupted syntax error score: {sum([penalties[c] for c in corrupted])}")

incomplete = [syntax_error[1] for syntax_error in syntax_errors if 'incomplete' == syntax_error[0]]
penalties = {')': 1, ']': 2, '}': 3, '>': 4}

scores = []
for missing in incomplete:
    score = 0
    for c in missing:
        score *= 5
        score += penalties[c]

    scores.append(score)

print(f"Missing syntax error score: {sorted(scores)[len(scores) // 2]}")
