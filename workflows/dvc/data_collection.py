import requests
import pandas as pd
from datetime import datetime

API_KEY = "c621069cebe8707bd65fbc50b9c553b2"
CITY = "Islamabad"
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

def fetch_weather_data():
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        weather_data = []
        for entry in data["list"]:
            weather_data.append({
                "Date": datetime.utcfromtimestamp(entry["dt"]).strftime('%Y-%m-%d'),
                "Time": datetime.utcfromtimestamp(entry["dt"]).strftime('%H:%M:%S'),
                "Temperature": entry["main"]["temp"],
                "Humidity": entry["main"]["humidity"],
                "Wind Speed": entry["wind"]["speed"],
                "Weather Condition": entry["weather"][0]["description"]
            })
        df = pd.DataFrame(weather_data)
        df.to_csv("data/weather_data.csv", index=False)
        print("Weather data saved to weather_data.csv")
    else:
        print("Failed to fetch weather data:", response.status_code, response.reason)

if __name__ == "__main__":
    fetch_weather_data()
