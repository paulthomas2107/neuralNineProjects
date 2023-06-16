import random
import requests

# random library
random_number = random.randint(0, 10)
print(random_number)

# random number service
url = "https://www.random.org/integers/?num=1&min=0&max=100&col=5&base=10&format=plain&rnd=new"
number = requests.get(url)
print(int(number.text))

# one request per minute
response = requests.get("https://qrng.anu.edu.au/API/jsonI.php?length=1&type=uint16")
print(response.text)
data = response.json()
random_int = data['data'][0]
print(random_int)
