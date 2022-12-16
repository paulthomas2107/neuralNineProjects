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
if response.status_code == requests.codes.not_found:
    print("Something not found !")
response = requests.get("https://httpbin.org/status/500")
print(response.status_code)
if response.status_code == requests.codes.internal_server_error:
    print("internal_server_error")

# User Agent
headers = {
    "User-Agent": "Fake Agent/1.1"

}
response = requests.get("https://httpbin.org/user-agent", headers=headers)
print(response.text)
headers = {
    "User-Agent": "Fake Agent/1.1",
    "Accept": "image/jpeg"
}
response = requests.get("https://httpbin.org/image", headers=headers)
with open("myImage.jpeg", "wb") as f:
    f.write(response.content)

# Timeouts
for _ in [1, 2, 3]:
    try:
        response = requests.get("https://httpbin.org/delay/4", timeout=2)
    except:
        continue

# Proxies
proxies = {
    "http": "139.99.237.62:80"
}
response = requests.get("http://httpbin.org/get", proxies=proxies)
print(response.text)
