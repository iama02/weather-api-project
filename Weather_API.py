import requests

api_key = "9d48844c36e12f85a547897fd5868802"  # Replace with your real API key
base_url = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter city name: ").strip()
params = {
    "q": city,
    "appid": api_key,
    "units": "metric"
}

response = requests.get(base_url, params=params)

if response.status_code == 200:
    data = response.json()
    print(f"📍 City: {data['name']}")
    print(f"🌡️ Temperature: {data['main']['temp']} °C")
    print(f"☁️ Weather: {data['weather'][0]['description'].title()}")
    print(f"💧 Humidity: {data['main']['humidity']}%")
    print(f"🌬️ Wind Speed: {data['wind']['speed']} m/s")
else:
    print("❌ Failed to get data. Please check your city name or try again.")
    print(f"Status code: {response.status_code}")
    print(f"Response content: {response.text}")
