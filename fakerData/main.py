import random

from faker import Faker
from faker.providers import BaseProvider

f = Faker(["en_GB", "nl_NL"])



print(f.name())
print(f.address())
print(f.county())
print(f.postcode())
print(f.ipv4_private())
print(f.ipv4_public())
print(f.sentence())
# print(f.zipcode())
print(f.locale())
print(f.license_plate())
print(f.phone_number())


for _ in range(10):
    print(f.unique.random_int(min=200, max=500))

for _ in range(5):
    print(f.bothify(text="????-####-??", letters="ABCXYZ"))

for _ in range(5):
    print(f.hexify(text="MAC: ^^:^^:^^:^^:^^:^^", upper=True))


class PaulProvider(BaseProvider):

    @staticmethod
    def food_category():
        return random.choice(['Chinese', 'Japanese', 'Spanish', 'Indian', 'American', 'Italian'])


f = Faker()
f.add_provider(PaulProvider)
print(f.food_category())
