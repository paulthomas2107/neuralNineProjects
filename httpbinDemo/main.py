import requests

BASE_URL = 'https://httpbin.org'

response = requests.get(BASE_URL + "/get?test=hello&other=paul  ",
                        headers={'User-Agent': 'something else'})
response = response.json()
print(response)

data = {'data1': 'Hello', 'data2': 'Paulie'}
response = requests.post(BASE_URL + "/post", data)
response = response.json()
print(response)

response = requests.get(BASE_URL + "/status/200")
print(response)
response = requests.get(BASE_URL + "/status/304")
print(response)
response = requests.get(BASE_URL + "/status/404")
print(response)

username = 'testuser'
password = 'testpass'
response = requests.get(BASE_URL + f'/basic-auth/{username}/{password}',
                        auth=(username, password))
response = response.json()
print(response)

TOKEN = 'An example bullshit token'
headers = {'Authorization': f'Bearer {TOKEN}'}
response = requests.get(BASE_URL + '/bearer', headers=headers)
if response.status_code == 200:
    response = response.json()
    print(response)
else:
    print('Auth failed')

TOKEN = 'Another example bullshit token'
headers = {'Authorization': f'Hello {TOKEN}'}
response = requests.get(BASE_URL + '/bearer', headers=headers)
if response.status_code == 200:
    response = response.json()
    print(response)
else:
    print('Auth failed')

cookies = {'cookies': 'working'}
response = requests.get(BASE_URL + "/cookies", cookies=cookies)
response = response.json()
print(response)

response = requests.get(BASE_URL + "/cookies/set/test/paul")
response = response.json()
print(response)

s = requests.session()
response = s.get(BASE_URL + "/cookies/set/test/paul")
response = response.json()
print(response)
print(s.cookies)


# n = input("How many times do you want to be redirected ?")
n = 1
response = requests.get(BASE_URL + f'/redirect/{n}')
response = response.json()
print(response)

# n = input("How many times do you want to be redirected ?")
n = 1
response = requests.get(BASE_URL + f'/redirect-to?url=https://neuralnine.com')
print(response.text)

response = requests.get(BASE_URL + '/delay/5', timeout=2)
response = response.json()
print(response)