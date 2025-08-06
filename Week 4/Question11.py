import requests
from bs4 import BeautifulSoup
import string

BASE = "https://sanand0.github.io/tdsdata/crawl_html/"

resp = requests.get(BASE)
resp.raise_for_status()

soup = BeautifulSoup(resp.text, 'html.parser')
links = soup.find_all('a', href=True)

count = 0
files = []

print(soup)

for a in links:
    href = a['href']
    if href.endswith('.html'):
        first = href[0].upper()
        if 'K' <= first <= 'U':
            files.append(href)
            count += 1

print(f"Found {count} HTML files starting with letters K–U:")
for f in files:
    print(f" - {f}")
