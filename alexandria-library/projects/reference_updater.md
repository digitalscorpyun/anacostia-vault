import os
import datetime

def update_references(directory):
    """
    Updates the references.md file with a new entry based on user input.
    Args:
        directory (str): The root directory of the Anacostia Vault.
    """
    ref_path = os.path.join(directory, "references.md")
    
    # Ensure the references.md file exists, create it if it doesn't
    if not os.path.exists(ref_path):
        with open(ref_path, "w") as f:
            f.write("""---
tags: references, knowledge_base, royal_purple  
related-topics:  
  - [[computer-science-index]]  
  - [[ai-fairness-360]]  
  - [[africana-studies-overview]]  
created: 2025-03-18  
updated: 2025-03-18  
---

# References  
🏴 **Category**: Knowledge Base / References  
🏴 **Location**: `anacostia-vault`  
🏴 **Date Created**: 2025-03-18  
🏴 **Last Updated**: 2025-03-18  

## 🌌 The Royal Purple Ledger of Wisdom  
*"Each reference is a drumbeat of resistance."*  
— Anacostia Vault Proverb  

This note stores summarized readings, aligning with Sönke Ahrens’ *How to Take Smart Notes* (2022)—[[africana-studies-decolonization-of-africa]]. It supports Python mastery and AI fairness—[[python-studies]], [[the-lion-of-anacostia-bias-detection]].

### 📚 Reference Entries  
*Note*: Requires Dataview (see `[[readme-computer-science-index]]`).  
```dataview  
TABLE title AS "Title", author AS "Author", date AS "Date", summary AS "Summary", link AS "Link"  
FROM "anacostia-vault"  
WHERE contains(file.name, "references") AND file.name != this.file.name  
SORT date DESC  