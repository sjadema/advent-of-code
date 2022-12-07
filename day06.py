with open('assets/day06.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

datastream = lines[0]
for i in range(len(datastream)):
    packet = set(list(datastream[i:i + 4]))
    if len(packet) == 4:
        print(f'''Packet start: {i + 4}''')
        break
