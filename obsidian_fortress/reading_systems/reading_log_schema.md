---
id: '20250511112837'
title: reading_log_schema
category: vault_ops
style: ScorpyunStyle
path: ''
created: 2025-05-07 22:47
updated: '2025-05-11'
status: in_progress
priority: normal
summary: This schema defines the required JSON structure for all summaries logged
  by OD‑COMPLY and related AVM agents into the reading_log.csv.
longform_summary: ''
tags:
- reading_systems
- data_schema
- od_comply
- vault_integrity
- scorpyunstyle
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

# 📊 reading_log_schema

**Purpose**:  
This schema defines the **canonical JSON structure** for AI-generated reading summaries used in `reading_log.csv`, Markdown note generation, and multi-agent workflows in the Anacostia Vault.

---

## 🧱 Required JSON Fields

| Field                  | Type     | Description                                                                 |
|------------------------|----------|-----------------------------------------------------------------------------|
| `author`               | string   | Primary author of the source                                               |
| `title`                | string   | Title of the book or media                                                 |
| `chapter`              | string   | Specific chapter or section covered                                        |
| `summary`              | string   | Core summary text (1–3 paragraphs)                                         |
| `key_takeaways`        | array    | Bullet list of essential concepts                                          |
| `critical_analysis`    | array    | Bullet list of critiques, insights, or stylistic evaluations               |
| `contemporary_connection` | array | Bullet list of real-world relevance and use cases                         |
| `date_read`            | string   | Date material was read (format: `YYYY-MM-DD`)                             |
| `published_date`       | string   | Original publish date (format: `YYYY-MM-DD` or year only)                 |
| `source_type`          | string   | One of: `"Book"`, `"Article"`, `"Podcast"`, `"Video"`, etc.               |
| `source_url`           | string   | Optional—URL if source is digital                                          |
| `extracted_by`         | string   | Agent or tool that generated the summary (e.g., `"OD-COMPLY"`, `"LLM"`)   |

---

## 📁 Usage in Vault Systems

- `reading_log.csv`: Flattened and appended for overview/logging
- `03_research/`: Used to auto-generate `.md` notes with YAML frontmatter
- Agent pipelines: Referenced by micro-agents for summarization, tagging, linking
- Obsidian queries: Accessed via Dataview or custom scripts for thematic exploration

---

## 📌 Sample Entry (JSON)

```json
{
  "author": "Eric Matthes",
  "title": "Python Crash Course",
  "chapter": "Part I: Basics - Control Flow",
  "summary": "...",
  "key_takeaways": ["...", "..."],
  "critical_analysis": ["...", "..."],
  "contemporary_connection": ["...", "..."],
  "date_read": "2025-05-07",
  "published_date": "2019-05-03",
  "source_type": "Book",
  "source_url": "",
  "extracted_by": "OD-COMPLY"
}

## 🜃 Connected Glyphs
<%*
if (!tp.frontmatter || !Array.isArray(tp.frontmatter.linked_notes)) {
  tR += "⚠️ No linked_notes found in frontmatter.";
} else {
  for (let note of tp.frontmatter.linked_notes) {
    tR += `- [[${note.replace(/\.md$/, "")}]]
`;
  }
}
%>
