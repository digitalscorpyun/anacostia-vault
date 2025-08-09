---
id: '20250511112837'
title: Lion Scraper
category: ''
style: ScorpyunStyle
path: ''
created: '2025-05-11'
updated: '2025-05-11'
status: in_progress
priority: normal
summary: ''
longform_summary: ''
tags: []
cssclasses:
- tyrian-purple
- sacred-tech
synapses: []
key_themes: []
bias_analysis: ''
grok_ctx_reflection: ''
quotes: []
adinkra: []
linked_notes: []
---
---
id: "20250520175500"
title: lion_scraper
category: scripts
style: ScorpyunStyle
path: scripts/lion_scraper.md
created: 2025-05-20T17:55:00
updated: 2025-05-20T17:55:00
status: active
priority: high
summary: Annotated scroll for `lion_scraper.py`, the sentinel script powering Africana media curation in the Anacostia Vault.
longform_summary: This scroll documents the logic and sacred function of `lion_scraper.py` — a Sunday-deployed news extraction tool that pulls curated headlines for cultural resistance and Afroalgorithmic archiving. It logs selectors, filters content, and triggers CSV ritual exports.
tags:
  - lion_scraper
  - sunday_scraping
  - afroalgorithmic_resistance
  - dom_traversal
  - sacred_automation
cssclasses:
  - tyrian-purple
  - sacred-tech
linked_notes:
  - 01_africana_frontlines
  - technofeudalism_annotations
  - dom_query_patterns
  - structure-note-sunday-curation
  - lion_scraper_output.csv
  - lion_scraper_log.txt
---

## 🦁 `lion_scraper.py` (v4.3.2 – Bulletproof Edition)

`lion_scraper.py` is the **weekly sentinel** of the Anacostia Vault’s narrative defense grid.  
Built to scrape curated Black, progressive, and AI-focused media sources, it outputs **clean, CSV-formatted headlines**, while logging rejections, anomalies, and selector health for post-scrape audits.

**Version 4.3.2** introduces:

- 🛡️ **Bulletproof config loading** with fail-safe exits
    
- 🔎 **Improved diagnostic logging** for article rejection patterns
    
- 📦 **CSV + TXT + Debug triplet** for ritual record-keeping
    
- 🧪 _DOM selector analysis now pending via companion scroll:_ `[[dom_query_patterns.md]]`
    

---

## 🧪 Schedule Directive: DOM Pattern Companion

> A companion scroll `[[dom_query_patterns.md]]` is now scheduled.  
> It will house walkthroughs for article selectors, DOM traversal theory, and known parser traps across `lion` sources. This supports better filter tuning and resilient scraping.

---

## 🛠️ Core Logic Highlights

- Uses **aiohttp** and **asyncio** for concurrent fetches.
- Loads source selectors from `config_patched.json`.
- Applies **DOM selectors** via `BeautifulSoup` (`soup.select()`).
- Filters noisy or generic content (`"menu"`, `"navigation"`, short titles).
- Outputs:
  - ✅ Valid articles → `output_csv`
  - ⚠️ Rejected (logged with reasons) → `rejected_titles.csv`
  - 🪵 Operational log → `log_txt`

---

## 🔁 Sunday Scraping Flow

1. **Start session** → Async fetch initiated across all source URLs.
2. **DOM Traversal** → Each site uses its configured CSS selector to locate article blocks.
3. **Title Extraction** → Pulls text via `.get_text(strip=True)` and resolves URLs.
4. **Filtering** → Deduplicates and excludes weak entries.
5. **Output** → Writes `output_csv` for vault import and logs all operations.

---

## 🔍 Targeted Variables

- `source["article_selector"]`  
  → CSS selector string passed to `soup.select()`, e.g. `div.headline > a`
  
- `seen = set()`  
  → Ensures deduplication across headlines

- `if href.startswith("http")`  
  → Handles relative URL reconstruction

---

## 🪵 Ritual Logging

Every scrape logs:

- Valid article count per source ✅  
- Failures by source ❌  
- Empty selectors ⚠️  
- Filtered (low quality) entries → rejected_titles.csv

---

## 🧬 Upcoming Enhancements

| Feature                  | Status      |
|--------------------------|-------------|
| `--sunday` mode toggle   | 🟡 Planned   |
| Metadata injection YAML  | 🟢 Active    |
| Selector validation suite| 🟠 In Draft  |
| DOM walkthrough scroll   | ✅ Queued (`dom_query_patterns.md`) |

---

## 🜃 Connected Glyphs

<%*
if (!tp.frontmatter || !Array.isArray(tp.frontmatter.linked_notes)) {
  tR += "⚠️ No linked_notes found in frontmatter.";
} else {
  for (let note of tp.frontmatter.linked_notes) {
    tR += `- [[${note.replace(/\.md$/, "")}]]
`;
  }
}
%>
