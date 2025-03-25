### 🏴 **Script - Bias Flag** 🏴

🔥 **Bias Slayer: Python Strikes Propaganda Dead** 🔥

**📜 Category:** Automation / Bias Detection

**Date Created:** 2025-03-14  
**Last Updated:** 2025-03-14

---

## ✊🏿 **Overview: bias_flag.py – The Lion’s Claw**

**script-bias-flag.md** unleashes **bias_flag.py**, a **Python war machine** forged by digitalscorpyun to hunt bias and sentiment in news headlines. It’s the beating heart of [[the-lion-of-anacostia-overview]], scraping BBC, The Federalist, and Al Jazeera with BeautifulSoup, wielding TextBlob to slash emotional propaganda, and logging every strike. This isn’t just code—it’s a **justice weapon**, syncing with [[development-priorities]] and your IBM AI Developer Cert grind.

> _"Bias bends to the flag—truth cuts through the noise." – Vault war cry._

---

## 🔥 **Key Pillars of Strike**

💻 **Scrape Might** → Headlines fall to your pull.  
🧠 **Bias Blade** → Sentiment detection cuts deep.  
📜 **Log Fury** → Every hit tracked, unyielding.  
🌍 **News Targets** → Global bias in your crosshairs.  
🚀 **Vault Power** → Automation fuels the fight.

---

## 🏆 **Script Commanders**

🦁 **Lion’s Will** → Justice drives the code.  
🐍 **Python Core** → Libraries forge the strike.  
👤 **digitalscorpyun** → The warrior behind the flag.

---

## 🌍 **Script Battlefield**

🔹 **🛡 The Code – Bias Flag Unleashed**  
```python
import os
import logging
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from textblob import TextBlob

# Forge the log stronghold
log_dir = r'C:\Users\digitalscorpyun\Anacostia\logs'
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(
    filename=os.path.join(log_dir, 'bias_log.txt'),
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Bias detection strike
def detect_sentiment(text):
    """Slash emotional bias and sentiment polarity."""
    emo_words = ["hate", "love", "fear", "amazing", "outrage", "crisis", "victory", "shame"]
    emo_flag = [word for word in emo_words if word in text.lower()]
    if emo_flag:
        return f"Emotional Bias Detected: {', '.join(set(emo_flag))}"
    polarity = TextBlob(text).sentiment.polarity
    return "Positive Sentiment" if polarity > 0.2 else "Negative Sentiment" if polarity < -0.2 else "Neutral"

# Target sites and selectors
sites = [
    ("https://www.bbc.com/news", {"data-testid": "internal-link"}, "h1"),
    ("https://thefederalist.com/", {"class": "entry-title"}, "h1"),
    ("https://www.aljazeera.com", {"class": "u-clickable-card__link"}, "h1")
]
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

# Strike loop
for base_url, selector, headline_tag in sites:
    logging.info(f"Scraping {base_url}")
    print(f"Scraping {base_url}")
    try:
        response = requests.get(base_url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Federalist flank
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
                logging.error(f"Error scraping article {i} at {article_url}: {e}")
                print(f"Error: {e}")
    except Exception as e:
        logging.error(f"Error scraping {base_url}: {e}")
        print(f"Error: {e}")
```

🔹 **🔥 How It Strikes – The War Plan**  
- **Log Forge**: Dumps every hit to `bias_log.txt`—[[anacostia-vault-execution]].  
- **Bias Slash**: Flags emotional triggers or polarity—hate, love, or neutral.  
- **Scrape Edge**: Hits three news fronts, pulls top 3 headlines—[[scorpyunsummary-weimar-anacostia-parallels]].  
- **Error Shield**: Catches failures, logs them—resilience rules.

---

## 🔗 **Connections in Your Zettelkasten**

📖 **[[00-index]]** → Vault’s war hub.  
🔥 **[[the-lion-of-anacostia-overview]]** → Justice flagship.  
✊🏿 **[[python-overview]]** → Code backbone.  
💻 **[[development-priorities]]** → Priority strike plan.  
🛠 **[[anacostia-vault-execution]]** → Execution core.  
📋 **[[to-do-list]]** → Action forge.

---

🔥 **This isn’t a script—it’s your vault’s bias killer.** 🔥  
🏴 **Every run tears propaganda apart.** 🏴  
🚀 **Deploy it, log it, own the truth.** 🚀

[[00-index]] | [[the-lion-of-anacostia-overview]] | [[python-overview]]

---

### 🏷️ **Tags**

#script_bias_flag #bias_detection #python_automation #lion_of_anacostia #vault_justice

---

### 📖 **Action Commands**

- Test on BBC/Al Jazeera—fix scraping bugs—[[development-priorities]].  
- Push to `virgin-repository`—[[github-virgin-repository]].  
- Link logs to [[show-grok]]—track the war.

---

### Improvements Made
1. **Structure**: Adopted Matamba-style (🏴 Title, 🔥 Subtitle, ✊🏿 Overview) for a fiery, unified strike.
2. **Tone**: Infused ScorpyunStyle™ heat (e.g., “war machine,” “bias slayer”) to match your ethos.
3. **Code**: Kept intact, added inline comments for clarity—battle-ready.
4. **Documentation**: Wrapped script in a vault hub, explaining function and flow.
5. **Connections**: Tied to vault hubs (e.g., "[[the-lion-of-anacostia-overview]]"), rooting it in your ecosystem.
6. **Backlinks**: Hyphenated (e.g., "[[python-overview]]"), no underscores, vault-ready.
7. **Tags**: Underscore_format (e.g., "script_bias_flag"), sharp and consistent.
8. **Filename**: Named "script-bias-flag.md" for kebab-case precision.

---

### Filename
Saved as **"script-bias-flag.md"**, a new vault weapon.

---

This redo makes "script-bias-flag.md" a vault-ready justice strike for your fight. Want more heat (e.g., new features), a debug focus, or extra links? Let me know! 🔥🚀