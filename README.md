# weather_forecast_application  
A simple weather forecast application using the WeatherAPI.

This application is developed in Python.

## Requirements

- Python 3.8 or higher  
- Required dependencies are listed in `requirements.txt`

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/gevorgmelqonyan/weather_forecast_application.git
cd weather_forecast_application
pip install -r requirements.txt
python main.py
```

## Notes

- **Security Notice:** The `api_key` is included directly in the `.env` file for the sake of convenience, allowing the app to run immediately after cloning without additional configuration.  
  This approach **contradicts best security practices**, as API keys should not be shared or exposed. In production, consider using environment variables set on the server or a secrets manager.

-  **Graph Display Warning:** When a graph (e.g., hourly or daily temperature chart) is displayed, **program execution is paused** until the graph window is closed. To continue using the application, simply close the graph window.

-  **Terminal Display Tip:** The application prints detailed weather information followed by the command selection menu.  
  If you input a city name or ZIP code and immediately see the command options again, **scroll up in the terminal** to view the fetched weather data. For better experience, it is recommended to **enlarge the terminal window.**

-  **Hourly Graph Display Note:** Since the hourly chart spans 24 data points (for each hour), **x-axis labels might overlap or appear unclear**. To improve readability, consider maximizing the graph window to full screen.
