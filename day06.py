with open('assets/day06.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

check_packet_start = check_message_start = True

datastream = lines[0]
for i in range(len(datastream)):
    if check_packet_start:
        packet = set(list(datastream[i:i + 4]))
        if len(packet) == 4:
            print(f'''Packet start: {i + 4}''')
            check_packet_start = False

    if check_message_start:
        packet = set(list(datastream[i:i + 14]))
        if len(packet) == 14:
            print(f'''Message start: {i + 14}''')
            check_message_start = False

    if not check_packet_start and not check_message_start:
        break
