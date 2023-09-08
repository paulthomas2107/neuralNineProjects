import pickle
import dill
import threading


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_older(self, years):
        self.age += years

    def __repr__(self):
        return f'{self.name} ({self.age})'


p = Person('Mike', 20)
p.get_older(10)
print(p)

with open('person.pkl', 'wb') as f:
    pickle.dump(p, f)

with open('person.pkl', 'rb') as f:
    print(pickle.load(f))

with open('person2.dil', 'wb') as f:
    dill.dump(p, f)

with open('person2.dil', 'rb') as f:
    print(dill.load(f))

my_square = lambda x: x ** 2
with open('square.pkl', 'wb') as f:
    dill.dump(my_square, f)
with open('square.pkl', 'rb') as f:
    my_square = dill.load(f)
print(my_square(10))


def outer(x):
    def inner(y):
        return x + y
    return inner


add_20 = outer(20)

with open('add_20.dil', 'wb') as f:
    dill.dump(add_20, f)
with open('add_20.dil', 'rb') as f:
    add_20 = dill.load(f)
print(add_20(15))


class MyClass:

    def __init__(self, initial_value):
        self.value = initial_value
        self.lock = threading.Lock()

    def increase(self, by):
        self.lock.acquire()
        self.value = by
        self.lock.release()

    def lock_value(self):
        self.lock.acquire()

    def unlock_value(self):
        self.lock.release()


myObj = MyClass(0)
myObj.increase(20)
myObj.lock_value()

with open('myObj.pkl', 'wb') as f:
    dill.dump(myObj, f)
with open('myObj.pkl', 'rb') as f:
    myObj = dill.load(f)

myObj.unlock_value()
myObj.increase(10)
