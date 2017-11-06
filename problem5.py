import hashlib
import sys

# Disable fast for 'fancy' cracking animation
fast = True
door_id = 'cxdnnyjw'

index = 0
password = ''
while len(password) < 8:
    message = door_id + str(index)
    digest = hashlib.md5(message.encode()).hexdigest()

    if '00000' == digest[0:5]:
        password += digest[5]

    if not fast:
        screen_possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'a', 'b', 'c', 'd', 'e', 'f']
        char_shown = screen_possibilities[index % len(screen_possibilities)]

        line = str(char_shown) + '*******'
        screen_line = password + line

        sys.stdout.flush()
        sys.stdout.write("Password: \"%s\"\r" % ''.join(screen_line[0:8]))

    index += 1

print('Password: "%s" (solved)' % password)

index = 0
password = ['*'] * 8
cracked_length = 0
while cracked_length < 8:
    message = door_id + str(index)
    digest = hashlib.md5(message.encode()).hexdigest()

    try:
        if '00000' == digest[0:5] and 0 <= int(digest[5]) <= 7 and password[int(digest[5])] == '*':
            password[int(digest[5])] = digest[6]
            cracked_length += 1

    except ValueError:
        pass

    if not fast:
        sys.stdout.write("Password: \"%s\"\r" % ''.join(password))
        sys.stdout.flush()

    index += 1

print('Password: "%s" (solved)' % ''.join(password))
