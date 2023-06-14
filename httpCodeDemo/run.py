import requests

res = requests.get("http://localhost:5000/")

print(res.status_code)