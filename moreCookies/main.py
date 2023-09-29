import requests

s = requests.session()

login_url = 'http://localhost:5000/login'
login_data = {'username': 'testuser', 'password': 'testpass'}

res = s.post(login_url, json=login_data)

saved_cookies = res.cookies
print(saved_cookies)

if res.json().get('success'):
    print("Login successful !")
else:
    print("Login failed !")


protected_url = 'http://localhost:5000/protected'

res = s.get(protected_url, cookies=saved_cookies)

if res.json().get('access'):
    print('Access granted !')
else:
    print('Access denied !')