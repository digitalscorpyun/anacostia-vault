# Reading Log Entry Script (process_text.py)

## Description

This Python script facilitates the creation of structured reading log entries. It prompts the user to manually enter information for predefined categories related to a text (e.g., book chapter, article) and appends this data as a new row to a central CSV file. It also maintains separate text files containing timestamped summaries for each logged title.

This version uses **manual input** for all data fields and does **not** require an OpenAI API key or perform AI-based extraction.

## Features

*   Prompts the user sequentially for input for each defined field (Title, Author, Summary, etc.).
*   Appends the entered data to a specified CSV file (`reading-log.csv`).
*   Automatically creates the CSV header row if the file doesn't exist.
*   Creates or appends to individual summary log files (`.txt`) for each unique title entered, stored in a separate directory.
*   Includes timestamps in the summary log entries.
*   Basic error handling for file operations.

## Requirements

*   Python 3.7+ (Python 3.13 recommended)
*   Pandas library:
    ```bash
    pip install pandas
    ```

## Setup

1.  **Install Python:** Ensure you have a compatible version of Python installed.
2.  **Install Pandas:** Open your terminal or command prompt and run `pip install pandas`.
3.  **Place Script:** Save the `process_text.py` script in your desired location (e.g., `C:\Users\digitalscorpyun\scripts`).
4.  **Check Paths (Configuration):** Verify the `CSV_PATH` and `SUMMARY_DIR` constants at the top of the script point to your desired locations. Modify them if necessary.

## Usage

1.  **Navigate to Script Directory:** Open your terminal (PowerShell, Command Prompt, etc.) and change to the directory where `process_text.py` is saved.
    ```powershell
    cd C:\Users\digitalscorpyun\scripts
    ```
2.  **Run the Script:** Execute the script using Python.
    ```powershell
    python process_text.py
    ```
3.  **Enter Data:** The script will prompt you to enter information for each field defined in `CSV_HEADERS` (Title, Author, Date, Chapter, Pages, KeyTakeaway, ReflectionAction, Excerpt, Summary, HistoricalContext, ContemporaryConnection, ScholarlySource). Type the relevant information for each prompt and press `Enter`.
4.  **Completion:** Once all fields are entered, the script will attempt to append the data to the CSV and update the summary log, printing confirmation messages or errors to the terminal.

## Configuration

The following constants can be modified directly within the `process_text.py` script:

*   `CSV_PATH`: The full path to the main CSV log file.
    *   Default: `"C:\\Users\\digitalscorpyun\\reading-log.csv"`
*   `SUMMARY_DIR`: The path to the directory where individual summary `.txt` files will be stored.
    *   Default: `"C:\\Users\\digitalscorpyun\\spencer-tullis\\africana-studies\\books-reading\\summaries"`
*   `CSV_HEADERS`: A list defining the column names for the CSV and the fields the user will be prompted for. Modifying this list will change the script's prompts and the CSV structure.

## Output Files

*   **`[CSV_PATH]` (e.g., `reading-log.csv`):** The main comma-separated value file containing all logged entries. Columns correspond to the `CSV_HEADERS` list.
*   **`[SUMMARY_DIR]/[Sanitized_Title]_summary.txt`:** Individual text files, one for each unique title entered. Each file contains timestamped entries for the 'Summary' field provided for that title. Filenames are sanitized versions of the entered 'Title'.