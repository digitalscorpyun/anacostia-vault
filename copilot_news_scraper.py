import aiohttp
import asyncio
import csv
import logging
import json
from datetime import datetime
from bs4 import BeautifulSoup
from urllib.parse import urlparse

# Load config.json
with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

WEBSITES = config["WEBSITES"]

# Configure logging
log_filename = f"copilot_scraper_log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
logging.basicConfig(filename=log_filename, level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

async def fetch(url, session):
    """Fetch HTML content from a given URL."""
    try:
        async with session.get(url) as response:
            if response.status == 200:
                logging.info(f"✅ Successfully fetched: {url}")
                return await response.text()
            else:
                logging.warning(f"❌ Failed to fetch {url}: HTTP {response.status}")
                return None
    except Exception as e:
        logging.error(f"❌ Error fetching {url}: {e}")
        return None

async def scrape_news():
    """Scrape news headlines from websites and save to CSV."""
    articles = []
    async with aiohttp.ClientSession() as session:
        for url in WEBSITES:
            html = await fetch(url, session)
            if html:
                soup = BeautifulSoup(html, "html.parser")
                headlines = soup.find_all(["h1", "h2", "h3"])
                for headline in headlines:
                    text = headline.get_text(strip=True)
                    if text:
                        source_name = urlparse(url).netloc.replace("www.", "").split(".")[0].capitalize()
                        hyperlink = f'=HYPERLINK("{url}", "{source_name}")'
                        articles.append((text, hyperlink))  # Headline first, Source second

    # Define CSV filename with timestamp
    csv_filename = f"copilot_scraped_news_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.csv"

    # Save results to CSV
    with open(csv_filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Headline", "Source"])  # Column headers
        writer.writerows(articles)  # Data rows

    logging.info(f"📂 Scraping complete. {len(articles)} articles saved to {csv_filename}")
    print(f"Scraping complete. {len(articles)} articles saved to {csv_filename}")

# Run the scraper
if __name__ == "__main__":
    asyncio.run(scrape_news())
