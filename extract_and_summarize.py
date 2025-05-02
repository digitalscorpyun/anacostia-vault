#!/usr/bin/env python
"""
extract_and_summarize.py v1.0.0
Reads data from extract-data.txt, summarizes the content, and logs the results
including summary and contemporary connection to a CSV file.
"""

import os
import sys
import csv
import logging
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv
import ibm_watson
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# ── Configuration ──────────────────────────────────────────────────────────────
__version__ = "1.0.0"
BASE_DIR = Path(__file__).parent  # Directory where the script is located
INPUT_FILE = BASE_DIR / "extract_data.txt"  # Input text file
OUTPUT_CSV = BASE_DIR / "reading_log.csv"  # Output CSV file in the same directory

FIELDNAMES = [
    "timestamp", "version", "source_type", "title",
    "author", "published_date", "date_read",
    "contemporary_connection", "summary"
]

# ── Logging Setup ──────────────────────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format=f"%(asctime)s [v{__version__}] %(levelname)s: %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)
log = logging.getLogger()

# ── IBM Watson NLU Setup ──────────────────────────────────────────────────────
def analyze_with_watson(text):
    """Analyze the text using IBM Watson's NLU API."""

    load_dotenv()
    ibm_api_key = os.getenv("IBM_API_KEY")

    authenticator = IAMAuthenticator(ibm_api_key)
    nlu = ibm_watson.NaturalLanguageUnderstandingV1(
        version='2021-08-01',
        authenticator=authenticator
    )
    nlu.set_service_url('https://api.au-syd.natural-language-understanding.watson.cloud.ibm.com/instances/8b781a43-67c5-4951-9208-d872d64eee70')  # Replace with your actual Service URL

    try:
        response = nlu.analyze(
            text=text,
            features=ibm_watson.features.Features(
                categories=ibm_watson.features.CategoriesOptions(),
                concepts=ibm_watson.features.ConceptsOptions(),
                sentiment=ibm_watson.features.SentimentOptions(),
                emotion=ibm_watson.features.EmotionOptions()
            )
        ).get_result()

        return response
    except Exception as e:
        log.error(f"Error during Watson NLU analysis: {e}")
        return None

# ── CSV Handling ──────────────────────────────────────────────────────────────
def append_to_csv(row):
    """Append data to the reading-log CSV file."""
    if not os.path.exists(BASE_DIR):
        os.makedirs(BASE_DIR)

    try:
        with open(OUTPUT_CSV, "a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=row.keys())
            writer.writerow(row)
        log.info(f"Logged data to {OUTPUT_CSV}")
    except Exception as e:
        log.error(f"Error writing to CSV: {e}")

# ── Main Execution ─────────────────────────────────────────────────────────────
def main():
    log.info(f"Starting extract_and_summarize.py v{__version__}")

    if not os.path.exists(BASE_DIR):
        os.makedirs(BASE_DIR)

    try:
        with open(INPUT_FILE, "r", encoding="utf-8") as f:
            content = f.read()
        log.info(f"Loaded text file: {INPUT_FILE}")
    except FileNotFoundError:
        log.error(f"Text file not found: {INPUT_FILE}")
        return

    summary = summarize_chunkwise(content)
    result = analyze_with_watson(content)
    
    if result:
        sentiment = result['sentiment']['document']['label']
        log.info(f"Sentiment detected: {sentiment}")

        row = {
            "timestamp": datetime.now().isoformat(),
            "version": __version__,
            "source_type": "book",
            "title": "Extracted Title",
            "author": "Extracted Author",
            "published_date": "N/A",
            "date_read": datetime.today().date().isoformat(),
            "contemporary_connection": sentiment,
            "summary": summary
        }

        append_to_csv(row)
        print("\n✅ Done — your reading_log.csv is now up to date.")
    else:
        log.error("No result from Watson NLU analysis.")

# ── Text Summarization ────────────────────────────────────────────────────────
def summarize_chunkwise(text, chunk_size=1000):
    """Break text into chunks and summarize each chunk."""
    chunks = []
    for idx in range(0, len(text), chunk_size):
        chunk = text[idx:idx + chunk_size]
        summary = generate_summary(chunk)
        chunks.append(summary)
        log.info(f"  • chunk {len(chunks)} summarized")
    return " ".join(chunks)

def generate_summary(text):
    """Generate a simple summary for each chunk (placeholder for more complex summarization)."""
    sentences = text.split('.')
    summary = '. '.join(sentences[:3]) if len(sentences) > 3 else text
    return summary

# ── Run the Script ────────────────────────────────────────────────────────────
if __name__ == "__main__":
    main()
