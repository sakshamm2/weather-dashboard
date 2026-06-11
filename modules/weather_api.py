# modules/weather_api.py
import requests

def get_weather(city):
    """
    Fetches both current weather and 5-day forecast data from OpenWeatherMap.
    Uses the explicit project API key.
    """
    api_key = "a812492d5be9b89872a83ca26ddfafce"
    
    # 1. Endpoint URLs for current metrics & 5-day trends
    current_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    forecast_url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
    
    try:
        # Send network requests to OpenWeatherMap
        current_res = requests.get(current_url).json()
        forecast_res = requests.get(forecast_url).json()
        
        # Verify the API responded successfully
        if current_res.get("cod") != 200 or forecast_res.get("cod") != "200":
            return None
            
        forecast_days = []
        forecast_temps = []
        
        # OpenWeather returns data points in 3-hour chunks (8 points per day).
        # We jump by 8 ([::8]) to get one clear daily snapshot for our chart.
        for item in forecast_res["list"][::8]:
            from datetime import datetime
            # Extract timestamp and turn it into a short day name (e.g., 'Mon')
            day_name = datetime.fromtimestamp(item["dt"]).strftime("%a")
            
            forecast_days.append(day_name)
            forecast_temps.append(round(item["main"]["temp"]))
            
        # Bundle current metrics and chart arrays together
        return {
            "current": current_res,
            "forecast_days": forecast_days,
            "forecast_temps": forecast_temps
        }
        
    except Exception:
        return None