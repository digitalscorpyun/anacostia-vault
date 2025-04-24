#!/usr/bin/env python3

# -*- coding: utf-8 -*-

"""

lion_scraper.py - Version 1.6

  

A dynamic web scraper designed to gather articles from websites relevant to the African diaspora, Black communities, and AI/tech innovations.

This tool is inspired by the principles of Sankofa—learning from the past to build a just future—and aligns with the mission

of digitalscorpyun's Anacostia Vault.

  

Version History:

    1.0 (2025-03-24): Initial release with modularized codebase and improved logging.

    1.1 (2025-04-06): Expanded article selectors and improved error handling without altering date filters.

    1.2 (2025-04-06): Enhanced debugging and logging, ensuring accurate article collection and output validation.

    1.3 (2025-04-06): Updated CSV format with clickable "go" links replacing full URLs.

    1.4 (2025-04-06): Implemented strict date filtering to exclude articles older than 7 days.

    1.5 (2025-04-06): Expanded website list to include AI/tech-related sources.

    1.6 (2025-04-07): Optimized runtime with increased concurrency, reduced timeouts, and limited retries.

  

Author: digitalscorpyun

License: MIT

"""

  

import aiohttp

import asyncio

import logging

import chardet

from bs4 import BeautifulSoup

from datetime import datetime, timedelta

import csv

from urllib.parse import urljoin

import os

  

# --- Configuration ---

VERSION = "1.6"

CONCURRENT_REQUESTS = 50  # Increased concurrency for faster execution

TIMEOUT = 5  # Reduced timeout to skip unresponsive sites quickly

RETRIES = 1  # Limited retries to minimize delays

FILTER_DAYS = 7  # Maximum age of articles in days

OUTPUT_DIRECTORY = r"C:\Users\digitalscorpyun\projects-and-coding\lion-scraper"

SEEN_ARTICLES = set()

  

DYNAMIC_WEBSITES = [

    # Black-centered websites

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

  

    # AI/Tech websites

    "https://openai.com/",

    "https://deepmind.com/",

    "https://www.tensorflow.org/",

    "https://huggingface.co/",

    "https://www.kaggle.com/",

    "https://aitrends.com/",

    "https://news.mit.edu/topic/artificial-intelligence",

    "https://www.analyticsinsight.net/",

    "https://www.wired.com/tag/artificial-intelligence/",

    "https://aimagazine.com/",

]

  

# --- Logging Setup ---

logging.basicConfig(

    level=logging.DEBUG,  # Enable detailed debugging

    format="%(asctime)s - %(levelname)s - %(message)s",

    handlers=[logging.StreamHandler()],

)

logger = logging.getLogger(__name__)

  

# --- Helper Functions ---

async def fetch(session, url):

    """Fetch URL contents asynchronously with retry logic."""

    for attempt in range(RETRIES):

        try:

            async with session.get(url, headers=HEADERS, timeout=TIMEOUT) as response:

                response.raise_for_status()

                raw_content = await response.read()

                encoding = chardet.detect(raw_content)["encoding"] or "utf-8"

                return raw_content.decode(encoding, errors="ignore")

        except Exception as e:

            logger.warning(f"Retry {attempt + 1}/{RETRIES} failed for {url}: {e}")

            await asyncio.sleep(2**attempt)

    logger.error(f"Failed to fetch {url} after {RETRIES} retries")

    return ""

  

async def fetch_article_date(session, article_url):

    """Extract publication date from the article page or URL."""

    try:

        html = await fetch(session, article_url)

        if not html:

            return None

  

        soup = BeautifulSoup(html, "html.parser")

  

        # Define selectors for finding the publication date

        date_selectors = [

            "time[datetime]",

            "meta[name='date']",

            "meta[property='article:published_time']",

            ".date",

            ".published-date",

            "time",

        ]

  

        for selector in date_selectors:

            date_element = soup.select_one(selector)

            if date_element:

                date_str = (

                    date_element.get("datetime")

                    or date_element.get("content")

                    or date_element.get_text(strip=True)

                )

                try:

                    return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S%z").date()

                except ValueError:

                    try:

                        return datetime.strptime(date_str, "%Y-%m-%d").date()

                    except ValueError:

                        continue

  

        return extract_date_from_url(article_url)

  

    except Exception as e:

        logger.warning(f"Failed to extract date from {article_url}: {e}")

        return None

  

def extract_date_from_url(url):

    """Attempt to extract a date from the article URL."""

    try:

        parts = url.split("/")

        for i in range(len(parts)):

            if parts[i].isdigit() and len(parts[i]) == 4:  # Look for a year

                year = int(parts[i])

                month = int(parts[i + 1]) if i + 1 < len(parts) else 1

                day = int(parts[i + 2]) if i + 2 < len(parts) else 1

                return datetime(year, month, day).date()

    except (ValueError, IndexError):

        return None

  

async def fetch_articles(url, session):

    """Fetch and process articles asynchronously with date filtering."""

    logger.info(f"Scraping {url}")

    html = await fetch(session, url)

    if not html:

        return []

  

    soup = BeautifulSoup(html, "html.parser")

  

    articles = []

    links = set()

    for selector in ["h1 a", "h2 a", "h3 a", "article a", ".headline a"]:

        for a in soup.select(selector):

            if "href" in a.attrs:

                text = a.get_text(strip=True)

                href = a["href"]

                if text and href:

                    links.add((text, href))

  

    for title, href in links:

        full_url = href if href.startswith("http") else urljoin(url, href)

        identifier = (title, full_url)

        if identifier in SEEN_ARTICLES:

            continue

        SEEN_ARTICLES.add(identifier)

  

        # Extract publication date and apply filtering

        article_date = await fetch_article_date(session, full_url)

        if article_date and (datetime.today().date() - article_date).days > FILTER_DAYS:

            logger.info(f"Skipping outdated article: {title} ({full_url})")

            continue

  

        # Add clickable "go" link

        hyperlink = f'=HYPERLINK("{full_url}", "go")'

        articles.append({"title": title, "link": hyperlink, "source": url})

        logger.info(f"Added: {title} ({full_url})")

  

    return articles

  

async def scrape_all():

    """Run all article scrapes asynchronously."""

    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=100)) as session:

        tasks = [fetch_articles(url, session) for url in DYNAMIC_WEBSITES]

        results = await asyncio.gather(*tasks)

  

    return [article for sublist in results for article in sublist]

  

def save_to_csv(articles, filename):

    """Save articles to CSV efficiently."""

    os.makedirs(OUTPUT_DIRECTORY, exist_ok=True)

    filepath = os.path.join(OUTPUT_DIRECTORY, filename)

    with open(filepath, "w", newline="", encoding="utf-8") as csvfile:

        writer = csv.DictWriter(csvfile, fieldnames=["title", "link", "source"])

        writer.writeheader()

        writer.writerows(articles)

    logger.info(f"Saved {len(articles)} articles to {filepath}")

  

async def main():

    """Main function to run the scraper asynchronously."""

    logger.info(f"Starting news scraping operation (Version {VERSION})...")

    articles = await scrape_all()

  

    if not articles:

        logger.warning("No articles found.")

        return

  

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    output_file = f"articles_{timestamp}.csv"

    save_to_csv(articles, output_file)

  

    logger.info(f"Scraping complete. {len(articles)} articles saved to {output_file}")

  

if __name__ == "__main__":

    asyncio.run(main())
