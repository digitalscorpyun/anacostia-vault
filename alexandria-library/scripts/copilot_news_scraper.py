import aiohttp

import asyncio

import logging

import chardet

from bs4 import BeautifulSoup

from datetime import datetime, timedelta

import csv

from urllib.parse import urljoin

from asyncio import Semaphore

from concurrent.futures import ThreadPoolExecutor

  

# --- Configuration ---

CONCURRENT_REQUESTS = 20  # Increased for faster execution

TIMEOUT = 10  # Lowered to avoid excessive wait times

RETRIES = 3  # Maximum retries before failing

SEMAPHORE = Semaphore(CONCURRENT_REQUESTS)

HEADERS = {"User-Agent": "Mozilla/5.0"}  # Avoid bot detection

FILTER_DAYS = 7  # Ignore articles older than this

executor = ThreadPoolExecutor(max_workers=10)  # Speed up parsing

  

# --- Global Sets for Deduplication ---

SEEN_ARTICLES = set()

DYNAMIC_WEBSITES = [

    "https://www.blackenterprise.com/",

    "https://thegrio.com/",

    "https://theblackwallsttimes.com/",

    "https://atlantablackstar.com/",

    "https://newsone.com/",

    "https://blackgirlnerds.com/",

    "https://www.theroot.com/",

    "https://thehilltoponline.com/",

    "https://www.npr.org/sections/codeswitch/",

    "https://www.ebony.com/",

    "https://afropunk.com/",

]

  

# --- Logging Setup ---

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

  

# --- Helper Functions ---

def get_source_name(url):

    """Extract source name from URL."""

    return url.split("//")[-1].split("/")[0]

  

async def fetch(session, url):

    """Fetch URL contents asynchronously with retry logic."""

    for attempt in range(RETRIES):

        try:

            async with SEMAPHORE:

                async with session.get(url, headers=HEADERS, timeout=TIMEOUT) as response:

                    response.raise_for_status()

                    raw_content = await response.read()

                    encoding = chardet.detect(raw_content)["encoding"] or "utf-8"

                    return raw_content.decode(encoding, errors="ignore")

        except Exception as e:

            logging.warning(f"Retry {attempt + 1}/{RETRIES} failed for {url}: {e}")

            await asyncio.sleep(2 ** attempt)  # Exponential backoff

    logging.error(f"Failed to fetch {url} after {RETRIES} retries")

    return ""

  

async def fetch_article_text(session, article_url):

    """Fetch and process article text with parallel parsing."""

    html = await fetch(session, article_url)

    if not html:

        return ""

  

    loop = asyncio.get_event_loop()

    soup = await loop.run_in_executor(executor, BeautifulSoup, html, "lxml")

  

    paragraphs = soup.find_all("p")

    return " ".join(p.get_text().strip() for p in paragraphs)

  

async def fetch_articles(url, session):

    """Fetch and process articles asynchronously."""

    logging.info(f"Scraping {url}")

    html = await fetch(session, url)

    if not html:

        return []

  

    loop = asyncio.get_event_loop()

    soup = await loop.run_in_executor(executor, BeautifulSoup, html, "lxml")

  

    articles = []

    links = set()

    for selector in ["h1 a", "h2 a", "h3 a", "article a"]:

        for a in soup.select(selector):

            if "href" in a.attrs:

                text = a.get_text(strip=True)

                href = a["href"]

                if text and href:

                    links.add((text, href))

  

    tasks = []

    for title, href in links:

        full_url = href if href.startswith("http") else urljoin(url, href)

  

        identifier = (title, full_url)

        if identifier in SEEN_ARTICLES:

            continue

        SEEN_ARTICLES.add(identifier)

  

        tasks.append(fetch_article_text(session, full_url))

  

    article_texts = await asyncio.gather(*tasks)

  

    # Filter and store articles

    for (title, full_url), text in zip(links, article_texts):

        if not title or not text:

            continue

  

        # Extract date from URL if possible

        pub_date = extract_date_from_url(full_url)

        if pub_date and (datetime.now() - pub_date).days > FILTER_DAYS:

            continue  # Skip old articles

  

        articles.append({

            "title": title,

            "link": full_url,

            "source": get_source_name(url),

        })

        logging.info(f"Added: {title} ({full_url})")

  

    return articles

  

def extract_date_from_url(url):

    """Attempt to extract a date from the article URL."""

    try:

        parts = url.split("/")

        for part in parts:

            if part.isdigit() and len(part) == 4:  # Detect year

                year = int(part)

                month = int(parts[parts.index(part) + 1])

                day = int(parts[parts.index(part) + 2])

                return datetime(year, month, day)

    except (ValueError, IndexError):

        return None  # Return None if extraction fails

  

async def scrape_all():

    """Run all article scrapes asynchronously."""

    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=100)) as session:

        tasks = [fetch_articles(url, session) for url in DYNAMIC_WEBSITES]

        results = await asyncio.gather(*tasks)

  

    return [article for sublist in results for article in sublist]

  

def save_to_csv(articles, filename):

    """Save articles to CSV efficiently."""

    with open(filename, "w", newline="", encoding="utf-8") as csvfile:

        writer = csv.DictWriter(csvfile, fieldnames=["title", "link", "source"])

        writer.writeheader()

        writer.writerows(articles)

  

async def main():

    """Main function to run the scraper asynchronously."""

    logging.info("Starting news scraping operation...")

    articles = await scrape_all()

  

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    output_file = f"articles_{timestamp}.csv"

    save_to_csv(articles, output_file)

  

    logging.info(f"Scraping complete. {len(articles)} articles saved to {output_file}")

  

if __name__ == "__main__":

    asyncio.run(main())

# Testing Checklist for copilot_news_scraper.py

## Environment Setup
- [ ] Commit latest changes and create a backup branch.
- [ ] Activate virtual environment.
- [ ] Install dependencies (`pip install -r requirements.txt`).

## Initial Run
- [ ] Execute: `python copilot_news_scraper.py`
- [ ] Check for errors/warnings in console output.

## Functional Verification
- [ ] Validate data extraction against expected output.
- [ ] Test new enhancements and parsing features.
- [ ] Run tests with controlled input datasets.

## Error Handling
- [ ] Test with invalid URLs/inputs to trigger error handling.
- [ ] Confirm descriptive logging of errors.

## Performance & Stability
- [ ] Run script multiple times for consistency.
- [ ] Monitor execution time and resource usage.
- [ ] Perform load testing if applicable.

## CSV Output & Data Integrity
- [ ] Verify CSV encoding and formatting.
- [ ] Confirm all fields are correctly scraped.

## Documentation & Finalization
- [ ] Update code comments and documentation.
- [ ] Merge branch and tag release in Git.
- [ ] Update Map of Content in Anacostia Vault.

[[to-do-list]] | [[00-index]] | [[ai-ml-overview]] | [[the-lion-of-anacostia-roadmap-anacostia-vault]] | [[africana-studies-overview]]