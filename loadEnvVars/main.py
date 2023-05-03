import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()

print(os.getenv("MY_SECRET_KEY"))
print((os.getenv("COMBINED")))
print((os.getenv("MAIL")))

config = dotenv_values('.env')
print(config)
print(config.get("HOST"))