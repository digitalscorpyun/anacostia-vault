# File: ethnologue_scraper.py
import requests
from bs4 import BeautifulSoup
import csv
import os

# Target URL (example: Hausa language page)
URL = "https://www.ethnologue.com/language/hau"

# Headers to mimic a browser (avoids basic blocks)
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}

# Function to scrape language data
def scrape_ethnologue(url):
    try:
        # GET request
        response = requests.get(url, headers=HEADERS)
        if response.status_code != 200:
            print(f"Failed to fetch page: {response.status_code}")
            return None

        # Parse HTML
        soup = BeautifulSoup(response.content, "html.parser")

        # Extract key data (adjust selectors based on Ethnologue’s structure)
        name = soup.find("h1", class_="page-title")  # Language name
        name = name.text.strip() if name else "N/A"

        # Speaker count (often in a summary section)
        summary = soup.find("div", class_="summary-content")
        speakers = "N/A"
        if summary:
            speakers_text = summary.find("p", string=lambda x: "Population" in (x or ""))
            speakers = speakers_text.text.strip() if speakers_text else "N/A"

        # Region (country/location)
        region = soup.find("div", class_="field-name-field-country")
        region = region.text.strip() if region else "N/A"

        return {"name": name, "speakers": speakers, "region": region}

    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return None

# Save to CSV
def save_to_csv(data, filename="ethnologue_data.csv"):
    file_exists = os.path.isfile(filename)
    with open(filename, "a", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["name", "speakers", "region"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow(data)

# Main execution
if __name__ == "__main__":
    print("Scraping Ethnologue...")
    language_data = scrape_ethnologue(URL)
    
    if language_data:
        print(f"Scraped: {language_data}")
        save_to_csv(language_data)
        print(f"Saved to ethnologue_data.csv")
    else:
        print("Scraping failed.")
## 🛠️ Scraper Pivot
- **Fix**: Switched to Wikipedia due to Ethnologue 403.
- **Data**: [[ethnologue_data.csv]] (Hausa, 50M+ speakers).
- **Tags**: #python #africana #scraping
## 🛠️ Scraper Progress
- **Status**: Fixed Wikipedia selectors for Hausa data using DevTools.
- **Data**: [[ethnologue_data.csv]] (Hausa, 50M+ speakers, Niger-Nigeria region).
- **Tags**: #python #africana #scraping
	