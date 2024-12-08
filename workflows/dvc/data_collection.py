# import requests
# import pandas as pd
# from datetime import datetime

# API_KEY = "c621069cebe8707bd65fbc50b9c553b2"
# CITY = "Islamabad"
# URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

# def fetch_weather_data():
#     response = requests.get(URL)
#     if response.status_code == 200:
#         data = response.json()
#         weather_data = []
#         for entry in data["list"]:
#             weather_data.append({
#                 "Date": datetime.utcfromtimestamp(entry["dt"]).strftime('%Y-%m-%d'),
#                 "Time": datetime.utcfromtimestamp(entry["dt"]).strftime('%H:%M:%S'),
#                 "Temperature": entry["main"]["temp"],
#                 "Humidity": entry["main"]["humidity"],
#                 "Wind Speed": entry["wind"]["speed"],
#                 "Weather Condition": entry["weather"][0]["description"]
#             })
#         df = pd.DataFrame(weather_data)
#         df.to_csv("data/weather_data.csv", index=False)
#         print("Weather data saved to weather_data.csv")
#     else:
#         print("Failed to fetch weather data:", response.status_code, response.reason)

# if __name__ == "__main__":
#     fetch_weather_data()
import requests
import pandas as pd
from datetime import datetime
import time

API_KEY = "c621069cebe8707bd65fbc50b9c553b2"
cities = [
    "New%20York", "London", "Paris", "Tokyo", "Berlin", "Sydney", "Los%20Angeles", "Moscow", "Madrid", "Rome",
    "Rio", "Mumbai", "Mexico%20City", "Beijing", "Cape%20Town", "Seoul", "Toronto", "Singapore", "Dubai", "Oslo",
    "Cairo", "Lagos", "Amsterdam", "Bangkok", "Istanbul", "Hong%20Kong", "San%20Francisco", "Kuala%20Lumpur", "Chicago",
    "Lisbon", "Athens", "Sao%20Paulo", "Jakarta", "Delhi", "Zurich", "Lima", "Santiago", "Tehran", "Melbourne",
    "Barcelona", "Copenhagen", "Vienna", "Stockholm", "Helsinki", "Warsaw", "Dubai", "Abuja", "Munich", "Jakarta",
    "Lagos", "Bali", "Brussels", "Lyon", "Islamabad"
]

# Initialize an empty list to store all the weather data
weather_data = []

def fetch_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        for entry in data["list"]:
            weather_data.append({
                "Date": datetime.utcfromtimestamp(entry["dt"]).strftime('%Y-%m-%d'),
                "Time": datetime.utcfromtimestamp(entry["dt"]).strftime('%H:%M:%S'),
                "Temperature": entry["main"]["temp"],
                "Humidity": entry["main"]["humidity"],
                "Wind Speed": entry["wind"]["speed"],
                "Weather Condition": entry["weather"][0]["description"],
                "City": city.replace("%20", " ")  # Replacing '%20' with space
            })
        print(f"Weather data for {city.replace('%20', ' ')} fetched successfully. ")
    else:
        print(f"Failed to fetch weather data for {city.replace('%20', ' ')}:", response.status_code, response.reason)

def save_to_csv():
    # Convert weather data into a DataFrame
    df = pd.DataFrame(weather_data)
    df.to_csv("data/weather_data.csv", index=False)
    print("Weather data saved to weather_data.csv\nTotal Rows:", len(weather_data))

if __name__ == "__main__":
    for city in cities:
        fetch_weather_data(city)
        time.sleep(10)  # Sleep for 10 seconds between requests
    
    save_to_csv()
