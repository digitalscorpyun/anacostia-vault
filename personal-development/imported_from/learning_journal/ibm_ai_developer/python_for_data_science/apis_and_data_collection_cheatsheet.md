---
id: "20250720073000"
title: api_data_collection_cheatsheet.md
category: learning_journal
style: CodeRitual
path: learning_journal/ibm_ai_developer/api_data_collection_cheatsheet.md
created: 2025-07-20T07:30:00-07:00
updated: 2025-07-20T07:30:00-07:00
status: active
priority: medium
summary: |
  Quick-reference guide for API and web scraping tools using Python, Pandas, and BeautifulSoup. Includes syntax patterns for GET, POST, JSON parsing, tag selectors, and HTML traversal methods.
longform_summary: |
  This cheat sheet documents essential techniques for collecting data via web APIs and scraping HTML documents using Python’s requests, json, and BeautifulSoup libraries. Patterns include reading data with GET/POST, working with headers and query parameters, parsing JSON, and navigating the DOM using methods like `find()`, `select()`, `text`, and sibling/parent access. Emphasizes syntax memorization and real-world usage.
tags:
  - ibm_ai
  - api
  - web_scraping
  - pandas
  - beautifulsoup
  - code_ritual
  - learning_journal
cssclasses:
  - bluefire
synapses: []
key_themes:
  - HTML parsing
  - API interaction
  - Python automation
bias_analysis: "None. Technical reference note."
grok_ctx_reflection: "Connects prior JS DOM knowledge to Pythonic scraping patterns."
quotes: []
adinkra: Eban
linked_notes: []
---

# API & Data Collection Cheat Sheet 🧪📡

## 🔧 Library Imports
```python
from bs4 import BeautifulSoup
import requests
````

## 🌐 HTTP Requests

### `GET`

```python
response = requests.get(url)
```

### `POST`

```python
response = requests.post(url, data={"key": "value"})
```

### `PUT`

```python
response = requests.put(url, data={"key": "value"})
```

### `DELETE`

```python
response = requests.delete(url)
```

### Query Parameters

```python
params = {"page": 1, "per_page": 10}
response = requests.get(url, params=params)
```

### Headers

```python
headers = {"Authorization": "Bearer YOUR_TOKEN"}
response = requests.get(url, headers=headers)
```

## 🧠 JSON Handling

```python
data = response.json()
```

## 🧬 HTML Parsing with BeautifulSoup

### Create Soup

```python
soup = BeautifulSoup(html, "html.parser")
```

### Find One Element

```python
element = soup.find("tag", attrs={"class": "classname"})
```

### Find All Elements

```python
elements = soup.find_all("tag", attrs={"id": "value"})
```

### Select via CSS Selector

```python
titles = soup.select("h1")
```

## 🔍 Navigating DOM

### Get Attribute

```python
href = element["href"]
```

### Get Text

```python
text = element.text
```

### Find Children

```python
children = element.findChildren()
```

### Find Parent

```python
parent = element.parent
```

### Next Sibling

```python
sibling = element.find_next_sibling()
```

## 🏷️ Common Tags for `find()` and `find_all()`

- `"a"`: links
    
- `"p"`: paragraphs
    
- `"h1"`–`"h6"`: headings
    
- `"table"`, `"tr"`, `"td"`: tables
    
- `"img"`: images
    
- `"form"`, `"button"`: inputs
    

## 🧾 Status Code

```python
status = response.status_code
```

---

© IBM Corporation. Adapted for Anacostia Vault.

```

Let me know if you want to break this into companion scrolls (e.g., `requests_patterns.md` vs `beautifulsoup_traversal.md`) or sync with any `dom_query_patterns.md` glyph already in play.
```