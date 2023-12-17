value = 'Hello'

match value:
    case 'Hello':
        print('Yes, Hello')
    case 'Exit':
        exit()
    case _:
        print('Default...')


division_numbers = (5, 2, 2, 0, 2)

match division_numbers:
    case (x, 0):
        print('No div by zero')
    case (x1, y):
        print(f'{x1}/{y} = {x1 / y}')
    case (x2, y, *other) if 0 not in other and y != 0:
        division_result = x / y
        for number in other:
            division_result /= number
        print(division_result)
    case (x3, y, *other) if 0 in other or y == 0:
        print('No div by zero')
    case _:
        print('Invalid....')
