"""
In this project we will create a rain alert app that send sms to user about rainy weather
"""
import requests

# fetching a data from openweather api
parameters = {
    "lat": 28.4089,
    "lon": 77.3178,
    "appid": "3f236668391a99c0ffd3ce9bbc91594f"
}

URL = "https://api.openweathermap.org/data/2.5/onecall"
response = requests.get(url=URL, params=parameters)
response.raise_for_status()  # handle http exceptions
data = response.json()  # extracting a json data
print(data)