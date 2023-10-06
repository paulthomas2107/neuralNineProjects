
from icecream import ic


def myFunction(a, b, c):
    for _ in range(10):
        print(a)
        print(b)
        print(a == b)
        print(type(a))
        print(type(b))
        if a == b:
            pass
        else:
            if c % 2 == 0:
                pass
            else:
                pass


def add(x, y):
    return x + y


ic(add(10, 20))
ic(add(40, 20))
ic(add(30, 70))
ic(add(10, 60))
ic(add(10, 10))
ic(add(20, 20))

res = ic(add(10, 10))
print(res)

data = {'data': [ 1, 2, 3, 4, 5], 'labels': ['a', 'b', 'c', 'd', 'e']}
print(data['data'][2])
ic(data['data'][2])


def func2(value):
    if value % 2 == 0:
        ic()
        return True
    else:
        ic()
        return False


func2(10)
func2(23)
func2(12)

ic.disable()

func2(10)
func2(23)
func2(12)

ic.enable()

func2(10)
func2(23)
func2(12)


def outputToFile(text):
    with open('debug.txt', 'a') as f:
        f.write(text + "\n")


ic.configureOutput(prefix='Debug| ', outputFunction=outputToFile, includeContext=True)
ic(add(10, 11))
