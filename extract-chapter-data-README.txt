# Reading Log Entry Script (extract_chapter_data.py)

## Version
**2.0.0**

## Description

This Python script enables structured reading log entries through two modes:
1. **Manual Input Mode**: Users are prompted to enter all fields manually.
2. **AI Extraction Mode**: Automatically extracts key data fields from text files using OpenAI's `gpt-3.5-turbo` model.

The script appends structured data to a CSV file (`reading-log.csv`) and updates markdown summary logs for each unique title, integrating seamlessly with Obsidian workflows.

---

## Features

- Dual Mode Support:
  - **Manual Input** for full control.
  - **AI-Powered Data Extraction** for automated workflows.
- **Token Management**: Truncates text exceeding token limits for API processing.
- **File Outputs**:
  - CSV log entries for tabular insights.
  - Markdown summary logs for individual titles.
- **Error Handling**:
  - Ensures robust handling of file operations and API responses.

---

## Requirements

- Python 3.7+ (Python 3.13 recommended)
- Libraries:
  ```bash
  pip install pandas openai tiktoken