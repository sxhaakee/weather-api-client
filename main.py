from weather import get_weather

city = input("Enter city: ")

result = get_weather(city)

if isinstance(result, str):
    print(result)
else:
    print(f"Temperature: {result['temp']}°C")
    print(f"Humidity: {result['humidity']}%")
    print(f"Condition: {result['condition']}")
    print(f"Sunrise: {result['sunrise']}")
    print(f"Sunset: {result['sunset']}")
    print(f"Country: {result['country']}")
    print(f"City: {result['city_name']}")
    print(f"Timezone: {result['timezone']}")
