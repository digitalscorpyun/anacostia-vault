import os
import re
import yaml
from collections import defaultdict

# ✅ Define the path to your Anacostia Vault
VAULT_PATH = r"C:\Users\digitalscorpyun\KUSH\Anacostia"

# ✅ File extension to look for
FILE_EXTENSION = '.md'

# ✅ Regular expression to capture YAML front matter
YAML_PATTERN = re.compile(r'^---\n(.*?)\n---', re.DOTALL)

# ✅ Dictionary to store tags and their associated files
tag_map = defaultdict(set)

def collect_files():
    """
    Recursively collect all .md files in the vault directory.
    """
    all_files = []
    for root, _, files in os.walk(VAULT_PATH):
        for file in files:
            if file.endswith(FILE_EXTENSION):
                all_files.append(os.path.join(root, file))
    return all_files

def extract_tags(file_path):
    """
    Extract tags from the YAML front matter of a file.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        yaml_match = YAML_PATTERN.search(content)
        if yaml_match:
            yaml_content = yaml_match.group(1)
            try:
                parsed_yaml = yaml.safe_load(yaml_content)
                if parsed_yaml and 'tags' in parsed_yaml:
                    tags = parsed_yaml['tags']
                    if isinstance(tags, list):
                        return tags
                    elif isinstance(tags, str):
                        return [tags]
            except yaml.YAMLError:
                pass
    return []

def check_tags():
    """
    Build a tag map and check for related notes via tags.
    """
    all_files = collect_files()
    file_name_map = {os.path.splitext(os.path.basename(f))[0]: f for f in all_files}

    for file_path in all_files:
        file_name = os.path.splitext(os.path.basename(file_path))[0]
        tags = extract_tags(file_path)
        
        for tag in tags:
            tag_map[tag].add(file_name)

    # Generate Report
    print("\n📋 Tag-Based Linking Report\n")
    for tag, files in tag_map.items():
        if len(files) > 1:
            print(f"\n🟢 Tag: {tag}")
            for file in files:
                print(f" - {file}")
    print("\n✅ Tag-Based Linking Analysis Done.")

if __name__ == "__main__":
    check_tags()
