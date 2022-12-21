import yaml
data = {
    "name": "Paul",
    "age": 33,
    "languages": ['Java', 'Python', 'C++'],
    "address": {
        "city": "Manchester",
        "zip": "CA90210"
    }
}

with open ("file.yml", "w") as f:
    yaml.dump(data, f, default_flow_style=False)
