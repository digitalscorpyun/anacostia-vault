---
created: '2025-01-01'
tags:
- personal_development
- journaling
- daily_guidelines
title: Personal Development - Daily Journal Guide
---

# Personal Development - Daily Journal Guide

This note is your central resource for orchestrating your daily reflections. It provides a framework for journaling, offers prompts to spark deep insights, and dynamically displays your most recent daily notes using Dataview. Use this guide to keep your daily reflections consistent and aligned with your overall growth strategy.

---

## Journaling Framework

### Structure Your Day

1. **Morning Intention:**  
   - Single most important focus.  
   - Quick check of your mindset.

2. **Midday Check-In:**  
   - Current wins, challenges, or redirection needed.

3. **Evening Wrap-Up:**  
   - Key takeaways, gratitude, any final reflection.

---

## Prompts

- "What new insight did I discover about myself today?"
- "Where can I improve tomorrow based on today's lessons?"
- "How am I progressing toward my broader goals?"

---

## Recent Daily Notes (Dataview)

```dataview
TABLE file.mtime AS "Last Modified", file.link AS "Daily Note"
FROM "Daily Notes"
WHERE contains(file.name, "2025")
SORT file.mtime desc
LIMIT 5

