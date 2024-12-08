
#! Start display and welcome message
format_output = "\033[32m"
format_reset = "\033[0m"

print(f"\n {format_output}--- Weather App---{format_reset}")

def welcome_message():
    print("Welcome to the weather forecast!")
    print("Get the 'latest' weather updates for a city from the list.")
welcome_message()

#! Available weather data
def weather_forecast():
    weather_data = {
        "London": {"temperature": "15°C", "conditions": "Cloudy", "wind_speed": "5 km/h", "humidity": "80%"},
        "New York": {"temperature": "20°C", "conditions": "Sunny", "wind_speed": "10 km/h", "humidity": "50%"},
        "Tokyo": {"temperature": "18°C", "conditions": "Rainy", "wind_speed": "7 km/h", "humidity": "90%"},
        "Sydney": {"temperature": "22°C", "conditions": "Windy", "wind_speed": "15 km/h", "humidity": "60%"},
        "Paris": {"temperature": "17°C", "conditions": "Foggy", "wind_speed": "3 km/h", "humidity": "85%"},
    }
    
#! user input
    while True:
        print("\nCurrent available information:", ", ".join(weather_data.keys()))
        city = input("\nEnter a city name from the list to see the forecast: ")
#! If the input matches the available information
        if city in weather_data:
            weather_info = fetch_weather_data(city, weather_data)
            display_weather_data(city, weather_info)
            break
#! If the input doesn't match the available information
        else:
            print("That isn't a city from the list. Please read the list. There is no other data currently available.")

#! Thank you message
    print("\nThanks! Check again for another city or come back and check again some time.")
    weather_forecast()

#! Fetch the data
def fetch_weather_data(city, weather_data):
    return weather_data.get(city)

#! Display order of the data
def display_weather_data(city, data):
    print(f"\nThe weather forecast for {city} is:")
    print(f"Temperature: {data['temperature']}")
    print(f"Conditions: {data['conditions']}")
    print(f"Wind Speed: {data['wind_speed']}")
    print(f"Humidity: {data['humidity']}")

#! Run the app
weather_forecast()
