import math

name = 'Mike'


def hello(msg):
    return msg


def mySquare(num):
    return num ** 2


print('Hello ' + name)
print(f'Hello {name} !')
print(f'Hello {10 / math.pi} !')
print(f'Hello {hello("Paul...")}')

print('Here is a calc 20 + 40 = ' + str(20 + 40))
print(f'Here is a calc 20 + 40 = {20 + 40}')

print(f'Here is a calc {20 + 40 = }')
print(f'{hello("Test") = }')

value = 10
print(f'Data: value is {value = }')

print(f'Here is call {mySquare(4) = }')

for i in range(10):
    value = i * mySquare(i)
    print(f'[DEBUG] {i = }, {mySquare(i) = }')
