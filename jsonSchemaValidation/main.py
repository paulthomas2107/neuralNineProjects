import json
from jsonschema import validate
from jsonschema.exceptions import ValidationError

with open('person.json') as f:
    document = json.load(f)

with open('person-schema.json') as f:
    schema = json.load(f)


try:
    validate(instance=document, schema=schema)
    print("Validation OK !")
except ValidationError as e:
    print('Validation failed !')
    print(f'Error message ${e.message}')