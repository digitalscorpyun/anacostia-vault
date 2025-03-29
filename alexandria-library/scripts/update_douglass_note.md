import pandas as pd
import re

# Paths
csv_path = "anacostia-vault/logs/reading_log.csv"
md_path = "anacostia-vault/history/03182025-douglass-anacostia-muller.md"

# Read CSV
df = pd.read_csv(csv_path)
chapter_6 = df[df['chapter'] == 6].iloc[0]  # Get Chapter 6 row
summary = chapter_6['summary']
date = chapter_6['date']

# Create new callout
new_callout = f"""> [!note] Literature Note: Chapter 6 Summary ({date})
> Muller’s *Frederick Douglass in Washington, D.C.: The Lion of Anacostia* (Chapter 6) {summary}—[[africana-studies-overview]].  
> - Linked to:  
>   - [[9-8]] (Bias Detection Context: Ethical leadership in fairness)  
>   - [[9-8a]] (Leadership in Anacostia: Governance and equity)  
> - *Source*: Muller, John, *Frederick Douglass in Washington, D.C.: The Lion of Anacostia* (2022), Chapter 6.
"""

# Read the Markdown file
with open(md_path, 'r') as f:
    content = f.read()

# Find the Content section and insert the new callout
content = re.sub(r'(## 📝 Content\n\n)', f'## 📝 Content\n\n{new_callout}\n', content)

# Update Changelog
changelog_entry = f"- 2025-03-18: Added Chapter 6 summary.\n"
content = re.sub(r'(## 📅 Changelog\n)', f'## 📅 Changelog\n{changelog_entry}', content)

# Write back to the file
with open(md_path, 'w') as f:
    f.write(content)

print("Updated 03182025-douglass-anacostia-muller.md with Chapter 6 summary.")