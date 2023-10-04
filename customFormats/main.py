import math

print(f'My value is {155.464:.2f}')  # 155.46
print(f'My value is {155.464:09}')  # 00155.464


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Hello {self.name} I am {self.age}'

    def __format__(self, format_spec):
        if format_spec == 'name':
            return self.name
        elif format_spec == 'age':
            return str(self.age)
        elif format_spec == 'both':
            return f'{self.name} {self.age}'
        else:
            raise Exception


p = Person('Paul', 21)
print(p)
# print(f'{p:greek}')
print(f'{p:name}')
print(f'{p:age}')
print(f'{p:both}')
# print(f'{p:boxxxxth}')


class Coordinate2D:
    def __init__(self,x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'x = {self.x} y = {self.y}'

    def __format__(self, format_spec):
        if format_spec == 'polar':
            r = math.sqrt(self.x ** 2 + self.y ** 2)
            theta = math.atan2(self.y, self.x)
            return f'r = {r:.2f}, theta = {theta:.2f}'
        return f'x = {self.x} y = {self.y}'


coord2D = Coordinate2D(20, 15)
print(coord2D)
print(f'{coord2D:something}')
print(f'{coord2D:polar}')
print(format(coord2D, 'polar'))