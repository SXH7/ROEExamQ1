import requests

# Define request to Nominatim
url = "https://nominatim.openstreetmap.org/search"
params = {
    "q": "Foshan",
    "country": "China",
    "format": "json",
    "addressdetails": 1,
    "limit": 10
}
headers = {
    "User-Agent": "TDS-WeatherApp/1.0 (your@email.com)"
}

# Make request
response = requests.get(url, params=params, headers=headers)
response.raise_for_status()  # throws error if not 200 OK

# Parse response
try:
    data = response.json()
except ValueError:
    print("Error: Response could not be parsed as JSON")
    exit()

# Make sure it's a list of dictionaries
if not isinstance(data, list):
    print("Unexpected response format")
    print(data)
    exit()

# Find entry with OSM ID ending in '4719'
found = False
for place in data:
    osm_id = str(place.get("osm_id", ""))
    if osm_id.endswith("4719"):
        bbox = place.get("boundingbox", [])
        if bbox:
            min_lat = float(bbox[0])  # First value is min latitude
            print(f"✅ Minimum latitude of Foshan (OSM ID ending in 4719): {min_lat}")
            found = True
            break

if not found:
    print("❌ No matching place found with OSM ID ending in 4719.")
