import requests

def get_weather(city):
    API_KEY = "your_api_key_here"  # Replace this with your real key
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # Celsius
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code == 200:
        print(f"\nWeather in {data['name']}, {data['sys']['country']}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Weather: {data['weather'][0]['description'].title()}")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind Speed: {data['wind']['speed']} m/s")
    else:
        print("\nCity not found or error fetching data.")

# Main
city = input("Enter city name: ")
get_weather(city)