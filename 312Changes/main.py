from typing import TypeVar, Tuple, TypedDict, override

value = 10
# Allows multi f strings
myString = f'Hello Paul - your age is {value} {f'Again: {value}'}'
print(myString)
print("="*80)

# Backslashes allowed
print(f'{"\n".join(["a", "b", "c"])}')
print("="*80)


def myFunction(param1: int):
    return param1 + 10


print(myFunction(21))
print("="*80)

T = TypeVar('T')

"""class DB(T):

    def __init__(self):
        self.entities = List[T] = []

    def add(self, entity: T) -> None:
        self.entities.append(entity)

    def get_all(self) -> List[T]:
        return self.entities

"""


point = Tuple[float, float]
point2 = Tuple[T, T]

type Point = tuple[float, float]
type Point[T] = tuple[T, T]


class Movie(TypedDict):
    name: str
    year: int


class Base:
    def getColor(self) -> str:
        return "Blue"


class GoodChild(Base):
    @override
    def getColor(self) -> str:
        return "Yellow"


class BadChild(Base):
    @override
    def getColour(self) -> str:
        return "Red"


b = BadChild()
print(b.getColor())
print(b.getColour())

b = GoodChild()
print(b.getColor())