import os
import re
from collections import defaultdict

# Set path to your Obsidian Vault
VAULT_PATH = r"C:\Users\miker\OneDrive\Documents\Anacostia"  # Updated with actual vault path

# Ensure the vault path exists
def validate_vault_path():
    if not os.path.exists(VAULT_PATH):
        print(f"Error: Vault path '{VAULT_PATH}' does not exist. Check the path and try again.")
        exit(1)

def get_links(file_path):
    """Extract [[wikilinks]] from a markdown file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        return set(re.findall(r'\[\[(.*?)\]\]', content))

def check_backlinks():
    """Check backlink consistency across markdown files."""
    validate_vault_path()
    links = defaultdict(set)
    
    try:
        all_files = [f for f in os.listdir(VAULT_PATH) if f.endswith('.md')]
    except Exception as e:
        print(f"Error accessing vault directory: {e}")
        exit(1)
    
    # Build link map
    for file in all_files:
        file_path = os.path.join(VAULT_PATH, file)
        links[file] = get_links(file_path)
        for linked_file in links[file]:
            links[linked_file].add(file)  # Ensure bidirectional linking
    
    # Find orphaned and weakly linked files
    orphans = [f for f in all_files if not links[f]]
    weak_links = [f for f in all_files if len(links[f]) <= 1 and f not in orphans]
    
    # Output results
    print("=== Backlink Validation Report ===")
    print("\n🔴 Orphaned Files (No Links):")
    print("\n".join(orphans) if orphans else "None")
    
    print("\n🟡 Weakly Linked Files (1 Link Only):")
    print("\n".join(weak_links) if weak_links else "None")
    
    print("\n🟢 Backlink Consistency Check Done!")
    
if __name__ == "__main__":
    check_backlinks()
