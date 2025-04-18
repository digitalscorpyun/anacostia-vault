#!/usr/bin/env python
"""
extract_chapter_data.py
Version 1.2.2
- Adds local summarizer fallback via Hugging Face
- Uses OpenAI Python v1.0+ client
- Manual prompt fallback when no AI available
"""

import os
import sys
import logging
import subprocess
from datetime import datetime
from pathlib import Path

# --- AI Libraries ---
from openai import OpenAI
from transformers import pipeline

# Version number
__version__ = "1.2.2"

# Constants
DATA_DIR = Path(r"C:\Users\digitalscorpyun\projects-and-coding\books-reading")
LOG_FILE = Path("script.log")

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler(sys.stdout)
    ]
)

# Initialize local summarizer
try:
    summarizer = pipeline(
        "summarization",
        model="sshleifer/distilbart-cnn-12-6",
        device=-1  # CPU
    )
    logging.info("Local summarizer loaded successfully.")
    print("✅ Local summarizer ready.")
except Exception as e:
    summarizer = None
    logging.warning(f"Local summarizer unavailable: {e}")
    print("⚠️ Local summarizer unavailable; AI mode will fallback to API/manual.")

def check_python_version():
    """Ensure Python version meets requirements."""
    required_version = (3, 9)
    if sys.version_info < required_version:
        logging.error("Python version too old. Update to 3.9+.")
        print(f"Error: Python 3.9+ required. Current version: {sys.version}")
        sys.exit(1)
    logging.info(f"Python version validated: {sys.version}")

def check_git_updates():
    """Check and pull the latest code from GitHub."""
    try:
        subprocess.run(["git", "pull", "origin", "main"], check=True)
        logging.info("Script updated successfully.")
        print("Script updated to the latest version!")
    except subprocess.CalledProcessError as e:
        logging.error(f"Git update failed: {e}")
        print("Update failed. Ensure Git is installed and the repository exists.")

def get_file_path(filename: str) -> Path:
    """Return the absolute path for a file in the data directory."""
    return DATA_DIR / filename

def read_file(filename: str) -> str | None:
    """Read a file safely, handling exceptions."""
    try:
        return get_file_path(filename).read_text(encoding="utf-8")
    except FileNotFoundError:
        logging.error(f"File not found: {filename}")
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        logging.error(f"Read error: {e}")
    return None

def write_to_log(data: str):
    """Write data to reading-log.csv with error handling."""
    try:
        log_path = get_file_path("reading-log.csv")
        log_path.parent.mkdir(parents=True, exist_ok=True)
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(data + "\n")
    except Exception as e:
        logging.error(f"Write error: {e}")

def prompt_engineering_menu() -> str | None:
    """Enhanced prompt selection for AI mode."""
    print("Choose a prompt style:")
    print("[a] Summary | [b] Chain-of-Thought | [c] Few-shot Prompting")
    choice = input("Enter your choice: ").strip().lower()
    if choice not in ("a", "b", "c"):
        logging.warning("Invalid prompt choice.")
        print("Invalid choice. Please select a valid option.")
        return None
    return choice

def analyze_bias(text: str) -> str:
    """Detect racial/gender bias using IBM watsonx.ai (placeholder)."""
    logging.info("Bias analysis is pending IBM integration.")
    return "Bias analysis pending IBM integration."

def handle_ai_mode(content: str):
    """
    Handle AI-based text processing:
     1) Local summarizer
     2) OpenAI API
     3) Manual prompt fallback
    """
    choice = prompt_engineering_menu()
    if not choice:
        return

    # Local summarizer path
    if summarizer:
        summary = summarizer(
            content,
            max_length=130,
            min_length=30,
            do_sample=False
        )[0]["summary_text"]
        write_to_log(f"Local AI Output: {summary}")
        print(f"\nResult (local model):\n{summary}\n")
        return

    # OpenAI API path
    prompts = {
        "a": f"Summarize this text:\n\n{content[:500]}",
        "b": f"Analyze step-by-step: {content[:500]}",
        "c": (
            "Example Task: Identify racial themes in *The Black President*.\n"
            f"Now analyze the following text:\n\n{content[:500]}"
        )
    }
    try:
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompts[choice]}
            ],
            max_tokens=150,
            timeout=30
        )
        ai_output = response.choices[0].message.content.strip()
        write_to_log(f"API AI Output: {ai_output}")
        print(f"\nResult (API model):\n{ai_output}\n")
        return

    except Exception as e:
        logging.error(f"AI error: {e}")

    # Manual fallback
    print("\n⚠️ AI unavailable. Paste this into chat.openai.com:")
    print(prompts[choice])

def handle_bias_detection(content: str):
    """Handle bias detection."""
    result = analyze_bias(content)
    write_to_log(f"Bias Analysis: {result}")
    print("Bias analysis:", result)

def handle_historical_context(content: str):
    """Handle historical context analysis (placeholder)."""
    logging.info("Historical context analysis is pending implementation.")
    print("Historical context analysis pending implementation.")

def main():
    """Main function to execute the script."""
    logging.info(f"Script {__version__} started.")
    check_python_version()
    check_git_updates()

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    logging.info("Data directory validated.")

    modes = {
        "1": "Manual",
        "2": "AI",
        "3": "Update",
        "4": "Bias Detection",
        "5": "Historical Context"
    }
    print(f"Modes: {modes} (or 'q' to quit)")
    mode = input("Enter mode: ").strip().lower()

    if mode == "q":
        sys.exit()
    if mode not in modes:
        logging.warning("Invalid mode selected.")
        print("Invalid mode. Please select a valid option.")
        return

    if mode == "3":
        check_git_updates()
        return

    content = read_file("extract_data.txt")
    if not content:
        return

    if mode == "2":
        handle_ai_mode(content)
    elif mode == "4":
        handle_bias_detection(content)
    elif mode == "5":
        handle_historical_context(content)
    else:
        timestamp = datetime.now().isoformat()
        write_to_log(f"{timestamp}, Mode {mode}, Preview: {content[:50]}...")
        print("Logged successfully.")

if __name__ == "__main__":
    main()
