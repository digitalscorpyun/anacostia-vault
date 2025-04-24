bias_flag.py v1.4

Purpose: Detect sentiment, bias patterns, and flag disparities in data for AI fairness analysis.

Version: 1.4 (2025-04-08) - Enhanced modularity, improved logging, and added compatibility checks.

Author: digitalscorpyun (with assistance from Grok)

import os
import logging
import pandas as pd
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re
from typing import List, Dict

try:
    from textblob import TextBlob
except ImportError:
    raise ImportError("TextBlob is not installed. Please install it using 'pip install textblob'.")


# ====================================
# LOGGING CONFIGURATION
# ====================================
log_dir = r'C:\Users\digitalscorpyun\Anacostia\logs'
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    filename=os.path.join(log_dir, 'bias_log.txt'),
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logging.info("bias_flag.py v1.4 initialized.")


# ====================================
# CLASS: BiasFlagger
# ====================================
class BiasFlagger:
    """
    BiasFlagger class is responsible for identifying bias patterns within text data.
    """
    def __init__(self, patterns: List[Dict[str, str]], analysis_mode: str = "standard"):
        self.patterns = patterns
        self.analysis_mode = analysis_mode
        self.results = []

    def flag_bias(self, text: str) -> List[Dict[str, str]]:
        for pattern in self.patterns:
            matches = re.findall(pattern['pattern'], text)
            if matches:
                self.results.append({
                    'pattern_name': pattern['name'],
                    'description': pattern['description'],
                    'matches': matches
                })
        return self.results

    def generate_report(self) -> pd.DataFrame:
        if not self.results:
            return pd.DataFrame(columns=['Pattern Name', 'Description', 'Matches'])
        
        report_data = [
            {
                'Pattern Name': result['pattern_name'],
                'Description': result['description'],
                'Matches': ", ".join(result['matches'])
            } for result in self.results
        ]
        return pd.DataFrame(report_data)


# ====================================
# CLASS: BiasAudit
# ====================================
class BiasAudit:  
    """
    BiasAudit class is responsible for analyzing disparities within datasets based on demographic data.
    """
    def __init__(self, data_path: str, threshold: float = 0.15):  
        try:  
            self.data = pd.read_csv(data_path)  
            self.threshold = threshold  
            self._validate_columns()  
            logging.info("BiasAudit initialized successfully.")  
        except FileNotFoundError:  
            logging.error("Data file not found. Path: %s", data_path)  
            raise  

    def _validate_columns(self):  
        required = {'salary', 'demographic'}  
        if not required.issubset(self.data.columns):  
            missing = required - set(self.data.columns)  
            raise ValueError(f"Missing columns: {missing}")  

    def flag_disparities(self) -> dict:  
        results = {}  
        overall_median = self.data['salary'].median()  

        for group, group_data in self.data.groupby('demographic'):  
            group_median = group_data['salary'].median()  
            disparity = abs(group_median - overall_median) / overall_median  
            results[group] = {  
                'median_salary': group_median,  
                'disparity_ratio': disparity,  
                'exceeds_threshold': disparity > self.threshold  
            }  
        return results  

    def generate_report(self, output_path: str):  
        report = pd.DataFrame(self.flag_disparities()).T  
        report.to_csv(output_path, index_label='demographic_group')  
        logging.info("Report saved to: %s", output_path)  


# ====================================
# FUNCTION: detect_sentiment
# ====================================
def detect_sentiment(text: str) -> str:
    """
    Analyzes text sentiment using TextBlob. Flags emotionally charged words if detected.
    """
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


# ====================================
# FUNCTION: Web Scraping
# ====================================
def scrape_websites(sites: List[tuple]):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    for base_url, selector, headline_tag in sites:
        logging.info(f"Scraping {base_url}")

        try:
            response = requests.get(base_url, headers=headers, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')

            articles = soup.find_all('a', attrs=selector)[:3]

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

                except Exception as e:
                    logging.error(f"Error scraping article {i} at {article_url}: {e}")

        except Exception as e:
            logging.error(f"Error scraping {base_url}: {e}")


# ====================================
# SCRIPT EXECUTION
# ====================================
if __name__ == "__main__":
    sites = [
        ("https://www.bbc.com/news", {"data-testid": "internal-link"}, "h1"),
        ("https://thefederalist.com/", {"class": "entry-title"}, "h1"),
        ("https://www.aljazeera.com", {"class": "u-clickable-card__link"}, "h1")
    ]
    scrape_websites(sites)

