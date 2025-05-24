from functions import *
from time import time
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")

cache= {}
forecast_day_count = 5

commands = {
    "1": ("current", print_weather_info),
    "2": ("forecast", print_weather_forecast_hours),
    "3": ("forecast", print_weather_forecast_days),
    "4": ("forecast", show_plot_for_hours),
    "5": ("forecast", show_plot_for_days),

}

degree_unit = input("Hello, which one would you prefer: Celsius or Fahrenheit?"
                    "\nEnter 'c' for Celsius"
                    "\nEnter 'f' for Fahrenheit.\n"
                    "Please enter your choice: ").lower()

while degree_unit != 'c' and degree_unit != 'f':
    degree_unit = input("Please enter 'c' or 'f': 'c' for Celsius and 'f' for Fahrenheit.").lower()

unit = True if degree_unit == 'c' else False
while True:
    data = None
    command = None
    while command not in ["1", "2", "3", "4", "5", "6"]:
        command = input("\nTo know the current weather, enter 1\n"
                        "To get the hourly forecast for today, enter 2\n"
                        "To get the weather forecast for the upcoming days, enter 3\n"
                        "To plot the temperature graph for one day, enter 4\n"
                        "To plot the temperature graph for the next 5 days, enter 5\n"
                        "To exit, enter 6\n"
                        "Please enter your choice: ")

    if command in commands:
        method, print_weather = commands[command]
    else:
        break

    while not data:
        location_info = input("Now please input your city or zip code: ")
        if (location_info in cache.keys() and cache[location_info][1] == method and
                time() - cache[location_info][0] < 10):
            data = cache[location_info][2]
        else:
            data = get_api_info(location_info, api_key, f"{method}.json", forecast_day_count)


    cache[data["location"]["name"].lower()] = [time(), method, data]
    print_weather(data, degree_unit)

