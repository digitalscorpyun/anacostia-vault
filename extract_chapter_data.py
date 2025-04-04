"""
Script: extract_chapter_data.py
Version: 2.2.0
Description:
This script automates the creation of structured reading log entries.
It supports both manual data entry and AI-based data extraction using
OpenAI's API. Outputs are stored in a central CSV file and individual
markdown summary files for seamless integration with Obsidian workflows.
Dependencies: pandas, tiktoken, openai
"""

import os
import json
import logging
from typing import Dict, Any
import pandas as pd
import tiktoken
import openai

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Constants (using os.path.join for portability)
BASE_DIR = os.path.join("C:", os.sep, "Users", "digitalscorpyun", "books-reading")
CSV_PATH = os.path.join(BASE_DIR, "reading-log.csv")
SUMMARY_DIR = BASE_DIR
TEXT_INPUT_PATH = os.path.join(BASE_DIR, "extract_data.txt")

CSV_HEADERS = [
    "Title", "Author", "Date", "Chapter", "Pages",
    "KeyTakeaway", "ReflectionAction", "Excerpt", "Summary",
    "HistoricalContext", "ContemporaryConnection", "ScholarlySource"
]
MODEL_NAME = "gpt-3.5-turbo"
TOKEN_LIMIT = 4096


def initialize_openai() -> None:
    """Initializes OpenAI API by setting the API key from environment variables."""
    openai.api_key = os.getenv("OPENAI_API_KEY")
    if not openai.api_key:
        raise ValueError("OpenAI API key missing. Set it as an environment variable.")


def get_manual_input() -> Dict[str, Any]:
    """
    Prompts the user to manually input data for each CSV header.
    Returns a dictionary of user-entered data.
    """
    logging.info("Please manually enter the following fields:")
    data = {header: input(f"{header}: ") for header in CSV_HEADERS}
    return data


def count_tokens(text: str) -> int:
    """Counts the number of tokens in the input text using tiktoken."""
    try:
        encoding = tiktoken.encoding_for_model(MODEL_NAME)
        return len(encoding.encode(text))
    except Exception as e:
        logging.error("Error counting tokens: %s", e)
        return 0


def truncate_text(text: str, max_tokens: int = TOKEN_LIMIT) -> str:
    """
    Truncates text exceeding the token limit to ensure we stay under max_tokens.
    """
    try:
        encoding = tiktoken.encoding_for_model(MODEL_NAME)
        tokens = encoding.encode(text)
        if len(tokens) > max_tokens:
            return encoding.decode(tokens[:max_tokens])
        else:
            return text
    except Exception as e:
        logging.error("Error truncating text: %s", e)
        return text


def extract_with_openai(input_text: str) -> str:
    """
    Uses OpenAI's API to extract structured data from the input text.
    Returns the extracted data as a JSON string.
    """
    initialize_openai()
    truncated_text = truncate_text(input_text)
    prompt = f"""
You are a helpful assistant. Extract structured information from the text below.
Respond with a JSON object with the following keys: {', '.join(CSV_HEADERS)}.
Text: {truncated_text}
"""
    try:
        response = openai.ChatCompletion.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": "Extract data in JSON format."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        logging.error("Error during AI extraction: %s", e)
        return ""


def append_to_csv(data: Dict[str, Any]) -> None:
    """
    Appends the provided data as a new row to the CSV file.
    Creates the CSV file if it doesn't exist.
    """
    try:
        df = pd.DataFrame([data], columns=CSV_HEADERS)
        os.makedirs(os.path.dirname(CSV_PATH), exist_ok=True)
        if os.path.exists(CSV_PATH):
            df.to_csv(CSV_PATH, mode='a', header=False, index=False, encoding='utf-8')
        else:
            df.to_csv(CSV_PATH, mode='w', header=True, index=False, encoding='utf-8')
        logging.info("Data successfully added to CSV: %s", CSV_PATH)
    except Exception as e:
        logging.error("Error appending to CSV: %s", e)


def update_summary_log(title: str, summary: str) -> None:
    """
    Updates (or creates) a markdown summary file for the given title.
    Appends a summary entry with a timestamp.
    """
    try:
        safe_title = "".join(c for c in title if c.isalnum() or c in (' ', '_')).rstrip()
        safe_title = safe_title or "Untitled"
        filepath = os.path.join(SUMMARY_DIR, f"{safe_title}_summary.md")
        os.makedirs(SUMMARY_DIR, exist_ok=True)
        timestamp = pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(filepath, 'a', encoding='utf-8') as file:
            file.write(f"### Summary ({timestamp}):\n{summary}\n\n")
        logging.info("Summary updated for '%s' at '%s'", title, filepath)
    except Exception as e:
        logging.error("Error updating summary log: %s", e)


def main() -> None:
    """
    Main function orchestrating manual user input and AI-powered extraction.
    Provides an option for selecting the mode or quitting.
    """
    while True:
        mode = input("Select mode: [1] Manual Input or [2] AI Extraction (or 'q' to quit): ").strip()
        if mode.lower() == 'q':
            break
        elif mode == "1":
            # Manual entry
            data = get_manual_input()
            append_to_csv(data)
            update_summary_log(data.get("Title", "Untitled"), data.get("Summary", "No summary provided"))
            break
        elif mode == "2":
            # AI extraction
            try:
                with open(TEXT_INPUT_PATH, 'r', encoding='utf-8') as f:
                    input_text = f.read()
                extracted_data = extract_with_openai(input_text)
                if extracted_data:
                    try:
                        data = json.loads(extracted_data)
                    except json.JSONDecodeError as e:
                        logging.error("Failed to decode JSON data from OpenAI response: %s", e)
                        break
                    append_to_csv(data)
                    update_summary_log(data.get("Title", "Untitled"), data.get("Summary", "No summary provided"))
                else:
                    logging.error("No data extracted from the OpenAI API response.")
            except Exception as e:
                logging.error("Error processing file: %s", e)
            break
        else:
            logging.warning("Invalid mode selected. Please try again.")


if __name__ == "__main__":
    main()