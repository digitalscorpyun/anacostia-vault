#!/usr/bin/env python3

# -*- coding: utf-8 -*-

# ==============================================================================

# 🦁 lion_scraper.py (v5.3.0 – UTC-safe + Reach & Recentness)

# - Proper robots.txt parsing (no false blocks)

# - Real User-Agent + Accept-Language

# - Retries/backoff for 403/429/timeouts

# - Selector fallbacks when primary yields 0

# - Date extractor: ancestor/sibling scan + relative times (“4 days ago”)

# - Timezone-safe comparisons (UTC everywhere)

# ==============================================================================

  

import asyncio

import csv

import json

import logging

import re

import sys

import time

from datetime import datetime, timedelta, timezone

from pathlib import Path

from urllib.parse import urljoin, urlparse

  

from bs4 import BeautifulSoup

from dateutil import parser

from aiohttp_client_cache.session import CachedSession

from aiohttp_client_cache.backends.sqlite import SQLiteBackend

  

# ==============================================================================

# CONFIG

# ==============================================================================

USER_AGENT = (

    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "

    "AppleWebKit/537.36 (KHTML, like Gecko) "

    "Chrome/124.0 Safari/537.36 LionScraper/5.3.0"

)

HEADERS = {

    "User-Agent": USER_AGENT,

    "Accept-Language": "en-US,en;q=0.9",

    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",

}

  

MAX_RETRIES = 2

REQUEST_TIMEOUT = 15

CUTOFF_DAYS = 7

  

# ==============================================================================

# TIME HELPERS (UTC-normalization)

# ==============================================================================

def _to_utc(dt: datetime) -> datetime:

    """Return a timezone-aware UTC datetime."""

    if dt is None:

        return None

    return dt.replace(tzinfo=timezone.utc) if dt.tzinfo is None else dt.astimezone(timezone.utc)

  

def _now_utc() -> datetime:

    return datetime.now(timezone.utc)

  

# ==============================================================================

# CONFIGURATION HANDLER

# ==============================================================================

class ScraperConfig:

    def __init__(self):

        self.script_dir = Path(__file__).parent.resolve()

        self._load_paths()

        self._validate_config()

  

    def _load_paths(self):

        self.config_path = self.script_dir / "config.json"

        self.output_csv = self.script_dir / "lion_scraper_output.csv"

        self.log_txt = self.script_dir / "lion_scraper_log.txt"

        self.debug_csv = self.script_dir / "rejected_titles.csv"

        self.cache_db = self.script_dir / "lion_cache.sqlite"

  

    def _validate_config(self):

        if not self.config_path.exists():

            raise FileNotFoundError(f"❌ Config not found: {self.config_path}")

        with self.config_path.open("r", encoding="utf-8") as f:

            self.config = json.load(f)

        self.sources = self.config.get("sources", [])

        if not self.sources:

            raise ValueError("❌ No sources configured")

  

# ==============================================================================

# VALIDATION ENGINE

# ==============================================================================

class ArticleValidator:

    @staticmethod

    def is_valid_article(title: str, href: str, seen: set) -> bool:

        title = (title or "").strip()

        return all([

            href,

            len(title) >= 5,

            title.lower() not in {"menu", "navigation", "read more", "sign up"},

            title not in seen,

            not re.match(r"^[\W\d_]+$", title),

        ])

  

# ==============================================================================

# DATE PROCESSING

# ==============================================================================

class DateExtractor:

    MONTHS_PATTERN = r"(JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC)[A-Z]*"

    DATE_PATTERNS = [

        rf"\b{MONTHS_PATTERN}\s*\d{{1,2}},?\s*\d{{2,4}}\b",

        rf"\b\d{{1,2}}\s*{MONTHS_PATTERN},?\s*\d{{2,4}}\b",

        r"\b\d{4}-\d{1,2}-\d{1,2}\b",

        r"\b\d{1,2}/\d{1,2}/\d{2,4}\b",

        r"\b\d{1,2}\.\d{1,2}\.\d{2,4}\b",

    ]

    RELATIVE_RE = re.compile(r"\b(\d+)\s+(minute|hour|day|week|month|year)s?\s+ago\b", re.I)

  

    @classmethod

    def extract_date(cls, element):

        # element + up to 3 ancestors

        node = element

        for _ in range(4):

            if not node:

                break

            dt = cls._check_structured(node) or cls._check_text(node)

            if dt:

                return _to_utc(dt)

            node = getattr(node, "parent", None)

  

        # siblings of original

        if element and element.parent:

            for s in element.parent.find_all(recursive=False):

                if s is element:

                    continue

                dt = cls._check_structured(s) or cls._check_text(s)

                if dt:

                    return _to_utc(dt)

        return None

  

    @classmethod

    def _relative_to_datetime(cls, text: str):

        m = cls.RELATIVE_RE.search(text or "")

        if not m:

            return None

        n, unit = int(m.group(1)), m.group(2).lower()

        minutes = {

            "minute": 1, "hour": 60, "day": 24 * 60, "week": 7 * 24 * 60,

            "month": 30 * 24 * 60, "year": 365 * 24 * 60,

        }[unit]

        return _now_utc() - timedelta(minutes=n * minutes)

  

    @classmethod

    def _check_structured(cls, element):

        # <time> and timestamp-ish elements

        for time_tag in element.select("time, [data-testid*='timestamp'], [class*='timestamp']"):

            for attr in ("datetime", "data-datetime", "data-seconds", "data-time"):

                val = time_tag.get(attr)

                if val:

                    try:

                        if attr == "data-seconds" and str(val).isdigit():

                            return datetime.fromtimestamp(int(val), tz=timezone.utc)

                        return parser.parse(str(val), fuzzy=True)

                    except Exception:

                        pass

            # visible text inside time tag

            try:

                txt = time_tag.get_text(strip=True)

                if txt:

                    rel = cls._relative_to_datetime(txt)

                    if rel:

                        return rel

                    return parser.parse(txt, fuzzy=True)

            except Exception:

                pass

  

        # document-level meta

        soup = element.find_parent("html")

        if soup:

            for meta in soup.select(

                'meta[property="article:published_time"],'

                'meta[property="article:modified_time"],'

                'meta[name="OriginalPublicationDate"],'

                'meta[name*="pubdate"], meta[property*="pubdate"],'

                'meta[name*="date"], meta[property*="date"]'

            ):

                content = meta.get("content")

                if content:

                    try:

                        return parser.parse(str(content), fuzzy=True)

                    except Exception:

                        continue

  

        # common date classes

        for date_elem in element.select('*[class*="date"], *[class*="time"], *[class*="posted"]'):

            txt = date_elem.get_text(" ", strip=True)

            if not txt:

                continue

            rel = cls._relative_to_datetime(txt)

            if rel:

                return rel

            try:

                return parser.parse(txt, fuzzy=True)

            except Exception:

                continue

        return None

  

    @classmethod

    def _check_text(cls, element):

        text = element.get_text(" ", strip=True)

  

        # relative first

        rel = cls._relative_to_datetime(text)

        if rel:

            return rel

  

        # absolute formats

        for pattern in cls.DATE_PATTERNS:

            m = re.search(pattern, text, re.IGNORECASE)

            if not m:

                continue

            try:

                dt = parser.parse(m.group(), fuzzy=True)

                if dt.year in (datetime.utcnow().year, datetime.utcnow().year - 1):

                    return dt

            except Exception:

                continue

  

        low = text.lower()

        if "today" in low or "just now" in low:

            return _now_utc()

        if "yesterday" in low:

            return _now_utc() - timedelta(days=1)

        return None

  

# ==============================================================================

# SCRAPER ENGINE

# ==============================================================================

class ScraperEngine:

    def __init__(self, config):

        self.config = config

        self._setup_logging()

  

    def _setup_logging(self):

        logging.basicConfig(

            filename=self.config.log_txt,

            level=logging.INFO,

            format="%(asctime)s | %(levelname)s | %(message)s",

            force=True,

        )

        self.logger = logging.getLogger()

  

    async def run(self):

        start_time = time.time()

        results = await self._scrape_all_sources()

        self._save_results(results)

        self._log_summary(results, start_time)

  

    async def _scrape_all_sources(self):

        async with CachedSession(

            cache=SQLiteBackend(str(self.config.cache_db)),

            headers=HEADERS,

        ) as session:

            tasks = [self._scrape_source(session, src) for src in self.config.sources]

            return await asyncio.gather(*tasks)

  

    # ----------- HTTP helpers -------------------------------------------------

    async def _fetch_text(self, session, url, timeout=REQUEST_TIMEOUT):

        last_exc = None

        for attempt in range(MAX_RETRIES + 1):

            try:

                async with session.get(url, timeout=timeout) as resp:

                    if resp.status in (403, 429) and attempt < MAX_RETRIES:

                        await asyncio.sleep(1.0 + attempt)

                        continue

                    resp.raise_for_status()

                    return await resp.text()

            except Exception as e:

                last_exc = e

                if attempt < MAX_RETRIES:

                    await asyncio.sleep(0.6 * (attempt + 1))

                else:

                    self.logger.error(f"❌ fetch failed [{url}]: {e}")

        raise last_exc

  

    async def _robots_allows(self, session, base_url: str) -> bool:

        """

        Parse robots.txt; allow if:

          - no robots.txt, or cannot parse, or

          - '*' does NOT explicitly disallow '/'.

        """

        try:

            parsed = urlparse(base_url)

            robots_url = f"{parsed.scheme}://{parsed.netloc}/robots.txt"

            text = await self._fetch_text(session, robots_url, timeout=6)

            rules = []

            agent = None

            for line in text.splitlines():

                line = line.strip()

                if not line or line.startswith("#"):

                    continue

                if line.lower().startswith("user-agent:"):

                    agent = line.split(":", 1)[1].strip()

                elif line.lower().startswith("disallow:"):

                    path = line.split(":", 1)[1].strip() or "/"

                    rules.append((agent, path))

            # If any rule for '*' (or our UA) disallows '/', block; else allow.

            for ua, path in rules:

                if ua in ("*", USER_AGENT) and path == "/":

                    self.logger.warning(f"🚫 robots disallow all at {base_url}")

                    return False

        except Exception as e:

            self.logger.info(f"⚠️ robots not enforced for {base_url}: {e}")

        return True

  

    # ----------- Source scrape ------------------------------------------------

    async def _scrape_source(self, session, source):

        base = source["url"].rstrip("/")

        if not await self._robots_allows(session, base):

            return []

        try:

            html = await self._fetch_text(session, base, timeout=REQUEST_TIMEOUT)

        except Exception as e:

            self.logger.error(f"❌ {source['name']} fetch error: {e}")

            return []

  

        return self._process_html(html, source)

  

    def _process_html(self, html, source):

        soup = BeautifulSoup(html, "html.parser")

  

        primary = source.get("article_selector", "")

        fallbacks = [

            "article a",

            "h2 a, h3 a",

            "a[href*='/news/'], a[href*='/story'], a[href*='/article']",

        ]

        selectors = [s for s in [primary] if s] + fallbacks

  

        elements = []

        used_selector = "NONE"

        for sel in selectors:

            elements = soup.select(sel)

            if elements:

                used_selector = sel

                break

  

        self.logger.info(f"🔍 {source['name']}: {len(elements)} elements via selector '{used_selector}'")

  

        seen = set()

        results, rejected = [], []

        cutoff_date = _now_utc() - timedelta(days=CUTOFF_DAYS)

  

        for element in elements[:200]:

            a_tag = self._extract_link(element)

            if not a_tag:

                continue

  

            title, href = self._extract_title_and_href(a_tag)

            if not ArticleValidator.is_valid_article(title, href, seen):

                rejected.append(self._rej(source, "invalid", title, href))

                continue

  

            # richer container for dates

            container = a_tag.parent if a_tag.name == "a" else a_tag

            if container and container.parent and container.parent.name not in ("html", "[document]"):

                container = container.parent

            pub_dt = DateExtractor.extract_date(container or element)

  

            if not pub_dt:

                results.append(self._res(source, title, href, None))

                continue

  

            if pub_dt < cutoff_date:

                rejected.append(self._rej(source, f"too_old ({pub_dt:%Y-%m-%d})", title, href))

                continue

  

            seen.add(title)

            results.append(self._res(source, title, href, pub_dt))

  

        self._log_results(source, results, rejected)

        return results

  

    # ----------- Helpers ------------------------------------------------------

    def _extract_link(self, element):

        return element if element.name == "a" else element.find("a")

  

    def _extract_title_and_href(self, a_tag):

        return a_tag.get_text(strip=True), a_tag.get("href", "")

  

    def _rej(self, source, reason, title, href):

        return {"source": source["name"], "reason": reason, "title": title, "url": href}

  

    def _res(self, source, title, href, pub_dt):

        full_url = urljoin(source["url"], str(href))

        return {

            "source": source["name"],

            "title": title,

            "url": f'=HYPERLINK("{full_url}", "Go!")',

            "date": pub_dt.strftime("%Y-%m-%d") if pub_dt else "undated",

            "timestamp": time.time(),

        }

  

    def _log_results(self, source, results, rejected):

        if results:

            dated = [r for r in results if r["date"] != "undated"]

            info = f" | Dated: {len(dated)}" if dated else ""

            self.logger.info(f"✅ {source['name']}: {len(results)} articles{info}")

        else:

            self.logger.warning(f"⚠️ {source['name']}: No valid articles")

        if rejected:

            with open(self.config.debug_csv, "a", newline="", encoding="utf-8") as f:

                writer = csv.DictWriter(f, fieldnames=["source", "reason", "title", "url"])

                if f.tell() == 0:

                    writer.writeheader()

                writer.writerows(rejected)

  

    def _save_results(self, results):

        flat = [item for sublist in results for item in sublist]

        if not flat:

            return

        with open(self.config.output_csv, "w", newline="", encoding="utf-8") as f:

            writer = csv.DictWriter(f, fieldnames=["source", "title", "url", "date", "timestamp"])

            writer.writeheader()

            writer.writerows(flat)

  

    def _log_summary(self, results, start_time):

        flat = [item for sublist in results for item in sublist]

        dated = [r for r in flat if r["date"] != "undated"]

  

        if dated:

            # parse dates as naive YYYY-MM-DD for summary only

            dates = [datetime.strptime(r["date"], "%Y-%m-%d") for r in dated]

            date_range = f"{min(dates):%Y-%m-%d} to {max(dates):%Y-%m-%d}"

        else:

            date_range = "N/A"

  

        summary = (

            f"\n🧾 Summary:\n"

            f"✅ Total articles: {len(flat)}\n"

            f"📅 Dated articles: {len(dated)}\n"

            f"📅 Date range: {date_range}\n"

            f"📄 CSV saved to: {self.config.output_csv}\n"

            f"🪵 Logs: {self.config.log_txt}\n"

            f"⏳ Duration: {time.time() - start_time:.2f}s\n"

            f"🧃 Rejections: {self.config.debug_csv}\n"

        )

        print(summary)

        self.logger.info(summary)

  

# ==============================================================================

# MAIN

# ==============================================================================

def main():

    try:

        cfg = ScraperConfig()

        engine = ScraperEngine(cfg)

        asyncio.run(engine.run())

    except Exception as e:

        logging.critical(f"🔥 Catastrophic failure: {e}")

        print(f"💥 Critical error: {e}")

        sys.exit(1)

  

if __name__ == "__main__":

    main()