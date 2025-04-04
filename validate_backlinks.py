<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> c12a7c54309f53da18c7759e2595707f58d593e6
import os
import re
from collections import defaultdict

<<<<<<< HEAD
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
=======
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
=======
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
>>>>>>> 769b11b2f1b8510b1da5db510583301e7c9784a9
>>>>>>> c12a7c54309f53da18c7759e2595707f58d593e6
