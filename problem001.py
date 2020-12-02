with open('assets/problem001.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]

expenses = [int(expense) for expense in lines]
for i in range(0, len(expenses)):
    for j in range(i + 1, len(expenses)):
        if 2020 == expenses[i] + expenses[j]:
            print('Double product is {}.'.format(expenses[i] * expenses[j]))

        for k in range(j + 1, len(expenses)):
            if 2020 == expenses[i] + expenses[j] + expenses[k]:
                print('Triple product is {}.'.format(expenses[i] * expenses[j] * expenses[k]))
