import requests
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
API_KEY = os.getenv("API_KEY")

# Weather config
CITY = "Davanagere"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Request parameters
params = {
    "q": CITY,
    "appid": API_KEY,
    "units": "metric"
}

# Make the request
response = requests.get(BASE_URL, params=params)

# Parse and plot if response is successful
if response.status_code == 200:
    data = response.json()
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]

    print(f"Temperature in {CITY}: {temp}°C")
    print(f"Humidity in {CITY}: {humidity}%")

    # Graph 1: Temperature
    plt.figure(figsize=(4, 4))
    plt.bar(["Temperature"], [temp], color="tomato")
    plt.title(f"Temperature in {CITY}")
    plt.ylabel("°C")
    plt.ylim(0, 50)
    plt.grid(True)
    plt.show()

    # Graph 2: Humidity
    plt.figure(figsize=(4, 4))
    plt.bar(["Humidity"], [humidity], color="skyblue")
    plt.title(f"Humidity in {CITY}")
    plt.ylabel("%")
    plt.ylim(0, 100)
    plt.grid(True)
    plt.show()

else:
    print("Failed to get data:", response.status_code, response.text)
