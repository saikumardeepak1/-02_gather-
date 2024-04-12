import requests
from datetime import datetime

def get_current_weather(api_key, city, country_code):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&appid={api_key}"
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to retrieve data:", response.text)
        return None
    return response.json()

def check_if_raining(weather_data):
    weather_conditions = [weather['main'] for weather in weather_data['weather']]
    return 'Rain' in weather_conditions

def main():
    API_KEY = 'c98ccadfe1fdf7c7e32fb827271360a1'
    CITY = "Portland"
    COUNTRY_CODE = "US"

    weather_data = get_current_weather(API_KEY, CITY, COUNTRY_CODE)
    if weather_data:
        is_raining = check_if_raining(weather_data)
        print(f"Is it currently raining in {CITY}, {COUNTRY_CODE}? {'Yes' if is_raining else 'No'}")

    next_class_datetime = input("Enter the date and time of your next DE class (format: YYYY-MM-DD HH:MM): ")
    try:
        next_class_time = datetime.strptime(next_class_datetime, '%Y-%m-%d %H:%M')
        print(f"Will it be raining during your next class? {'Yes' if is_raining else 'No'}")
    except ValueError:
        print("Invalid date format. Please use the format 'YYYY-MM-DD HH:MM'.")

    print("Enter the city name and country code to get current weather. Example: London,UK")
    user_city_input = input("City and country code: ")
    try:
        city, country = user_city_input.split(',')
        city_weather_data = get_current_weather(API_KEY, city.strip(), country.strip())
        if city_weather_data:
            print(f"Current weather in {city.strip()} ({country.strip()}): {city_weather_data['weather'][0]['description']}.")
    except ValueError:
        print("Please enter the city and country code separated by a comma.")

if __name__ == "__main__":
    main()
