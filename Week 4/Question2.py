import requests
from bs4 import BeautifulSoup
import json

# IMDb search URL for feature films with rating 7.0 to 8.0
url = "https://www.imdb.com/search/title/?user_rating=7,8"

# Set a browser-like User-Agent to avoid being blocked
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

# Send request
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

with open("imdb_debug.html", "w", encoding="utf-8") as f:
    f.write(soup.prettify())

# Store results
results = []

# Each movie is inside a div with class 'lister-item mode-advanced'
movies = soup.find_all('li', class_='ipc-metadata-list-summary-item')[:25]

for movie in movies:
    header = movie.find('h3', class_='ipc-title__text ipc-title__text--reduced')
    title = header.text.strip()

    # Extract IMDb ID from href: /title/tt1234567/

    title_tag = movie.find('a', class_='ipc-title-link-wrapper')
    href = title_tag['href']
    imdb_id = href.split('/')[2]

    # Year (strip extra characters)
    header = movie.find('div', class_="sc-dc48a950-7 hMHetG dli-title-metadata")
    year_text = header.find('span', class_='sc-dc48a950-8 gikOtO dli-title-metadata-item').text
    year = ''.join(filter(str.isdigit, year_text[:6]))  # safe parse first few chars

    # Rating
    rating_tag = movie.find('span', class_="ipc-rating-star--rating")
    rating = rating_tag.text.strip()


    results.append({"id": imdb_id,"title": title,"year": year,"rating": rating})

# Output JSON
print(json.dumps(results, indent=2))