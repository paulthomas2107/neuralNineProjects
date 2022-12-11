import requests


# GET
params = {
   "name": "Paul",
   "age": 33
}
response = requests.get("https://httpbin.org/get", params=params)
print(response.url)

res_json = response.json()
print(res_json)

# POST
payload = {
   "name": "Paul",
   "age": 33
}
response = requests.post("https://httpbin.org/post", data=payload)
print(response.url)

res_json = response.json()
print(res_json)

# Status Codes
response = requests.get("https://httpbin.org/status/200")
print(response.status_code)
response = requests.get("https://httpbin.org/status/404")
print(response.status_code)



