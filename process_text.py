import os
import pandas as pd

# Constants - Using the latest paths provided
CSV_PATH = "C:\\Users\\digitalscorpyun\\reading-log.csv"
SUMMARY_DIR = "C:\\Users\\digitalscorpyun" # Keeping original summary path unless told otherwise

# Define the headers/fields needed for the CSV
CSV_HEADERS = [
    "Title", "Author", "Date", "Chapter", "Pages",
    "KeyTakeaway", "ReflectionAction", "Excerpt", "Summary",
    "HistoricalContext", "ContemporaryConnection", "ScholarlySource"
]

def get_manual_input():
    """Prompts the user to manually enter data for each field."""
    data = {}
    print("Please enter the details for the reading log entry:")
    for header in CSV_HEADERS:
        data[header] = input(f"Enter {header}: ")
    return data

def append_to_csv(data, csv_path=CSV_PATH):
    """Appends the manually entered data to the CSV file."""
    try:
        df = pd.DataFrame([data], columns=CSV_HEADERS) # Ensure correct column order
        # Ensure the directory exists (for the CSV file itself)
        csv_dir = os.path.dirname(csv_path)
        if csv_dir: # Only create if path includes a directory
             os.makedirs(csv_dir, exist_ok=True)

        if os.path.exists(csv_path):
            # Append without header if file exists
            df.to_csv(csv_path, mode='a', header=False, index=False, encoding='utf-8')
        else:
            # Write with header if file is new
            df.to_csv(csv_path, mode='w', header=True, index=False, encoding='utf-8')
        print(f"Data appended to CSV successfully: {csv_path}")
    except Exception as e:
        print(f"Error appending data to CSV: {e}")

def update_summary_log(title, summary, summary_dir=SUMMARY_DIR):
    """Updates the summary log for a given text using manually entered data."""
    try:
        # Basic sanitization for filename
        safe_title = "".join(c for c in title if c.isalnum() or c in (' ', '_')).rstrip()
        if not safe_title: # Handle cases where title is empty or only invalid chars
            safe_title = "Untitled_Document"
        filename = f"{safe_title.replace(' ', '_')}_summary.txt"
        filepath = os.path.join(summary_dir, filename)

        # Ensure the summary directory exists
        os.makedirs(summary_dir, exist_ok=True)

        # Append the new summary to the file
        with open(filepath, 'a', encoding='utf-8') as file:
            # Add a timestamp for clarity when appending multiple summaries
            timestamp = pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')
            file.write(f"Summary ({timestamp}):\n{summary}\n\n")
        print(f"Summary updated for '{title}' in '{filepath}'.")
    except Exception as e:
        print(f"Error updating summary log: {e}")

def main():
    """Main function to orchestrate manual data entry and logging."""
    try:
        # Get manual input from the user
        manual_data = get_manual_input()

        if manual_data:
            # Append data to CSV
            append_to_csv(manual_data)

            # Update summary log using manually entered Title and Summary
            title_for_log = manual_data.get('Title', 'Untitled') # Use 'Untitled' if Title is empty
            summary_for_log = manual_data.get('Summary', 'No summary provided') # Use default if Summary is empty
            update_summary_log(title_for_log, summary_for_log)
        else:
            print("No data entered.")

    except Exception as e:
        print(f"An unexpected error occurred in main: {e}")

# --- Script Execution Starts Here ---
if __name__ == "__main__":
    main()