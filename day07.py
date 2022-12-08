from typing import Generator

with open('assets/day07.txt', 'r') as file:
    output = (line for line in file.read().splitlines())


def create_tree(lines: Generator) -> dict:
    tree = {}

    try:
        while line := next(lines):
            if '$ ls' == line[:4]:
                try:
                    while line := next(lines):
                        if '$' == line[0]:
                            break

                        size, name = line.split(' ')
                        tree[name] = int(size) if size != 'dir' else {}
                except StopIteration:
                    return tree

            if '$ cd ..' == line:
                return tree

            if '$ cd' == line[:4]:
                name = line[5:]
                tree[name] = create_tree(lines)
    except StopIteration:
        return tree


def calculate_size(fs: dict) -> dict:
    directories = {}

    def traverse(directory: dict, prefix: str = '') -> int:
        total_size = 0
        for name, size in directory.items():
            if type(size) == dict:
                name = f'''{prefix}/{name}'''.lstrip('/')

                size = traverse(size, name)
                directories[name] = size

            total_size += size

        return total_size

    traverse(fs)

    return {'/' + directory: size for directory, size in directories.items()}


filesystem = create_tree(output)
sizes = calculate_size(filesystem)

at_most_100k = sum([size for size in sizes.values() if size <= 100000])
print(f'''Total of directories which are at most 100000 in size: {at_most_100k}''')

disk_size, size_required = 70000000, 30000000
size_available = disk_size - sizes['/']
lower_limit = size_required - size_available

removal_candidates = [size for size in sizes.values() if size > lower_limit]
print(f'''Size of directory to remove: {sorted(removal_candidates)[0]}''')
