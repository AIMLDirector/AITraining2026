import datetime
import requests
from zoneinfo import ZoneInfo
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from google.adk.agents import Agent

# Initialize helper objects
geolocator = Nominatim(user_agent="weather_time_agent")
tz_finder = TimezoneFinder()

def get_city_data(city: str):
    """Internal helper to get latitude, longitude, and timezone for a city."""
    location = geolocator.geocode(city)
    if not location:
        return None
    
    # Find timezone ID (e.g., 'America/New_York') from coordinates
    tz_name = tz_finder.timezone_at(lng=location.longitude, lat=location.latitude)
    return {
        "lat": location.latitude,
        "lon": location.longitude,
        "tz_name": tz_name
    }

def get_weather(city: str) -> dict:
    """Retrieves current weather report for any specified city dynamically."""
    data = get_city_data(city)
    if not data:
        return {"status": "error", "error_message": f"Could not find location for '{city}'."}

    # Open-Meteo free API for live weather
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": data["lat"],
        "longitude": data["lon"],
        "current_weather": True
    }
    
    try:
        response = requests.get(url, params=params).json()
        temp_c = response["current_weather"]["temperature"]
        temp_f = (temp_c * 9/5) + 32
        report = f"The weather in {city} is currently {temp_c}°C ({temp_f:.1f}°F)."
        return {"status": "success", "report": report}
    except Exception as e:
        return {"status": "error", "error_message": f"Failed to fetch weather: {str(e)}"}

def get_current_time(city: str) -> dict:
    """Returns the current local time for any specified city dynamically."""
    data = get_city_data(city)
    if not data or not data["tz_name"]:
        return {"status": "error", "error_message": f"Could not find timezone for '{city}'."}

    try:
        tz = ZoneInfo(data["tz_name"])
        now = datetime.datetime.now(tz)
        report = f'The current time in {city} ({data["tz_name"]}) is {now.strftime("%Y-%m-%d %H:%M:%S %Z%z")}'
        return {"status": "success", "report": report}
    except Exception as e:
        return {"status": "error", "error_message": f"Timezone error: {str(e)}"}

# Agent remains the same, but now uses the dynamic tools
root_agent = Agent(
    name="weather_time_agent",
    model="gemini-2.0-flash",
    description="Agent to answer questions about the time and weather in a city.",
    instruction="You are a helpful agent who can answer user questions about the time and weather in a city.",
    tools=[get_weather, get_current_time],
)

