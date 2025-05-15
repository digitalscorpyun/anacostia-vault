---
id: '20250511112837'
title: Lion Scraper
category: ''
style: ScorpyunStyle
path: ''
created: '2025-05-11'
updated: '2025-05-11'
status: in_progress
priority: normal
summary: ''
longform_summary: ''
tags: []
cssclasses:
- tyrian-purple
- sacred-tech
synapses: []
key_themes: []
bias_analysis: ''
grok_ctx_reflection: ''
quotes: []
adinkra: []
linked_notes: []
---

# lion_scraper.py (v4.3)

  

import aiohttp

import asyncio

import csv

import json

import logging

from bs4 import BeautifulSoup

from pathlib import Path

  

# Load config relative to script

script_dir = Path(__file__).parent

config_path = script_dir / "config_patched.json"

  

with open(config_path, "r", encoding="utf-8") as f:

    config = json.load(f)

  

sources = config["sources"]

output_csv = config["output_csv"]

log_txt = config["log_txt"]

debug_csv = script_dir / "rejected_titles.csv"

  

# Set up logging

logging.basicConfig(

    filename=log_txt,

    level=logging.INFO,

    format="%(asctime)s | %(levelname)s | %(message)s"

)

logger = logging.getLogger()

  
  

# Helper function to scrape each source

async def fetch(session, source):

    try:

        async with session.get(source["url"], timeout=10) as response:

            html = await response.text()

            soup = BeautifulSoup(html, "html.parser")

            articles = soup.select(source["article_selector"])

  

            seen = set()

            results = []

            rejected = []

  

            for a in articles:

                title = a.get_text(strip=True)

                href = a.get("href")

  

                if not href or len(title) < 5 or title.lower() in {"navigation", "menu"} or title in seen:

                    rejected.append({

                        "source": source["name"],

                        "reason": "filtered",

                        "title": title,

                        "url": href

                    })

                    continue

  

                seen.add(title)

  

                full_url = (

                    href

                    if href.startswith("http")

                    else source["url"].rstrip("/") + "/" + href.lstrip("/")

                )

  

                results.append({

                    "source": source["name"],

                    "title": title,

                    "url": f'=HYPERLINK("{full_url}", "Go!")'

                })

  

                if len(results) >= 20:

                    break

  

            if results:

                logger.info(f"✅ {source['name']}: {len(results)} articles scraped")

            else:

                logger.warning(

                    f"⚠️ {source['name']}: No valid articles (check selectors or filters)"

                )

  

            # Write rejected for debugging

            if rejected:

                with open(debug_csv, "a", newline="", encoding="utf-8") as f:

                    writer = csv.DictWriter(f, fieldnames=["source", "reason", "title", "url"])

                    if f.tell() == 0:

                        writer.writeheader()

                    writer.writerows(rejected)

  

            return results

  

    except Exception as e:

        logger.warning(f"❌ {source['name']}: Failed - {e}")

        return []

  
  

# Orchestrator

async def main():

    all_results = []

  

    async with aiohttp.ClientSession() as session:

        tasks = [fetch(session, site) for site in sources]

        results = await asyncio.gather(*tasks)

  

        for r in results:

            all_results.extend(r)

  

    if all_results:

        with open(output_csv, "w", newline="", encoding="utf-8") as f:

            writer = csv.DictWriter(f, fieldnames=["source", "title", "url"])

            writer.writeheader()

            writer.writerows(all_results)

  

    summary = (

        f"✅ Scraping complete. Articles scraped: {len(all_results)}\n"

        f"📄 CSV saved at: {output_csv}\n"

        f"🪵 Log file at: {log_txt}\n"

        f"🔎 Rejected entries in: {debug_csv}"

    )

  

    print(summary)

  

    with open(log_txt, "a", encoding="utf-8") as log_file:

        log_file.write("\n" + summary + "\n")

  
  

if __name__ == "__main__":

    asyncio.run(main())