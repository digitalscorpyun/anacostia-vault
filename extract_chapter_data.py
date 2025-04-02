"""
Script: extract_chapter_data.py
Version: 2.0.0
Description:
This script automates the creation of structured reading log entries. It supports both manual data entry
and AI-based data extraction using OpenAI's API. Outputs are stored in a central CSV file and individual
markdown summary files for seamless integration with Obsidian workflows.
"""

import os
import pandas as pd
import tiktoken
import openai

# Constants
CSV_PATH = "C:\\Users\\digitalscorpyun\\books-reading\\reading-log.csv"
SUMMARY_DIR = "C:\\Users\\digitalscorpyun\\books-reading"
TEXT_INPUT_PATH = "C:\\Users\\digitalscorpyun\\books-reading\\extract_data.txt"
CSV_HEADERS = [
    "Title", "Author", "Date", "Chapter", "Pages",
    "KeyTakeaway", "ReflectionAction", "Excerpt", "Summary",
    "HistoricalContext", "ContemporaryConnection", "ScholarlySource"
]
MODEL_NAME = "gpt-3.5-turbo"
TOKEN_LIMIT = 4096

def initialize_openai():
    """Initializes OpenAI API."""
    openai.api_key = os.getenv("OPENAI_API_KEY")
    if not openai.api_key:
        raise ValueError("OpenAI API key missing. Set it as an environment variable.")

def get_manual_input():
    """Prompts the user to manually input data."""
    print("Please manually enter the following fields:")
    data = {header: input(f"{header}: ") for header in CSV_HEADERS}
    return data

def extract_with_openai(input_text):
    """Extracts data from the text using OpenAI's API."""
    initialize_openai()
    truncated_text = truncate_text(input_text)
    prompt = f"""
    Extract structured information from the following text and respond in JSON format:
    {truncated_text}
    """
    try:
        response = openai.ChatCompletion.create(
            model=MODEL_NAME,
            messages=[{"role": "system", "content": "Extract data in JSON format."},
                      {"role": "user", "content": prompt}],
            temperature=0.2
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error during AI extraction: {e}")
        return None

def count_tokens(text):
    """Counts tokens in the input text."""
    try:
        encoding = tiktoken.encoding_for_model(MODEL_NAME)
        return len(encoding.encode(text))
    except Exception as e:
        print(f"Error counting tokens: {e}")
        return 0

def truncate_text(text, max_tokens=TOKEN_LIMIT):
    """Truncates text exceeding the token limit."""
    encoding = tiktoken.encoding_for_model(MODEL_NAME)
    tokens = encoding.encode(text)
    return encoding.decode(tokens[:max_tokens]) if len(tokens) > max_tokens else text

def append_to_csv(data):
    """Appends data to a CSV file."""
    try:
        df = pd.DataFrame([data], columns=CSV_HEADERS)
        os.makedirs(os.path.dirname(CSV_PATH), exist_ok=True)
        if os.path.exists(CSV_PATH):
            df.to_csv(CSV_PATH, mode='a', header=False, index=False, encoding='utf-8')
        else:
            df.to_csv(CSV_PATH, mode='w', header=True, index=False, encoding='utf-8')
        print(f"Data successfully added to CSV: {CSV_PATH}")
    except Exception as e:
        print(f"Error appending to CSV: {e}")

def update_summary_log(title, summary):
    """Updates a summary markdown file."""
    try:
        safe_title = "".join(c for c in title if c.isalnum() or c in (' ', '_')).rstrip()
        safe_title = safe_title or "Untitled"
        filepath = os.path.join(SUMMARY_DIR, f"{safe_title}_summary.md")
        os.makedirs(SUMMARY_DIR, exist_ok=True)
        timestamp = pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(filepath, 'a', encoding='utf-8') as file:
            file.write(f"### Summary ({timestamp}):\n{summary}\n\n")
        print(f"Summary updated for '{title}' at '{filepath}'")
    except Exception as e:
        print(f"Error updating summary log: {e}")

def main():
    """Main function orchestrating manual input and/or AI-powered extraction."""
    print("Select mode: [1] Manual Input or [2] AI Extraction")
    mode = input("Mode (1/2): ").strip()
    if mode == "1":
        # Manual entry
        data = get_manual_input()
        append_to_csv(data)
        update_summary_log(data.get("Title", "Untitled"), data.get("Summary", "No summary provided"))
    elif mode == "2":
        # AI extraction
        try:
            with open(TEXT_INPUT_PATH, 'r', encoding='utf-8') as f:
                input_text = f.read()
            extracted_data = extract_with_openai(input_text)
            if extracted_data:
                append_to_csv(eval(extracted_data))  # Convert JSON string to dict
                update_summary_log(eval(extracted_data).get("Title", "Untitled"),
                                   eval(extracted_data).get("Summary", "No summary provided"))
        except Exception as e:
            print(f"Error processing file: {e}")
    else:
        print("Invalid mode selected. Exiting.")

if __name__ == "__main__":
    main()