import requests

# Optional: add your personal access token to avoid rate limits
GITHUB_TOKEN = 'token here'
headers = {
    "Accept": "application/vnd.github+json",
}
if GITHUB_TOKEN:
    headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"

# Step 1: Search GitHub users in Chennai with >170 followers
url = "https://api.github.com/search/users"
params = {"q": "location:Chennai followers:>170", "per_page": 100}

resp = requests.get(url, headers=headers, params=params)
resp.raise_for_status()
items = resp.json().get("items", [])

# Step 2: Fetch each user's details to get created_at
newest_date = None
for user in items:
    u = requests.get(user["url"], headers=headers).json()
    created = u.get("created_at")
    if created and (newest_date is None or created > newest_date):
        newest_date = created

# Step 3: Output newest creation date in ISO 8601 format
if newest_date:
    print(newest_date)
else:
    print("No matching users found.")
