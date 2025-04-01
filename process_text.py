"""
Script: process_text_v2.py
Version: 2.0.1

Description:
This script processes a chapter text file by splitting it into chunks if needed,
extracting structured data via OpenAI's API for each chunk, then aggregating the responses.
The final extracted data is appended to a CSV file and a summary log is updated.
The design follows a chain-of-agents approach to handle long inputs.
"""

import os
import json
import openai
import pandas as pd
import tiktoken  # for token counting

# Constants
CSV_PATH = r"C:\Users\digitalscorpyun\reading-log.csv"
SUMMARY_DIR = r"C:\Users\digitalscorpyun\spencer-tullis\africana-studies\books-reading\summaries"
MODEL_NAME = "gpt-3.5-turbo"  # or use gpt-4 if desired
TOKEN_LIMIT = 4096  # overall API token limit
# Reserve some tokens for prompt structure; set chunk token limit conservatively.
CHUNK_TOKEN_LIMIT = 3500

EXPECTED_FIELDS = [
    "Title", "Author", "Date", "Chapter", "Pages",
    "KeyTakeaway", "ReflectionAction", "Excerpt", "Summary",
    "HistoricalContext", "ContemporaryConnection", "ScholarlySource"
]


def initialize_openai():
    """Initializes the OpenAI API client."""
    openai.api_key = os.getenv("OPENAI_API_KEY")
    print(f"--- DEBUG: API Key retrieved: {openai.api_key} ---")
    if not openai.api_key:
        raise ValueError("OpenAI API key not found in environment variables.")


def read_chapter_text(file_path):
    """Reads the text from the specified file."""
    try:
        clean_path = file_path.strip('\'"')
        with open(clean_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {clean_path}")
    except PermissionError:
        raise PermissionError(f"Permission denied accessing file: {clean_path}")
    except Exception as e:
        raise RuntimeError(f"Error reading file: {e}")


def count_tokens(text):
    """Counts the number of tokens in text using the specified model's tokenizer."""
    try:
        encoding = tiktoken.encoding_for_model(MODEL_NAME)
        return len(encoding.encode(text))
    except Exception as e:
        print(f"Error counting tokens: {e}")
        return 0


def chunk_text(text, chunk_token_limit=CHUNK_TOKEN_LIMIT):
    """
    Splits text into chunks that do not exceed the specified token limit.
    Uses tiktoken for an accurate token count.
    """
    try:
        encoding = tiktoken.encoding_for_model(MODEL_NAME)
        tokens = encoding.encode(text)
        chunks = []
        for i in range(0, len(tokens), chunk_token_limit):
            chunk_tokens = tokens[i: i + chunk_token_limit]
            chunk = encoding.decode(chunk_tokens)
            chunks.append(chunk)
        return chunks
    except Exception as e:
        print(f"Error during chunking: {e}")
        return [text]  # fallback: treat full text as one chunk


def extract_data_from_chunk(text_chunk):
    """
    Extracts structured data from a text chunk via OpenAI's API.
    The prompt instructs the model to return a JSON object with expected fields.
    """
    prompt = f"""
You are an expert research assistant. Extract exactly the following fields based on the provided chapter text.
Return your answer strictly as valid JSON with these keys: {EXPECTED_FIELDS}.
If a field is not explicitly mentioned, use "Not specified in text" as its value.
Follow these word count limits:
- Title: Max 10 words
- Author: Max 5 words
- Chapter: Max 5 words
- KeyTakeaway: Max 20 words
- ReflectionAction: Max 30 words
- Excerpt: Max 50 words
- Summary: Max 50 words
- HistoricalContext, ContemporaryConnection, ScholarlySource: Max 50 words each
Chapter Text:
\"\"\"{text_chunk}\"\"\"
"""
    try:
        response = openai.ChatCompletion.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": "You are a helpful assistant that extracts structured data in JSON format."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2
        )
        content = response.choices[0].message.content.strip()
        data = json.loads(content)
        # Ensure all expected fields exist:
        for field in EXPECTED_FIELDS:
            if field not in data:
                data[field] = "Not specified in text"
        return data
    except Exception as e:
        # Catch any API-related errors generically.
        print(f"Error during API call for extraction: {e}")
        return None


def aggregate_extracted_data(data_list):
    """
    Aggregates a list of partial JSON responses into one final JSON object.
    Prompts the API to merge the responses.
    """
    prompt = f"""
You are an expert research editor. Given the following list of JSON objects that contain extracted information from different chunks of a chapter,
merge them into a single JSON object with the following keys: {EXPECTED_FIELDS}.
For each key, choose the best answer available. If none of the objects provide a clear answer, use "Not specified in text".
Do not add additional keys or commentary.
List of JSON objects:
{json.dumps(data_list, indent=2)}
Respond strictly as a valid JSON object.
"""
    try:
        response = openai.ChatCompletion.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": "You are an expert editor specialized in data aggregation."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2
        )
        aggregated_content = response.choices[0].message.content.strip()
        aggregated_data = json.loads(aggregated_content)
        # Ensure all expected fields exist in the aggregated output:
        for field in EXPECTED_FIELDS:
            if field not in aggregated_data:
                aggregated_data[field] = "Not specified in text"
        return aggregated_data
    except Exception as e:
        print(f"Error aggregating extracted data: {e}")
        return None


def append_to_csv(data, csv_path=CSV_PATH):
    """Appends the extracted data to a CSV file."""
    try:
        df = pd.DataFrame([data])
        os.makedirs(os.path.dirname(csv_path), exist_ok=True)
        if os.path.exists(csv_path):
            df.to_csv(csv_path, mode='a', header=False, index=False, encoding='utf-8')
        else:
            df.to_csv(csv_path, mode='w', header=True, index=False, encoding='utf-8')
        print(f"Data appended to CSV successfully: {csv_path}")
    except Exception as e:
        print(f"Error appending data to CSV: {e}")


def update_summary_log(title, summary, summary_dir=SUMMARY_DIR):
    """Appends the summary to a log file named after the document title."""
    try:
        safe_title = "".join(c for c in title if c.isalnum() or c in (' ', '_')).rstrip()
        if not safe_title:
            safe_title = "Untitled_Document"
        filename = f"{safe_title.replace(' ', '_')}_summary.txt"
        filepath = os.path.join(summary_dir, filename)
        os.makedirs(summary_dir, exist_ok=True)
        with open(filepath, 'a', encoding='utf-8') as file:
            file.write(f"Summary ({pd.Timestamp.now()}):\n{summary}\n\n")
        print(f"Summary updated for '{title}' in '{filepath}'.")
    except Exception as e:
        print(f"Error updating summary log: {e}")


def main():
    """Main orchestrating function."""
    try:
        file_path_input = input("Enter the path to the chapter text file: ").strip()
        initialize_openai()
        chapter_text = read_chapter_text(file_path_input)
        total_token_count = count_tokens(chapter_text)
        print(f"Total tokens in text: {total_token_count}")

        if total_token_count <= CHUNK_TOKEN_LIMIT:
            print("Text is within token limit; processing as a single chunk.")
            extracted_data = extract_data_from_chunk(chapter_text)
        else:
            print("Text exceeds chunk limit; splitting into smaller chunks.")
            chunks = chunk_text(chapter_text, chunk_token_limit=CHUNK_TOKEN_LIMIT)
            partial_results = []
            for idx, chunk in enumerate(chunks, start=1):
                print(f"Extracting data from chunk {idx}/{len(chunks)}...")
                result = extract_data_from_chunk(chunk)
                if result:
                    partial_results.append(result)
            if partial_results:
                print("Aggregating results from all chunks...")
                extracted_data = aggregate_extracted_data(partial_results)
            else:
                print("No data was extracted from any chunk.")
                extracted_data = None

        if extracted_data:
            append_to_csv(extracted_data)
            title_for_log = extracted_data.get("Title", "Untitled")
            summary_for_log = extracted_data.get("Summary", "No summary extracted")
            update_summary_log(title_for_log, summary_for_log)
        else:
            print("No extraction data available to write.")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except PermissionError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Configuration Error: {e}")
    except RuntimeError as e:
        print(f"File Reading Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred in main: {e}")


if __name__ == "__main__":
    main()