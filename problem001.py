with open('assets/problem001.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

expenses = [int(expense) for expense in lines]
for i in range(0, len(expenses)):
    for j in range(i + 1, len(expenses)):
        if 2020 == expenses[i] + expenses[j]:
            print('Product is {}.'.format(expenses[i] * expenses[j]))
            break
