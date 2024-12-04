with open('assets/day02.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

reports = [[int(level) for level in line.split(' ')] for line in lines]

safe_reports = 0
for report in reports:
    if len(set(report)) != len(report):
        continue

    base = ''.join([str(level) for level in report])
    ascending = ''.join([str(level) for level in sorted(report)])
    descending = ''.join([str(level) for level in sorted(report, reverse=True)])

    if base != ascending and base != descending:
        continue

    valid = 0
    for i in range(0, len(report) - 1):
        a = report[i]
        b = report[i + 1]

        if 1 <= max(a, b) - min(a, b) <= 3:
            valid += 1

    if valid == len(report) - 1:
        safe_reports += 1

print(f'Number of safe reports: {safe_reports}')
