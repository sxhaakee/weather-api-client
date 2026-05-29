# weather-intelligence-client 🌦️

A robust Python-based weather application that fetches real-time weather information using the OpenWeatherMap API.

This project was built to practice real-world backend engineering concepts such as:

* REST API integration
* JSON parsing
* modular architecture
* virtual environments
* dependency management
* timezone-aware programming
* logging
* exception handling
* Git & GitHub workflow

---

# Project Objective

The goal of this project was not just to display weather data, but to understand how real backend systems are structured and engineered.

The project focuses on:

* clean code organization
* safe API handling
* user input validation
* reliable error handling
* production-style logging
* secure secret management

---

# Features

- ✅ Real-time weather data
- ✅ Temperature in Celsius
- ✅ Humidity tracking
- ✅ Weather condition descriptions
- ✅ Sunrise & sunset timings
- ✅ Global timezone conversion
- ✅ Country code → full country name mapping
- ✅ Input validation
- ✅ Exception handling
- ✅ Logging system
- ✅ Modular project structure
- ✅ Secure API key handling using `.env`

---

# Tech Stack

| Technology         | Purpose                         |
| ------------------ | ------------------------------- |
| Python 3           | Core programming language       |
| Requests           | API communication               |
| OpenWeatherMap API | Weather data provider           |
| python-dotenv      | Environment variable management |
| Git & GitHub       | Version control                 |

---

# Project Structure

```bash
weather-api-client/
│
├── main.py
├── weather.py
├── config.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

---

# Core Engineering Concepts Implemented

## 1. REST API Integration

The application communicates with the OpenWeatherMap API using HTTP GET requests.

Example:

```python
response = requests.get(BASE_URL, params=params, timeout=10)
```

This helped in understanding:

* APIs
* HTTP requests
* query parameters
* JSON responses

---

## 2. JSON Parsing

The API returns nested JSON data which is parsed using Python dictionaries and lists.

Example:

```python
temp = data["main"]["temp"]
condition = data["weather"][0]["description"]
```

Concepts practiced:

* nested dictionaries
* list indexing
* structured data extraction

---

## 3. Modular Architecture

The project is separated into multiple files for cleaner architecture.

### `main.py`

Handles:

* user interaction
* displaying output

### `weather.py`

Handles:

* API communication
* data processing
* timezone conversion
* validation
* exception handling

### `config.py`

Handles:

* configuration
* API keys
* base URLs

This separation improves:

* maintainability
* scalability
* readability

---

# Virtual Environment

A dedicated virtual environment was created for dependency isolation.

## Create virtual environment

```bash
python3 -m venv venv
```

## Activate virtual environment

### macOS / Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

---

# Dependency Management

Dependencies are stored inside:

```bash
requirements.txt
```

Generated using:

```bash
pip freeze > requirements.txt
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Environment Variables & Security

Sensitive information like API keys should never be hardcoded directly inside source code.

This project uses a `.env` file:

```env
API_KEY=your_api_key_here
```

Loaded securely using:

```python
from dotenv import load_dotenv
```

Benefits:

* prevents secret exposure
* safer GitHub uploads
* production-style configuration management

---

# Timezone-Aware Programming

The API returns sunrise and sunset times as UNIX timestamps.

These timestamps are converted into proper local times using:

* UTC conversion
* timezone offsets
* datetime formatting

Example:

```python
datetime.fromtimestamp(..., UTC)
```

This ensures:

* correct international timings
* location-aware results
* timezone-safe processing

---

# Input Validation

The application validates user input before sending requests to the API.

Example:

```python
if not city.replace(" ", "").isalpha():
```

This prevents:

* invalid requests
* garbage input
* unnecessary API calls

---

# Logging System

A logging system was implemented instead of relying on simple print debugging.

Example:

```python
logging.info("Fetching weather data")
logging.error("Invalid city input")
```

Benefits:

* debugging
* monitoring
* execution tracking
* production-style diagnostics

---

# Exception Handling

Robust exception handling was implemented for safer execution.

Handled cases include:

* invalid city names
* API failures
* timeout errors
* network failures
* missing JSON fields
* unexpected runtime errors

Example:

```python
except requests.exceptions.Timeout:
```

This prevents application crashes and improves reliability.

---

# Installation Guide

## Step 1 — Clone Repository

```bash
git clone https://github.com/sxhaakee/weather-api-client.git
```

---

## Step 2 — Move Into Project Folder

```bash
cd weather-api-client
```

---

## Step 3 — Create Virtual Environment

```bash
python3 -m venv venv
```

---

## Step 4 — Activate Virtual Environment

### macOS / Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

---

## Step 5 — Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 6 — Create `.env`

```env
API_KEY=your_openweathermap_api_key
```

---

## Step 7 — Run Application

```bash
python3 main.py
```

---

# Example Output

```bash
Enter city: Tokyo

INFO - Fetching weather data for Tokyo
INFO - Weather data fetched successfully for Tokyo

Weather Report for Tokyo
-----------------------------------
Temperature: 25.18°C
Humidity: 29%
Condition: broken clouds
Sunrise: 04:28 AM
Sunset: 06:49 PM
Country: Japan
Timezone: UTC+9
```

---

# Error Handling Example

```bash
Enter city: 75865

ERROR - Invalid city input

Error: Please enter a valid city name.
```

---

# Git & GitHub Workflow Used

```bash
git init
git add .
git commit -m "Build weather API client"
git push
```

Concepts practiced:

* version control
* commits
* remote repositories
* GitHub workflow

---

# Future Improvements

* 5-day weather forecast
* GUI interface
* Async API requests
* Docker support
* FastAPI backend
* Weather icons
* AI-generated weather summaries
* Unit testing

---

# Learning Outcomes

Through this project, the following concepts were learned and implemented:

* REST APIs
* HTTP requests
* JSON parsing
* modular programming
* virtual environments
* dependency management
* timezone handling
* UNIX timestamps
* logging systems
* exception handling
* Git & GitHub
* secure API management

---

# GitHub Repository

[weather-api-client Repository](https://github.com/sxhaakee/weather-api-client.git)

---

# Author

Mohammed Shakeeb

GitHub:
[sxhaakee GitHub Profile](https://github.com/sxhaakee)
