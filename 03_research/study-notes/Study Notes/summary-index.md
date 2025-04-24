---
category: Vault Infrastructure
created: 2025-04-11
tags:
- dashboard
- summary_index
title: "\U0001F4CA Summary Index"
updated: 2025-04-11
---

## 📊 Summary Index

```dataview
table file.link as "📁 File", 
      title as "📌 Title", 
      category as "📂 Category", 
      created as "🕰️ Created", 
      updated as "♻️ Updated", 
      synapses as "🧠 Synapses"
from ""
where contains(tags, "summary")
sort created desc

