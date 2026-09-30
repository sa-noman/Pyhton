import os

def fetch_weather(city, api_key):
    import requests
    response = requests.get(
        "https://api.openweathermap.org/data/2.5/weather",
        params={"q": city, "appid": api_key, "units": "metric"},
        timeout=15,
    )
    response.raise_for_status()
    data = response.json()
    return {
        "city": data["name"],
        "temp_c": data["main"]["temp"],
        "summary": data["weather"][0]["description"],
    }

def format_weather(weather):
    return f"{weather['city']}: {weather['temp_c']}°C, {weather['summary']}"

if __name__ == "__main__":
    city = input("City: ").strip()
    print(format_weather(fetch_weather(city, os.environ["OPENWEATHER_API_KEY"])))
