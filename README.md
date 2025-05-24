# weather_forecast_application

A simple weather forecast application using the WeatherAPI.

This application is developed in Python.

## Requirements

- Python 3.8 or higher  
- Required dependencies are listed in `requirements.txt`

## How to Run

1. **Open a terminal window** (Command Prompt on Windows, Terminal on macOS/Linux).
2. **Clone the repository**:

```bash
git clone https://github.com/gevorgmelqonyan/weather_forecast_application.git
```

3. **Navigate to the folder** where you cloned the repository:

```bash
cd weather_forecast_application
```

4. **Install the required dependencies:**

```bash
pip install -r requirements.txt
```

5. **Run the program:**

```bash
python main.py
```

*Note: If `python` doesn't work, try using `python3` instead.*

---

## Notes and Considerations

-  **The API key is already included in a `.env` file** in the repository in order to ensure the program works immediately after cloning from GitHub. This is **not secure practice** and only done for convenience during testing or demonstration.

-  **When viewing charts/graphs, the program is temporarily paused**. To continue, **close the chart window**.

-  It is **recommended to maximize your terminal window**, as the application prints a lot of information. After each weather query, the program prints the command selection menu again. If you enter a city or ZIP code and get the menu again without seeing the weather data, **scroll up** to view the previous output.

-  When plotting **hourly weather charts**, since the X-axis includes 24 points, the hour labels may be hard to read. To avoid this, it is **recommended to maximize the chart window to full screen**.
