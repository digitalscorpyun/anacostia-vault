# copilot_news_scraper.py v1.1
# This script scrapes news headlines from a list of websites and saves them to a CSV file.

import aiohttp
import asyncio
import csv
import logging
import json
import os
from datetime import datetime
from bs4 import BeautifulSoup
from urllib.parse import urlparse

# Load configuration (websites list and output directory)
with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

WEBSITES = config["WEBSITES"]
OUTPUT_DIR = config.get("OUTPUT_DIR", "C:\\Users\\digitalscorpyun\\copilot_news_scraper_articles")

# Ensure the output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Configure logging to file (saved in the output directory with timestamped filename)
log_filename = os.path.join(OUTPUT_DIR, f"copilot_scraper_log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt")
logging.basicConfig(filename=log_filename, level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

async def fetch(url: str, session: aiohttp.ClientSession) -> str:
    """Fetch HTML content from a given URL with error handling and fallback encodings."""
    try:
        async with session.get(url) as response:
            if response.status == 200:
                logging.info(f"✅ Successfully fetched: {url}")
                try:
                    # Read raw bytes from the response
                    content = await response.read()
                except Exception as e:
                    logging.error(f"❌ Error reading content from {url}: {e}")
                    return None
                # Decode content with fallback logic for encoding issues
                try:
                    html = content.decode('utf-8')
                except UnicodeDecodeError:
                    # If UTF-8 strict decode fails, ignore errors and log a warning
                    try:
                        html = content.decode('utf-8', errors='ignore')
                        logging.warning(f"⚠️ Encoding issue for {url}: some characters were ignored during UTF-8 decode.")
                    except Exception:
                        # Final fallback to Latin-1 if UTF-8 fails
                        try:
                            html = content.decode('latin-1', errors='ignore')
                            logging.warning(f"⚠️ Encoding issue for {url}: decoded with Latin-1 as fallback.")
                        except Exception as e:
                            logging.error(f"❌ Failed to decode content from {url}: {e}")
                            return None
                return html
            else:
                logging.warning(f"❌ Failed to fetch {url}: HTTP {response.status}")
                return None
    except Exception as e:
        logging.error(f"❌ Exception during fetch for {url}: {e}")
        return None

async def scrape_news():
    """Scrape news headlines from the list of websites and save them to a CSV file."""
    articles = []  # List of (headline_text, source_hyperlink)

    async with aiohttp.ClientSession() as session:
        for url in WEBSITES:
            html = await fetch(url, session)
            if not html:
                # If fetch failed or content couldn’t be decoded, skip this site
                logging.warning(f"⚠️ Skipping {url} due to fetch failure or decoding issue.")
                continue

            soup = BeautifulSoup(html, "html.parser")
            headlines = soup.find_all(["h1", "h2", "h3"])
            if not headlines or all(not h.get_text(strip=True) for h in headlines):
                # No headlines found in the HTML (might be a change in site structure or dynamic content)
                logging.warning(f"⚠️ No headlines found for {url} (content might be dynamic or structure changed).")
                continue

            count_for_site = 0
            source_name = urlparse(url).netloc.replace("www.", "").split(".")[0].capitalize()
            for headline in headlines:
                text = headline.get_text(strip=True)
                # Clean up whitespace/newlines in the headline text
                if text:
                    text = text.replace('\r', ' ').replace('\n', ' ').replace('\t', ' ').strip()
                if not text:
                    continue  # skip if it's empty after cleaning

                # Prepare the source hyperlink formula for Excel
                hyperlink = f'=HYPERLINK("{url}", "{source_name}")'
                articles.append((text, hyperlink))
                count_for_site += 1

                # Log the extracted headline for verification
                logging.info(f"Extracted Headline: '{text}' from {url}")

            logging.info(f"Found {count_for_site} headlines on {url}")

    # Define CSV filename with timestamp in the specified output directory
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    csv_path = os.path.join(OUTPUT_DIR, f"copilot_scraped_news_{timestamp}.csv")

    # Write results to CSV file
    try:
        with open(csv_path, mode="w", newline="", encoding="utf-8-sig") as file:
            writer = csv.writer(file)
            writer.writerow(["Headline", "Source"])  # Column headers

            if articles:
                writer.writerows(articles)
            else:
                # If no articles were collected, log a warning (CSV will contain only headers)
                logging.warning("⚠️ No headlines extracted from any site. CSV will only contain the header row.")
                # (We still write the header above, so the file won't be completely empty)

        logging.info(f"📂 Scraping complete. {len(articles)} articles saved to {csv_path}")
        print(f"Scraping complete. {len(articles)} articles saved to {csv_path}")
    except Exception as e:
        logging.error(f"❌ Error writing CSV file {csv_path}: {e}")
        print(f"Error writing CSV: {e}")

# Run the scraper asynchronously
if __name__ == "__main__":
    asyncio.run(scrape_news())
