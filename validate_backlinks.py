import os
import re
from collections import defaultdict

# ✅ Define the path to your Anacostia Vault (Make sure this is correct)
VAULT_PATH = r"C:\Users\digitalscorpyun\KUSH\Anacostia"

# ✅ Regular expression to find all backlinks in a file
BACKLINK_PATTERN = re.compile(r'\[\[(.*?)\]\]')

# ✅ Dictionary to store backlinks
backlink_map = defaultdict(set)
all_files = []

def collect_files():
    """
    Recursively collect all .md files in the vault directory.
    """
    for root, _, files in os.walk(VAULT_PATH):
        for file in files:
            if file.endswith('.md'):
                all_files.append(os.path.join(root, file))

def extract_backlinks(file_path):
    """
    Extract backlinks from a given file.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        matches = BACKLINK_PATTERN.findall(content)
        return matches

def get_file_name(file_path):
    """
    Extract the file name without the .md extension.
    """
    return os.path.splitext(os.path.basename(file_path))[0]

def check_backlinks():
    """
    Build a backlink map and check for consistency.
    """
    collect_files()
    all_file_names = {get_file_name(f) for f in all_files}
    
    for file_path in all_files:
        file_name = get_file_name(file_path)
        backlinks = extract_backlinks(file_path)
        
        for link in backlinks:
            backlink_map[link].add(file_name)

    orphaned_files = []
    weakly_linked_files = []

    for file_name in all_file_names:
        if file_name not in backlink_map:
            orphaned_files.append(file_name)
        elif len(backlink_map[file_name]) == 1:
            weakly_linked_files.append(file_name)

    # Generate Report
    print("\n📋 Backlink Validation Report\n")
    
    if orphaned_files:
        print("🔴 Orphaned Files (No Incoming Links):")
        for file in orphaned_files:
            print(f" - {file}")
    else:
        print("✅ No Orphaned Files Detected.")

    if weakly_linked_files:
        print("\n🟡 Weakly Linked Files (Only One Incoming Link):")
        for file in weakly_linked_files:
            print(f" - {file}")
    else:
        print("✅ No Weakly Linked Files Detected.")

    print("\n✅ Backlink Consistency Check Done.")

if __name__ == "__main__":
    check_backlinks()
