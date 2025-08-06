import requests
from datetime import date, timedelta
from itertools import cycle

# Step 1: Get locationId for Melbourne from BBC API
search_url = "https://weather-broker-cdn.api.bbci.co.uk/en/observation/locations?search=Melbourne"
headers = {"User-Agent": "Mozilla/5.0"}

search_response = requests.get(search_url, headers=headers)
search_data = search_response.json()

# Find the Melbourne in Australia
melbourne_entry = next(
    (entry for entry in search_data if "Australia" in entry.get("name", "")),
    None
)

if not melbourne_entry:
    print("Melbourne, Australia not found.")
    exit()

location_id = melbourne_entry["id"]

# Step 2: Get 7-day weather forecast
forecast_url = f"https://weather-broker-cdn.api.bbci.co.uk/en/forecast/daily/{location_id}"
forecast_response = requests.get(forecast_url, headers=headers)
forecast_data = forecast_response.json()

# Step 3: Extract date-description pairs
forecast_result = {
    day["localDate"]: day["enhancedWeatherDescription"]
    for day in forecast_data.get("forecasts", [])
    if "localDate" in day and "enhancedWeatherDescription" in day
}

# Step 4: Generate 14 unique dates starting from today
start_date = date.today()
dates_14 = [str(start_date + timedelta(days=i)) for i in range(14)]

# Step 5: Repeat descriptions to fill 14 days
descriptions = cycle(forecast_result.values())
forecast_14 = {day: next(descriptions) for day in dates_14}

# Step 6: Output final JSON
import json
print(json.dumps(forecast_14, indent=2))
