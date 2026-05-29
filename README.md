# Weather API Client 🌦️

A Python-based weather application that fetches real-time weather data using the OpenWeatherMap API.

Built to practice:

* API integration
* JSON parsing
* timezone handling
* modular Python architecture
* backend engineering fundamentals

---

## Features

* Real-time weather information
* Temperature & humidity
* Weather conditions
* Sunrise & sunset timing
* Global timezone conversion
* Country name mapping
* Clean modular structure
* Error handling support

---

## Tech Stack

* Python 3
* Requests
* OpenWeatherMap API
* python-dotenv

---

## Project Structure

```bash
weather-api-client/
│
├── main.py
├── weather.py
├── config.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/sxhaakee/weather-api-client.git
```

Move into the project folder:

```bash
cd weather-api-client
```

Create virtual environment:

```bash
python3 -m venv venv
```

Activate virtual environment:

### macOS / Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
API_KEY=your_openweathermap_api_key
```

Get your free API key from OpenWeatherMap.

---

## Run The Project

```bash
python3 main.py
```

---

## Example Output

```bash
Enter city: Tokyo

Temperature: 25.18°C
Humidity: 29%
Condition: broken clouds
Sunrise: 04:28 AM
Sunset: 06:49 PM
Country: Japan
City: Tokyo
Timezone: UTC+9
```

---

## Concepts Practiced

* REST API requests
* JSON parsing
* Dictionaries & nested data
* Functions & modularity
* Timezone conversion
* UNIX timestamp handling
* Environment variables
* Virtual environments
* Git & GitHub workflow

---

## Future Improvements

* GUI interface
* 5-day weather forecast
* Weather icons
* Async API requests
* FastAPI backend
* Docker support
* AI weather summaries

---

## Author

Mohammed Shakeeb

GitHub:
https://github.com/sxhaakee