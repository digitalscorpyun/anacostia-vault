---
review_date: 2025-11-17
id: '20250510224500'
title: task_dashboard
category: vault_ops
style: ScorpyunStyle
path: 00_war_council/task_dashboard
created: 2025-05-10 22:45
updated: 2025-08-17 15:30
status: active
priority: high
summary: Dynamic Dataview-powered task dashboard pulling live to-dos from the Anacostia Vault.
longform_summary: >
  This dashboard aggregates and visualizes all incomplete tasks from core war-council lists
  and project scrolls, grouped by sections, due dates, and source notes. It respects YAML
  metadata (title, category, status, priority) and enforces Scorpyun discipline for sacred-tech ops.
tags:
  - dashboard
  - vault_ops
  - dataview
  - scorpyunstyle
  - task_management
  - sacred_tech
cssclasses:
  - tyrian-purple
  - sacred-tech
synapses:
  - session_context
  - summary_styles_guide
key_themes:
  - operational_rhythm
  - prioritization
  - ritual_review
bias_analysis: Operational only; no content bias expected. Ensure due-date logic doesn’t over-police creative notes.
grok_ctx_reflection: The vault breathes through tasks; this board is its pulse. Begin wide, then act precise.
quotes:
  - "Begin wide, finish precise."
adinkra:
  - Nkyinkyim
  - Eban
linked_notes:
  - to_do_list
  - session_context
  - roadmap_anacostia_vault
  - vault_structure_emitter
---

# 🗂️ Task Dashboard (War Council)

**Aim:** See everything. Touch what matters. Move one sacred stone at a time.

---

## ✅ Open Tasks (To-Do List Nerve Center)

```dataview
table t.text as "Task", file.link as "Note", t.section as "Section"
from "00_war_council/to_do_list"
flatten file.tasks as t
where !t.completed
sort t.section asc, t.text asc
