import re
from util.screen import Screen

file = open('assets/problem8.txt', 'r')
lines = file.readlines()

methods = {
    'draw_rect': {
        'pattern': '^(?P<operation>rect)\s(?P<width>[\d]+)x(?P<height>[\d]+)$',
        'groups': ['width', 'height'],
    },
    'rotate_row': {
        'pattern': '^(?P<operation>rotate row)\sy=(?P<row>[\d]+)\sby\s(?P<amount>[\d]+)$',
        'groups': ['row', 'amount'],
    },
    'rotate_col': {
        'pattern': '^(?P<operation>rotate column)\sx=(?P<column>[\d]+)\sby\s(?P<amount>[\d]+)$',
        'groups': ['column', 'amount']
    },
}

operations = []
for line in lines:
    operation = {
        'method': '',
        'arguments': []
    }

    for method, settings in methods.items():
        match = re.search(settings['pattern'], line.replace('\n', ''))
        if match:
            operation['method'] = method
            for group in settings['groups']:
                operation['arguments'].append(int(match.group(group)))

            break

    operations.append(operation)


screen = Screen(50, 6)
for operation in operations:
    method = getattr(screen, operation['method'])
    method(operation['arguments'][0], operation['arguments'][1])


print('Number of active pixels is: ', screen.get_active())
print(screen)
