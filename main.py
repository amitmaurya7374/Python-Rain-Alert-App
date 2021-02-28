"""
In this project we will create a rain alert app that send sms to user about rainy weather
"""
import os

import requests
from twilio.http.http_client import TwilioHttpClient
from twilio.rest import Client

from api_key import APIKey

user_account_keys = APIKey()
api_key = user_account_keys.apikey

# for twilio
account_sid = user_account_keys.account_sid
auth_token = user_account_keys.auth_token
from_phone_number = user_account_keys.phone_number
to_phone_number = user_account_keys.to_phone_number

proxy_client = TwilioHttpClient()
proxy_client.session.proxies = {'https': os.environ['https_proxy']}
client = Client(account_sid, auth_token, proxy_client)

# fetching a data from openweather api
parameters = {
    "lat": 28.408913,
    "lon": 77.317787,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

URL = "https://api.openweathermap.org/data/2.5/onecall"
response = requests.get(url=URL, params=parameters)
response.raise_for_status()  # handle http exceptions
weather_data = response.json()  # extracting a json data
hourly_data = weather_data["hourly"]

# print(f"hourly data : {hourly_data}")
first_index_id = hourly_data[0]["weather"]

hourly_weather_key_data = [code["weather"] for code in hourly_data]
hourly_weather_key_data = hourly_weather_key_data[:12]

will_rain = False
for weather_id in range(0, len(hourly_weather_key_data)):
    condition_code = hourly_weather_key_data[weather_id][0]["id"]
    if condition_code < 700:
        will_rain = True

if will_rain:
    message = client.messages \
        .create(
        body="Looks like Today is a rainy day.Remember to carry umberalla",
        from_=from_phone_number,
        to=to_phone_number
    )
    print(message.status)
