"""Takes in a number n, returns the square of n"""


class MyPerson:
    """Takes in a number n, returns the square of n"""
    def __init__(self, name, age, gender):
        """Takes in a number n, returns the square of n"""
        self.name = name
        self.age = age
        self.asked_for_name = False
        self.gender = gender

    def get_name(self):
        """Takes in a number n, returns the square of n"""
        self.asked_for_name = True
        return self.name

    def dump(self):
        """Takes in a number n, returns the square of n"""
        print(self.name, self.age, self.gender)


print(MyPerson("Paul", 20, "m").get_name())
print(print.__doc__)
