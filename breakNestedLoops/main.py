for i in range(10):
    #  if i == 5:
    #    continue
    for j in range(20):
        print(f'{i=}, {j=}')
        if i + j == 10:
            print("Condition met...break")
            break
    else:
        continue
    break

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

for row in matrix:
    for element in row:
        print(element)
        if element == 11:
            print('Found 11....quitting')
            break
    else:
        continue
    break
