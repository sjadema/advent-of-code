content = None
with open('assets/problem2.txt', 'r') as file:
    content = file.readlines()

rows = []
for line in content:
    row = line.replace('\n', '').split('\t')
    for i in range(len(row)):
        row[i] = int(row[i])

    rows.append(row)

checksum = []
for row in rows:
    sorted_row = sorted(row)
    checksum.append(abs(sorted_row[0] - sorted_row[-1]))

print('Checksum rows: ', sum(checksum))

checksum = []
for row in rows:
    sorted_row = sorted(row)[::-1]
    for i in range(len(sorted_row)):
        for j in range(i + 1, len(sorted_row)):
            if sorted_row[i] % sorted_row[j] == 0:
                checksum.append(int(sorted_row[i] / sorted_row[j]))

print('Checksum divisors: ', sum(checksum))
