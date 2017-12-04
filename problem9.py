import re

with open('assets/problem9.txt') as file:
    content = file.read().strip()

# content = 'A(1x5)BC'
# content = '(3x3)XYZ'
# content = 'A(2x2)BCD(2x2)EFG'
# content = '(6x1)(1x3)A'
# content = 'X(8x2)(3x3)ABCY'

start_position = 0
while start_position < len(content):
    sliced_content = content[start_position:]

    match = re.search('\((?P<length>[\d]+)x(?P<times>[\d]+)\)', sliced_content)
    if not match:
        break

    length = int(match.group('length'))
    times = int(match.group('times'))

    content_end = match.start()
    uncompressed_start = match.end()

    content_pre = content[0:start_position + content_end]
    uncompressed = sliced_content[uncompressed_start:uncompressed_start + length] * times
    content_post = sliced_content[uncompressed_start + length:]

    content = content_pre + uncompressed + content_post
    start_position = len(content[0:content_end] + uncompressed)

    print(content)

print('Uncompressed content length: ', len(content))


# print(new_string)



