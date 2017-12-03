with open('assets/problem2.txt', 'r') as file:
    rows = [sorted(list(map(int, row.split('\t')))) for row in file.readlines()]

checksum = []
for row in rows:
    checksum.append(abs(row[0] - row[-1]))

print('Checksum rows: ', sum(checksum))

checksum = []
for row in rows:
    row = row[::-1]
    for i in range(len(row)):
        for j in range(i + 1, len(row)):
            if row[i] % row[j] == 0:
                checksum.append(int(row[i] / row[j]))

print('Checksum divisors: ', sum(checksum))
