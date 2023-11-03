from functools import cached_property
import requests


class User:
    def __init__(self, user_id):
        self.user_id = user_id
        self.api_url = f'http://localhost:5000/users/{user_id}'

    @cached_property
    def data(self):
        print('Fetching user data')
        response = requests.get(self.api_url)
        response.raise_for_status()
        return response.json()

    @property
    def username(self):
        return self.data['username']

    @property
    def email(self):
        return self.data['email']


user = User(12345)
print('Username: ', user.username)
print('Email`: ', user.email)

print('Username: ', user.username)
print('Email`: ', user.email)