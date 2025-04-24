# validate_backlinks.py (Version 2.1)

# Purpose: Validate wikilink connectivity inside Obsidian Vault (Anacostia)

# Author: digitalscorpyun | Maintained for Anacostia Vault Integrity

  

import os

import re

from collections import defaultdict

  

# === Configuration ===

VAULT_PATH = r"C:\Users\digitalscorpyun\KUSH\Anacostia"

  

# === Core Utilities ===

  

def validate_vault_path():

    """Ensure the defined vault path exists."""

    if not os.path.exists(VAULT_PATH):

        print(f"❌ Error: Vault path '{VAULT_PATH}' does not exist. Check the path and try again.")

        exit(1)

  

def get_links(file_path):

    """Extract [[wikilinks]] from a markdown file."""

    with open(file_path, 'r', encoding='utf-8') as f:

        content = f.read()

        return set(re.findall(r'\[\[(.*?)\]\]', content))

  

def check_backlinks():

    """Check backlink consistency and report orphans and weak links."""

    validate_vault_path()

    links = defaultdict(set)

  

    try:

        all_files = [f for f in os.listdir(VAULT_PATH) if f.endswith('.md')]

    except Exception as e:

        print(f"❌ Error accessing vault directory: {e}")

        exit(1)

  

    for file in all_files:

        file_path = os.path.join(VAULT_PATH, file)

        file_name = os.path.splitext(file)[0]  # Exclude .md extension

        linked_refs = get_links(file_path)

        links[file_name] = linked_refs

  

        # Build reverse (back) references

        for ref in linked_refs:

            links[ref].add(file_name)

  

    # Orphaned = no backlinks at all

    orphans = [f for f in all_files if not links[os.path.splitext(f)[0]]]

  

    # Weak links = only one connection

    weak_links = [f for f in all_files if len(links[os.path.splitext(f)[0]]) <= 1 and f not in orphans]

  

    # === Output Report ===

    print("\n=== 🔗 Backlink Validation Report (v2.1) ===")

  

    print("\n🔴 Orphaned Files (No Links):")

    print("\n".join(orphans) if orphans else "✅ None")

  

    print("\n🟡 Weakly Linked Files (1 Link Only):")

    print("\n".join(weak_links) if weak_links else "✅ None")

  

    print("\n🟢 Backlink Consistency Check Complete.")

  

# === Main ===

if __name__ == "__main__":

    check_backlinks()
