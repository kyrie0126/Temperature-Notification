import requests
from temp_convert import kelvin_to_fahrenheit, time_convert
import datetime as dt
import pytz
from twilio.rest import Client

# -------------------- API Call --------------------
api_id = "your_api_id"
api_url = "https://api.openweathermap.org/data/3.0/onecall"

account_sid = 'your_twilio_sid'
auth_token = 'your_twilio_token'

# location set to NY City
weather_params = {
    "lat": 40.7128,
    "lon": -74.0060,
    "exclude": "current,minutely,daily",
    "appid": api_id
}

response = requests.get(api_url, params=weather_params)
response.raise_for_status()
weather_data = response.json()

# -------------------- Current Time --------------------
# for ET specify tz with pytz package
now = dt.datetime.now(tz=pytz.timezone('US/Eastern'))
hour_base = now.hour

# -------------------- Temp and Condition --------------------
forecast_notification = ""
for hour in range(0, 12):
    fahrenheit = kelvin_to_fahrenheit(weather_data["hourly"][hour]["temp"])
    condition = weather_data["hourly"][hour]["weather"][0]["description"]
    time = time_convert(hour_base, hour)
    forecast_notification += f"{time}: {fahrenheit}F and {condition}\n"

# -------------------- Send SMS via Twilio --------------------
client = Client(account_sid, auth_token)
message = client.messages \
                .create(
                     body=f"Today's Forecast:\n{forecast_notification}",
                     from_='+19257226334',
                     to='+19253145566'
                 )
print(message.status)
