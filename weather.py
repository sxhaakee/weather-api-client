import logging
from datetime import datetime, UTC, timedelta
import requests
from config import API_KEY, BASE_URL

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s"
)

country_codes = {
    "IN": "India",
    "GB": "United Kingdom",
    "DE": "Germany",
    "JP": "Japan",
    "US": "United States",
    "FR": "France",
    "AE": "United Arab Emirates"
}

def get_weather(city):

    city = city.strip()

    if not city.replace(" ", "").isalpha():

        logging.error("Invalid city input")

        return {
        "success": False,
        "error": "Please enter a valid city name."
        }

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:

        logging.info(f"Fetching weather data for {city}")

        response = requests.get(
            BASE_URL,
            params=params,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        timezone_offset = data["timezone"]

        timezone_hours = timezone_offset / 3600

        timezone_name = f"UTC{timezone_hours:+.0f}"

        temp = data["main"]["temp"]

        humidity = data["main"]["humidity"]

        condition = data["weather"][0]["description"]

        sunrise = datetime.fromtimestamp(
            data["sys"]["sunrise"],
            UTC
        ) + timedelta(seconds=timezone_offset)

        sunset = datetime.fromtimestamp(
            data["sys"]["sunset"],
            UTC
        ) + timedelta(seconds=timezone_offset)

        sunrise = sunrise.strftime("%I:%M %p")

        sunset = sunset.strftime("%I:%M %p")

        country_code = data["sys"]["country"]

        country = country_codes.get(
            country_code,
            country_code
        )

        city_name = data["name"]

        logging.info(
            f"Weather data fetched successfully for {city_name}"
        )

        return {
            "success": True,
            "temp": temp,
            "humidity": humidity,
            "condition": condition,
            "sunrise": sunrise,
            "sunset": sunset,
            "country": country,
            "city_name": city_name,
            "timezone": timezone_name
        }

    except requests.exceptions.Timeout:

        logging.error("Request timed out")

        return {
            "success": False,
            "error": "Request timed out. Try again later."
        }

    except requests.exceptions.HTTPError:

        logging.error("Invalid city or API issue")

        return {
            "success": False,
            "error": "Invalid city or API error."
        }

    except requests.exceptions.RequestException as e:

        logging.error(f"Network error: {e}")

        return {
            "success": False,
            "error": "Network error occurred."
        }

    except KeyError as e:

        logging.error(f"Missing data in API response: {e}")

        return {
            "success": False,
            "error": "Unexpected API response format."
        }

    except Exception as e:

        logging.error(f"Unexpected error: {e}")

        return {
            "success": False,
            "error": "Something went wrong."
        }
