import requests
from config import API_KEY, BASE_URL
from datetime import datetime, UTC, timedelta

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()
    timezone_offset = data["timezone"]
    timezone_hours = timezone_offset / 3600

    timezone_name = f"UTC{timezone_hours:+.0f}"
    print(data)

    if response.status_code != 200:
        return f"Error: {data['message']}"

    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    condition = data["weather"][0]["description"]
    sunrise = datetime.fromtimestamp(
        data["sys"]["sunrise"],
        UTC
    )+timedelta(seconds=timezone_offset)

    sunrise = sunrise.strftime("%I:%M %p")
    sunset = datetime.fromtimestamp(
    data["sys"]["sunset"],
    UTC
    ) + timedelta(seconds=timezone_offset)

    sunset = sunset.strftime("%I:%M %p") 
    country = data["sys"]["country"]
    city_name = data["name"]

    return {
        "temp": temp,
        "humidity": humidity,
        "condition": condition,
        "sunrise": sunrise,
        "sunset": sunset,
        "country": country,
        "city_name": city_name,
        "timezone": timezone_name,
    }