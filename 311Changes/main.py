import tomllib
from typing import Literal, Self
from enum import Enum, StrEnum, auto


class Class2(Enum):
    RED = 1,
    GREEN = 2,
    BLUE = "Blue"


class Class3(StrEnum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()


print(Class2.BLUE.value)
print(Class3.BLUE.value, Class3.BLUE.name)


def functionLit(query: Literal["a"]):
    print(query)
    pass


class MyClass:
    def __init__(self, name):
        self.name = name

    def myCool(self, parameter: str) -> Self:
        self.name = parameter
        return self


mc = MyClass("PaulT")
new_mc = mc.myCool("Test")
print(new_mc.name)


functionLit("a")


def myFunction():
    numbers = [10, 20, 30, 40, 50]
    divisors = [5, 3, 0, 9, 1]
    return [x / y for x in numbers for y in divisors]


# myFunction()

try:
    print(10 / 2)
except ZeroDivisionError as e:
    """
    e.add_note("Are you sure want to div by 0")
    e.add_note("Are you sure want to div by 0")
    e.add_note("Are you sure want to div by 0")
    """
    raise


with open("settings.toml", "rb") as f:
    data = tomllib.load(f)
print(data)


def functionTypes(parameter: any) -> int:
    return int(parameter)


print(functionTypes(100) + 21)
print(round(functionTypes(7.8) + 21))


