class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age


p = Person('Mike', 30)
# print(p.name)
# print(p.age)

choice = input("Which column do you want to access ?")

# if choice == "name":
#    print(p.name)
# elif choice == "age":
#    print(p.age)
# else:
#    print("Not found")

print(getattr(p, choice, 'Not found'))

choice = input("Which column do you want to change ? ")
value = input("To what value ? ")
setattr(p, choice, value)
print(p.age)
print(p.name)

