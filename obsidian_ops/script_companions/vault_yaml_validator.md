#!/usr/bin/env python3

  

"""

🛡️ vault_yaml_validator.py

Scans all markdown files in the Anacostia Vault and validates that:

- Each contains YAML frontmatter

- YAML block has exactly 21 fields

- Logs results to a summary report scroll

"""

  

import os

import re

import yaml

from datetime import datetime

  

# === CONFIG ===

VAULT_PATH = "/mnt/c/Users/digitalscorpyun/sankofa_temple/Anacostia"

OUTPUT_FILE = os.path.join(VAULT_PATH, "vault_ops/vault_yaml_validator_status.md")

REQUIRED_FIELDS = [

    "id", "title", "category", "style", "path", "created", "updated", "review_date",

    "status", "priority", "summary", "longform_summary", "tags", "cssclasses",

    "synapses", "key_themes", "bias_analysis", "grok_ctx_reflection", "quotes",

    "adinkra", "linked_notes"

]

  

# === HELPERS ===

  

def extract_yaml_block(content):

    """Extract YAML frontmatter block from markdown content"""

    if content.startswith("---"):

        parts = content.split("---", 2)

        if len(parts) > 2:

            return parts[1].strip()

    return None

  

def validate_fields(yaml_dict):

    """Return missing and extra fields relative to REQUIRED_FIELDS"""

    keys = list(yaml_dict.keys())

    missing = [f for f in REQUIRED_FIELDS if f not in keys]

    extra = [f for f in keys if f not in REQUIRED_FIELDS]

    return missing, extra

  

# === SCAN LOGIC ===

  

results = []

for root, _, files in os.walk(VAULT_PATH):

    for filename in files:

        if filename.endswith(".md"):

            full_path = os.path.join(root, filename)

            rel_path = os.path.relpath(full_path, VAULT_PATH)

            with open(full_path, "r", encoding="utf-8") as f:

                content = f.read()

            yaml_block = extract_yaml_block(content)

            if not yaml_block:

                results.append((rel_path, "❌ No YAML frontmatter", [], []))

                continue

            try:

                parsed = yaml.safe_load(yaml_block)

                if not isinstance(parsed, dict):

                    raise ValueError("YAML is not a dictionary")

                missing, extra = validate_fields(parsed)

                if not missing and not extra:

                    results.append((rel_path, "✅ Valid", [], []))

                else:

                    results.append((rel_path, "⚠️ Field mismatch", missing, extra))

            except Exception as e:

                results.append((rel_path, f"❌ YAML error: {e}", [], []))

  

# === OUTPUT REPORT ===

  

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

  

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:

    f.write(f"# 🛡️ Vault YAML Validation Report\n")

    f.write(f"**Generated:** {timestamp}\n\n")

    f.write("| File | Status | Missing Fields | Extra Fields |\n")

    f.write("|------|--------|----------------|---------------|\n")

    for rel_path, status, missing, extra in results:

        missing_str = ", ".join(missing) if missing else ""

        extra_str = ", ".join(extra) if extra else ""

        f.write(f"| `{rel_path}` | {status} | {missing_str} | {extra_str} |\n")

  

print(f"✅ Validation complete. Report written to: {OUTPUT_FILE}")