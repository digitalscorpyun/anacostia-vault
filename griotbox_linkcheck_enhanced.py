# usage:
#   python scripts/griotbox_linkcheck.py --dry-run
#   python scripts/griotbox_linkcheck.py --online   (does HTTP checks)
import re, sys, argparse, datetime as dt, pathlib
from urllib.parse import urlparse

MD_PATH = r"C:\Users\digitalscorpyun\sankofa_temple\Anacostia\social\griotbox_feed.md"

def extract_links(text):
    # [label](url) and raw http(s)://... links
    md = re.findall(r'\[[^\]]*\]\(([^)]+)\)', text)
    raw = re.findall(r'(?<!\()https?://[^\s)>\]]+', text)
    return sorted(set(md + raw))

def online_check(urls, timeout=6):
    import requests
    bad = []
    for u in urls:
        try:
            # HEAD first, fallback to GET on 405/403
            r = requests.head(u, allow_redirects=True, timeout=timeout)
            if r.status_code in (403, 405):
                r = requests.get(u, allow_redirects=True, timeout=timeout, stream=True)
            if r.status_code >= 400:
                bad.append((u, r.status_code))
        except Exception as e:
            bad.append((u, str(e)[:120]))
    return bad

def main(dry=False, online=False):
    ts = dt.datetime.utcnow().replace(microsecond=0).isoformat() + "Z"
    p = pathlib.Path(MD_PATH)
    if not p.exists():
        print(f"[{ts}] ERROR: missing file: {MD_PATH}")
        return 2
    text = p.read_text(encoding="utf-8", errors="ignore")
    links = extract_links(text)
    print(f"[{ts}] Found {len(links)} link(s) in griotbox_feed.md")

    if not links:
        print("[info] nothing to check.")
        return 0

    if online:
        print("[info] running online checks…")
        bad = online_check(links)
        if bad:
            print(f"[fail] {len(bad)} bad link(s):")
            for u, why in bad:
                print(f"  - {u}  ->  {why}")
            return 1
        print("[ok] all links reachable.")
    else:
        # Offline summary only
        domains = {}
        for u in links:
            domains.setdefault(urlparse(u).netloc.lower(), 0)
            domains[urlparse(u).netloc.lower()] += 1
        top = sorted(domains.items(), key=lambda x: (-x[1], x[0]))[:10]
        print("[info] top domains:")
        for d, n in top:
            print(f"  {d}: {n}")
    return 0

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="kept for compatibility; no-op")
    ap.add_argument("--online", action="store_true", help="perform HTTP reachability checks")
    args = ap.parse_args()
    sys.exit(main(dry=args.dry_run, online=args.online))