# validate_backlinks_refactored.py (Version 2.2)
# Purpose: Validate wikilink connectivity inside Obsidian Vault (Anacostia)
# Author: digitalscorpyun | Maintained for Anacostia Vault Integrity

import os
import re
from collections import defaultdict

# === Configuration ===
VAULT_PATH = r"C:\Users\digitalscorpyun\KUSH\Anacostia"

def validate_vault_path():
    """Ensure the defined vault path exists."""
    if not os.path.exists(VAULT_PATH):
        print(f"❌ Error: Vault path '{VAULT_PATH}' does not exist. Check the path and try again.")
        exit(1)

def get_forward_links(file_path):
    """Extract [[wikilinks]] from a markdown file as a set of forward references."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        # Find all wikilinks, ignoring possible alias or pipe usage
        # Example: [[ai-fairness-tools|Fairness Tools]]
        links = re.findall(r'\[\[([^|\]]+)(?:\|[^\]]*)?\]\]', content)
        return set(links)

def check_backlinks():
    """Check forward and backward references, report on orphaned and weakly linked files."""
    validate_vault_path()

    # references[file_name] = set of forward references (where this file links to)
    references = defaultdict(set)
    # backlinks[file_name] = set of backward references (other files pointing to this file)
    backlinks = defaultdict(set)

    try:
        all_files = [f for f in os.listdir(VAULT_PATH) if f.endswith('.md')]
    except Exception as e:
        print(f"❌ Error accessing vault directory: {e}")
        exit(1)

    # Build references and backlinks
    for file in all_files:
        file_path = os.path.join(VAULT_PATH, file)
        file_name = os.path.splitext(file)[0]  # Exclude .md extension

        # Gather forward links from current file
        fwd_links = get_forward_links(file_path)
        references[file_name] = fwd_links

        # Populate backlinks for each referenced file
        for ref in fwd_links:
            backlinks[ref].add(file_name)

    # Initialize any file that might not have been referenced at all
    for file in all_files:
        file_name = os.path.splitext(file)[0]
        # Ensure each file is in the backlinks dictionary
        if file_name not in backlinks:
            backlinks[file_name] = set()

    # ORPHANED FILES: No one links to them => empty backlinks
    orphans = []
    for file in all_files:
        base_name = os.path.splitext(file)[0]
        if len(backlinks[base_name]) == 0:
            orphans.append(file)

    # WEAK LINKS: Only one inbound link
    # (Ignore orphans, because they have zero inbound links)
    weak_links = []
    for file in all_files:
        base_name = os.path.splitext(file)[0]
        if file not in orphans and len(backlinks[base_name]) == 1:
            weak_links.append(file)

    # === OUTPUT REPORT ===
    print("\n=== 🔗 Backlink Validation Report (v2.2) ===")

    print("\n🔴 Orphaned Files (No Inbound Links):")
    if orphans:
        print("\n".join(orphans))
    else:
        print("✅ None")

    print("\n🟡 Weakly Linked Files (Exactly 1 Inbound Link):")
    if weak_links:
        print("\n".join(weak_links))
    else:
        print("✅ None")

    print("\n🟢 Backlink Consistency Check Complete.\n")

    # (Optional) Print summary of total references/backlinks
    total_files = len(all_files)
    print(f"Total .md files in vault: {total_files}")
    print(f"Orphaned files: {len(orphans)}")
    print(f"Weakly linked files: {len(weak_links)}")

# === Main ===
if __name__ == "__main__":
    check_backlinks()
