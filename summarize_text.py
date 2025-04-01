import csv
import re
import textwrap  # For better text formatting in summaries

# Script Version: 1.3 (Corrected file path handling)

def summarize_chapter(text_file, csv_filename="practical_deep_learning_for_cloud_mobile_and_edge_chapter_summaries.csv"):
    """
    Reads a text file, extracts chapter content, and creates summaries,
    logging them into a CSV file.  This version is tailored to the
    structure of the provided 'Practical Deep Learning' text.

    Args:
        text_file (str): The path to the input text file.
        csv_filename (str, optional): The name of the CSV file.
                                     Defaults to 
                                     "practical_deep_learning_for_cloud_mobile_and_edge_chapter_summaries.csv".
    """

    try:
        with open(text_file, 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        print(f"Error: File '{text_file}' not found.")
        return

    #  Corrected chapter extraction: Assumes consistent "Chapter X: Title\n" format
    #  Capturing group () includes the chapter title in the split results.
    chapters = re.split(r'(Chapter \d+: .*?\n)', text, flags=re.IGNORECASE)

    #  Clean up the split results: remove extra whitespace and empty strings.
    chapters = [c.strip() for c in chapters]
    chapters = list(filter(None, chapters))

    #  Pair up chapter titles and content.
    chapter_data = []
    for i in range(0, len(chapters), 2):
        if i + 1 < len(chapters):
            chapter_data.append({'title': chapters[i], 'content': chapters[i + 1]})

    file_exists = False
    try:
        with open(csv_filename, 'r', newline='', encoding='utf-8') as csvfile:
            file_exists = True
    except FileNotFoundError:
        pass  # File doesn't exist yet, that's okay

    with open(csv_filename, 'a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Chapter Title', 'Summary']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()  # Write header only if the file is newly created

        for chapter in chapter_data:
            summary = generate_summary(chapter['content'])
            writer.writerow({'Chapter Title': chapter['title'], 'Summary': summary})

    print(f"\nChapter summaries logged to '{csv_filename}'")


def generate_summary(text):
    """
    Placeholder for summarization logic.  
    Replace with a more advanced method.  This version adds text wrapping.
    """
    sentences = text.split('.')
    summary = '. '.join(sentences[:3]) if len(sentences) > 3 else text

    # Wrap the summary for better readability (adjust width as needed)
    wrapped_summary = textwrap.fill(summary, width=80)
    return wrapped_summary


if __name__ == "__main__":
    #  ***IMPORTANT:*** Use the ABSOLUTE path to your text file!
    text_file = "C:\\Users\\digitalscorpyun\\scripts\\practical_deep_learning_for_cloud_mobile_and_edge.txt"  # Your file name
    summarize_chapter(text_file)