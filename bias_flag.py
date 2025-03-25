import os
import logging
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from textblob import TextBlob

# Configure logging
log_dir = r'C:\Users\digitalscorpyun\Anacostia\logs'
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    filename=os.path.join(log_dir, 'bias_log.txt'),
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Sentiment and bias detection function
def detect_sentiment(text):
    """Detect emotional bias or sentiment polarity."""
    emo_words = ["hate", "love", "fear", "amazing", "outrage", "crisis", "victory", "shame"]
    emo_flag = [word for word in emo_words if word in text.lower()]

    if emo_flag:
        result = f"Emotional Bias Detected: {', '.join(set(emo_flag))}"
    else:
        polarity = TextBlob(text).sentiment.polarity
        if polarity > 0.2:
            result = "Positive Sentiment"
        elif polarity < -0.2:
            result = "Negative Sentiment"
        else:
            result = "Neutral"
    return result

# Updated and tested selectors
sites = [
    ("https://www.bbc.com/news", {"data-testid": "internal-link"}, "h1"),
    ("https://thefederalist.com/", {"class": "entry-title"}, "h1"),
    ("https://www.aljazeera.com", {"class": "u-clickable-card__link"}, "h1")
]

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

# Scraping loop
for base_url, selector, headline_tag in sites:
    logging.info(f"Scraping {base_url}")
    print(f"Scraping {base_url}")

    try:
        response = requests.get(base_url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Special handling for The Federalist
        if "thefederalist.com" in base_url:
            headline_elements = soup.find_all('h2', class_='entry-title')[:3]
            articles = [h2.find('a') for h2 in headline_elements if h2.find('a')]
        else:
            articles = soup.find_all('a', attrs=selector)[:3]

        print(f"Found {len(articles)} articles from {base_url}.")

        for i, article in enumerate(articles, 1):
            article_href = article.get('href', '')
            article_url = urljoin(base_url, article_href)

            try:
                art_resp = requests.get(article_url, headers=headers, timeout=10)
                art_resp.raise_for_status()
                art_soup = BeautifulSoup(art_resp.text, 'html.parser')
                headline_elem = art_soup.find(headline_tag)
                headline = headline_elem.get_text(strip=True) if headline_elem else "No headline found"

                result = detect_sentiment(headline)
                log_msg = f"Article {i} - URL: {article_url}, Headline: {headline}, Result: {result}"
                logging.info(log_msg)

                print(log_msg)

            except Exception as e:
                error_msg = f"Error scraping article {i} at {article_url}: {e}"
                logging.error(error_msg)
                print(error_msg)

    except Exception as e:
        error_msg = f"Error scraping {base_url}: {e}"
        logging.error(error_msg)
        print(error_msg)
