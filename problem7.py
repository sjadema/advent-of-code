import re

file = open('assets/problem7.txt', 'r')
lines = file.readlines()

addresses = []
for line in lines:
    hyper_nets = []
    super_nets = []

    matches = re.finditer('(?P<hyper_net>\[[^\]]+\])|(?P<super_nets>[^[]+)', line.replace('\n', ''))
    for match in matches:
        if match.group('hyper_net') is not None:
            hyper_net = match.group('hyper_net')
            hyper_nets.append(hyper_net[1:len(hyper_net) - 1])
        elif match.group('super_nets') is not None:
            super_nets.append(match.group('super_nets'))

    addresses.append({
        'hyper_nets': tuple(hyper_nets),
        'super_nets': tuple(super_nets),
    })


def has_abba(address_part):
    slices = []
    for i in range(0, len(address_part) - 1):
        slices.append(address_part[i:][0:2])

    for i in range(0, len(slices) - 2):
        if slices[i] != slices[i+2] and slices[i] == slices[i+2][::-1]:
            return True

    return False


tls_total = 0
for address in addresses:
    valid = True
    for hyper_net in address['hyper_nets']:
        if has_abba(hyper_net):
            valid = False
            break

    if not valid:
        continue

    for super_net in address['super_nets']:
        if has_abba(super_net):
            tls_total += 1
            break

print('Valid TLS addresses: ', tls_total)


def get_aba(address_part):
    parts = []
    for i in range(0, len(address_part) - 2):
        parts.append(address_part[i:][0:3])

    patterns = []
    for part in parts:
        if part[0] != part[1] and part[0] == part[2]:
            patterns.append(part)

    return patterns


ssl_total = 0
for address in addresses:
    found = False
    for super_net in address['super_nets']:
        if found:
            break

        aba = get_aba(super_net)
        for pattern in aba:
            if found:
                break

            bab_pattern = pattern[1:3] + pattern[1]

            for hyper_net in address['hyper_nets']:
                match = re.search(bab_pattern, hyper_net)
                if match:
                    ssl_total += 1
                    found = True
                    break

print('Valid SSL addresses: ', ssl_total)
