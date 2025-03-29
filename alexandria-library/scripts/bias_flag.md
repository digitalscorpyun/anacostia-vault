import requests
import logging
from bs4 import BeautifulSoup
from textblob import TextBlob
from urllib.parse import urljoin

# Logging configuration (excellent as-is)
logging.basicConfig(
    filename='C:\\Lion\\bias_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

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

# Target sites with selectors
sites = [
    ("https://www.bbc.com/news", {"data-test-id": "internal-link"}, "h1"),
    ("https://www.breitbart.com", {"class": "so-widget-sow-headline"}, "h1"),
    ("https://www.aljazeera.com", {"class": "gc__title"}, "h1")
]

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

for base_url, selector, headline_tag in sites:
    logging.info(f"Scraping {base_url}")
    try:
        response = requests.get(base_url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        articles = soup.find_all('a', selector)[:3]

        for i, article in enumerate(articles, 1):
            article_url = urljoin(base_url, article.get('href', ''))
            try:
                art_resp = requests.get(article_url, headers=headers, timeout=10)
                art_resp.raise_for_status()
                art_soup = BeautifulSoup(art_resp.text, 'html.parser')
                headline_tag_elem = art_soup.find(headline_tag)
                headline = headline_tag_elem.get_text(strip=True) if headline_tag_elem else "No headline found"

                result = detect_sentiment(headline)
                log_msg = f"Article {i} - URL: {article_url}, Headline: {headline}, Result: {result}"
                logging.info(log_msg)

                print(log_msg)  # Quick debugging and confirmation

            except Exception as e:
                logging.error(f"Failed scraping article {i} at {article_url}: {e}")

    except Exception as e:
        logging.error(f"Error scraping {base_url}: {e}")


[[to-do-list]] | [[00-index]] | [[ai-ml-overview]] | [[the-lion-of-anacostia-roadmap-anacostia-vault]] | [[africana-studies-overview]]