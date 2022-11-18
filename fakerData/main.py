import random

from faker import Faker
from faker.providers import BaseProvider, DynamicProvider

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

    @staticmethod
    def food_title():
        return "TITLE"


f = Faker()
f.add_provider(PaulProvider)
print(f.food_category())
print(f.food_title())

language_provider = DynamicProvider(
    provider_name="programming_language",
    elements=["Java", "Cobol", "C++", "Python", "JavaScript"]
)

f.add_provider(language_provider)
print(f.programming_language())
