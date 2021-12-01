with open('assets/problem001.txt', 'r') as file:
    depths = [int(line) for line in file.read().splitlines()]

print(depths)

increased = 0
for i in range(1, len(depths)):
    if depths[i] > depths[i - 1]:
        increased += 1

print("Depth increased: {:d} times.".format(increased))

windows = []
for i in range(0, len(depths) - 2):
    window = 0
    for j in range(0, 3):
        window += depths[i + j]

    windows.append(window)

increased = 0
for i in range(1, len(windows)):
    if windows[i] > windows[i - 1]:
        increased += 1

print("Depth windows increased: {:d} times.".format(increased))
