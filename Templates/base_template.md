---
id: <% tp.date.now("YYYYMMDDHHmmss") %>  # 1. Unique timestamp ID
title: <% tp.file.title %>  # 2. Note title (auto-fills from filename)
category: <% tp.system.prompt('Enter category (e.g., afrikan_studies, ai_ethics, media_analysis)') %>  # 3. Top-level content category
style: <% tp.system.suggester(['ScorpyunStyle', 'UBW', 'GriotBox'], ['ScorpyunStyle']) %>  # 4. Formatting style
path: <% tp.system.prompt('Enter folder path (e.g., afrikan_frontlines, obsidian_fortress)') %>  # 5. Relative vault path
created: <% tp.date.now('YYYY-MM-DD HH:mm') %>  # 6. Creation timestamp
updated: <% tp.date.now('YYYY-MM-DD HH:mm') %>  # 7. Last updated timestamp
status: <% tp.system.suggester(['idea', 'in_progress', 'complete'], ['in_progress']) %>  # 8. Current progress status
priority: <% tp.system.suggester(['high', 'medium', 'low'], ['medium']) %>  # 9. Urgency level
summary:  # 10. One-sentence overview
longform_summary: ""  # 11. Extended summary (optional)
tags:  # 12. Topic tags in snake_case
cssclasses:  # 13. Style classes for Obsidian theming
synapses:  # 14. Thought-links or idea chains
  - ""
  - ""
  - ""
  - ""
key_themes:  # 15. Core topics or concepts
  - ""
  - ""
  - ""
bias_analysis: ""  # 16. Embedded assumptions or systemic angles
grok_ctx_reflection: ""  # 17. AI ethics, system design, or reflection zone
quotes:  # 18. Notable excerpts or references
  - ""
  - ""
  - ""
adinkra:  # 19. Symbolic glyphs for cultural alignment
  - 🦢 sankofa
linked_notes:  # 20. Manual backlinks to related vault notes
  - - - sankofa_spine
  - - - digitalscorpyun_manifesto_and_syllabus
  - - - 00_session_context
  - - - 00_to_do_list
---

# <%= tp.file.title %>

## 📌 Overview
<%= tp.frontmatter.summary || "Write a brief description of what this note captures..." %>

---

## 📖 Longform Summary
<%= tp.frontmatter.longform_summary || "Optional detailed breakdown goes here..." %>

---

## 🔑 Key Themes
<% for (let theme of tp.frontmatter.key_themes || ["", "", ""]) { %>
- <%= theme %>
<% } %>

---

## ⚖️ Bias Analysis
<%= tp.frontmatter.bias_analysis || "(Identify embedded assumptions or blind spots here...)" %>

---

## 🤖 GROK-CTX Reflections
<%= tp.frontmatter.grok_ctx_reflection || "(Use this space for AI ethics or design implications...)" %>

---

## 🧠 Synapses
<% for (let syn of tp.frontmatter.synapses || []) { %>
- <%= syn %>
<% } %>

---

## 📜 Quotes
<% for (let quote of tp.frontmatter.quotes || []) { %>
> “<%= quote %>”
<% } %>

---

## 🔗 Linked Notes
<% if (tp.frontmatter.linked_notes && tp.frontmatter.linked_notes.length > 0) { %>
> [!links]+ Connected Threads
<% for (let link of tp.frontmatter.linked_notes) { %>
> - [[<%= link.replace(/\.md|\.py$/, "") %>]]
<% } %>
<% } else { %>
> [!info] No linked notes yet.
<% } %>

---

## 🏷️ Tags
<% if (tp.frontmatter.tags && tp.frontmatter.tags.length > 0) { %>
<% for (let tag of tp.frontmatter.tags) { %>
#<%= tag %> 
<% } %>
<% } else { %>
#uncategorized
<% } %>
