import datetime as dt
import requests
import sys

VERSION = "2.5"
BASE_URL = "http://api.openweathermap.org/data/" + VERSION + "/weather?"
API_KEY = open('api.key', 'r').read()
CITY = "Manilla"


def kelvinToCelsiusAndFahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9 / 5) + 32
    return celsius, fahrenheit


url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

response = requests.get(url).json()

temp_kelvin = response['main']['temp']
temp_celsius, temp_fahrenheit = kelvinToCelsiusAndFahrenheit(temp_kelvin)
feels_like_kelvin = response['main']['feels_like']
feels_like_celsius, feels_like_fahrenheit = kelvinToCelsiusAndFahrenheit(feels_like_kelvin)
humidity = response['main']['humidity']
wind_speed = response['wind']['speed']
description = response['weather'][0]['description']
sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])

print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)
print(f"Temperature.......in {CITY}:{temp_celsius: .2f}°C or{temp_fahrenheit: .2f}°F")
print(f"Feels like........in {CITY}:{feels_like_celsius: .2f}°C or{feels_like_fahrenheit: .2f}°F")
print(f"Humidity..........in {CITY}:{humidity: .2f}%")
print(f"Wind Speed........in {CITY}:{wind_speed: .2f}m/s")
print(f"General weather...in {CITY}: {description}")
print(f"Sunrise......... .in {CITY}: {sunrise_time} local time")
print(f"Sunset.......... .in {CITY}: {sunset_time} local time")
