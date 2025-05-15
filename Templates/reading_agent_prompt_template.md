---
id: '20250511112837'
title: Reading Agent Prompt Template
category: ''
style: ScorpyunStyle
path: ''
created: '2025-05-11'
updated: '2025-05-11'
status: in_progress
priority: normal
summary: ''
longform_summary: ''
tags: []
cssclasses:
- tyrian-purple
- sacred-tech
synapses: []
key_themes: []
bias_analysis: ''
grok_ctx_reflection: ''
quotes: []
adinkra: []
linked_notes: []
---

Thought for a second

Below is a **ScorpyunStyle reading‑agent prompt template**. Drop it into your `extract_and_summarize.py` or Obsidian reading‑log entry and fill in the `{{…}}` fields when you call the agent.

````markdown
```yaml
author: "{{author_name}}"
title: "{{work_title}}"
chapter: "{{chapter_or_section}}"
date_read: "{{YYYY-MM-DD}}"
published_date: "{{original_publication_date}}"
notes_path: "04_code/technical_mastery/reading_logs/{{file_name}}.md"
tags:
  - africana_theory
  - ai_ethics
  - sacred_tech
source_type: "{{Book|Article|Podcast}}"
source_url: "{{URL_if_applicable}}"
extracted_by: "{{agent_name}}"
````

# ScorpyunStyle Summary

Use the following sections in your analysis:

## Key Takeaways

– {{bullet_point_1}}  
– {{bullet_point_2}}  
– …

## Historical & Cultural Context

Provide graduate‑level grounding in Africana history, colonial legacies, and epistemic resistance.

## Critical Analysis

Engage with the text through Africana/Womanist/postcolonial critique; highlight tensions, blind spots, and revolutionary potential.

## Contemporary Connection

Tie themes to current social movements, tech ethics debates, or algorithmic justice efforts.

## Relevance to Tech, AI Ethics, or Black Thought

Explain how this maps onto sacred‑tech narratives, AI bias frameworks, or Black radical tradition.

## Conclusion or Reflection

Offer a closing reflection or ritual invocation that speaks to your Algorithmic Griot persona.

```

**How to use:**  
1. Replace `{{…}}` placeholders with your text metadata.  
2. Send the entire block (YAML + Markdown) to your AI agent.  
3. The agent will return a ready‑to‑paste note or a CSV row following your vault conventions.

This ensures every summary is **ScorpyunStyle**, **structured**, and **automation‑friendly**.
```