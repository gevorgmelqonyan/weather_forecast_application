import requests
import matplotlib.pyplot as plt

def get_api_info(city, key, method, day = None):
    if day:
        url = f"http://api.weatherapi.com/v1/{method}?key={key}&q={city}&days={day}&aqi=no&alerts=no"
    else:
        url = f"http://api.weatherapi.com/v1/{method}?key={key}&q={city}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    elif response.status_code in [400, 401, 403]:

        error_info = response.json().get("error", {})
        error_code = error_info.get("code")
        error_message = error_info.get("message")

        error_messages = {
            1002: "API key not provided. Please configure your API key.",
            1003: "Location parameter ('q') not provided. Please enter a location.",
            1005: "Invalid API request URL. Check your method or endpoint.",
            1006: f"No location found for '{city}'. Please check the spelling.",
            2006: "Invalid API key. Please verify your key.",
            2007: "Monthly request limit exceeded. Upgrade your plan or wait.",
            2008: "API key disabled. Contact support or check your account.",
            2009: "API key does not have access to this resource. Check your subscription plan.",
            9000: "Invalid JSON format in request. Please check the request body.",
            9001: "Too many locations in bulk request. Limit to under 50.",
            9999: "Internal server error. Please try again later.",
        }

        user_message = error_messages.get(error_code, f"Unexpected error: {error_message} (code {error_code})")
        print(f"Error: {user_message}")
        return None


def print_weather_info(data, temp_c = True):
    city_name = data["location"]["name"]
    if temp_c:
        gradus = data["current"]["temp_c"]
        gradus_symbol = "°C"
    else:
        gradus = data["current"]["temp_f"]
        gradus_symbol = "°F"
    condition = data["current"]["condition"]["text"]
    wind_speed_mph = data["current"]["wind_mph"]
    wind_degree = data["current"]["wind_degree"]
    wind_dir = data["current"]["wind_dir"]
    precip_mm = data["current"]["precip_mm"]
    air_pressure = data["current"]["pressure_mb"]
    humidity = data["current"]["humidity"]
    cloud = data["current"]["cloud"]
    vis_km = data["current"]["vis_km"]
    uv = data["current"]["uv"]

    print(f"\nIt is {gradus}{gradus_symbol} in {city_name} and the weather is {condition}.")
    print(f"Wind speed is {wind_speed_mph} km/h.")
    print(f"Wind direction is {wind_degree}°, which corresponds to compass direction '{wind_dir}'.")
    print(f"Precipitation amount is {precip_mm} mm.")
    print(f"Air pressure is {air_pressure} mb.")
    print(f"Humidity is {humidity}%.")
    print(f"Cloud cover is {cloud}%.")
    print(f"Visibility is {vis_km} km.")
    print(f"UV index is {uv} (0–11+ scale).")


def print_weather_forecast_days(data, temp_c = True):
    for i in range(5):
        forecast_day = data["forecast"]["forecastday"][i]["date"]
        if temp_c:
            max_gradus = data["forecast"]["forecastday"][i]['day']["maxtemp_c"]
            min_gradus = data["forecast"]["forecastday"][i]['day']["mintemp_c"]
            avg_gradus = data["forecast"]["forecastday"][i]['day']["avgtemp_c"]
            gradus_symbol = "°C"
        else:
            max_gradus = data["forecast"]["forecastday"][i]['day']["maxtemp_c"]
            min_gradus = data["forecast"]["forecastday"][i]['day']["mintemp_c"]
            avg_gradus = data["forecast"]["forecastday"][i]['day']["avgtemp_c"]
            gradus_symbol = "°F"
        max_wind_speed = data["forecast"]["forecastday"][i]['day']["maxwind_kph"]
        avghumidity = data["forecast"]["forecastday"][i]['day']["avghumidity"]
        daily_will_it_rain = data["forecast"]["forecastday"][i]['day']["daily_will_it_rain"]
        condition = data["forecast"]["forecastday"][i]['day']["condition"]["text"]

        print(f"\nDate: ", forecast_day)
        print(f"Maximum temperature {max_gradus}{gradus_symbol}")
        print(f"Minimum temperature {min_gradus}{gradus_symbol}")
        print(f"Average temperature {avg_gradus}{gradus_symbol}")
        print(f"Maximum wind speed {max_wind_speed}")
        print(f"Average humidity {avghumidity}")
        if daily_will_it_rain:
            daily_chance_of_rain = data["forecast"]["forecastday"][i]['day']["daily_chance_of_rain"]
            print(f"There is a {daily_chance_of_rain} chance of rain")
        else:
            print("There will be no rain")
        print(f"Condition {condition}\n")

def print_weather_forecast_hours(data, temp_c = True):
    city_name = data["location"]["name"]
    print()
    for i in range(0, 24):
        forecast_hour = data["forecast"]["forecastday"][0]["hour"][i]['time']
        if temp_c:
            gradus = data["forecast"]["forecastday"][0]["hour"][i]['temp_c']
            gradus_symbol = "°C"
        else:
            gradus = data["forecast"]["forecastday"][0]["hour"][i]['temp_f']
            gradus_symbol = "°F"
        condition = data["forecast"]["forecastday"][0]["hour"][i]["condition"]["text"]
        wind_speed_mph = data["forecast"]["forecastday"][0]["hour"][i]["wind_mph"]
        air_pressure = data["forecast"]["forecastday"][0]["hour"][i]["pressure_mb"]
        humidity = data["forecast"]["forecastday"][0]["hour"][i]["humidity"]
        cloud = data["forecast"]["forecastday"][0]["hour"][i]["cloud"]
        vis_km = data["forecast"]["forecastday"][0]["hour"][i]["vis_km"]

        print(
            f"At {forecast_hour[-5:]}, the weather in {city_name}: {gradus}{gradus_symbol} with {condition.lower()}, "
            f"wind speed of {wind_speed_mph} mph, air pressure {air_pressure} mb, humidity {humidity}%, "
            f"cloud cover {cloud}%, and visibility up to {vis_km} km."
        )


def show_plot_for_hours(data, temp_c = True):
    city_name = data["location"]["name"]
    tems = [data["forecast"]["forecastday"][0]["hour"][i]['temp_c'] if temp_c else data["forecast"]["forecastday"][0]["hour"][i]['temp_f'] for i in range(24)]
    gradus_symbol = "°C" if temp_c else "°F"
    forecast_hour = [data["forecast"]["forecastday"][0]["hour"][i]['time'][-5:] for i in range(24)]

    plt.plot(forecast_hour, tems, marker="o", linestyle='-', color='skyblue', label=f"Temperature ({temp_c})  in {city_name}")
    plt.xlabel("Hours")
    plt.ylabel(f"Temperature ({gradus_symbol}) in {city_name}")
    plt.grid(True)
    plt.legend()
    plt.show()

def show_plot_for_days(data, temp_c = True):
    city_name = data["location"]["name"]
    tems = [data["forecast"]["forecastday"][i]['day']["avgtemp_c"] if temp_c else data["forecast"]["forecastday"][i]['day']["avgtemp_f"] for i in range(5)]
    gradus_symbol = "°C" if temp_c else "°F"
    forecast_day = [data["forecast"]["forecastday"][i]["date"] for i in range(5)]

    plt.plot(forecast_day, tems, marker="o", linestyle='-', color='skyblue', label=f"Temperature ({gradus_symbol})  in {city_name}")
    plt.xlabel("Days")
    plt.ylabel(f"Temperature ({gradus_symbol})")
    plt.grid(True)
    plt.legend()
    plt.show()
