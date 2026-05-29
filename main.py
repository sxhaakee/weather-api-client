from weather import get_weather

city = input("Enter city: ")

result = get_weather(city)

if not result["success"]:

    print(f"Error: {result['error']}")

else:

    print(f"\nWeather Report for {result['city_name']}")
    print("-" * 35)

    print(f"Temperature: {result['temp']}°C")

    print(f"Humidity: {result['humidity']}%")

    print(f"Condition: {result['condition']}")

    print(f"Sunrise: {result['sunrise']}")

    print(f"Sunset: {result['sunset']}")

    print(f"Country: {result['country']}")

    print(f"Timezone: {result['timezone']}")
