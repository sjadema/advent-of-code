with open('assets/day16.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]


def hex2bin(value: str) -> str:
    conversion = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111',
    }

    return ''.join([conversion[char.upper()] for char in value])


def bin2dec(value: str) -> int:
    return int(value, 2)


binaries = [hex2bin(line) for line in lines]

packet_versions = []
for binary in binaries:
    packet_version, packet_type = bin2dec(binary[0:3]), bin2dec(binary[3:6])
    packet_versions.append(packet_version)

    if 4 == packet_type:
        continue





print(f"Sum of all packet versions: {sum(packet_versions)}")
