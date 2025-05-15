---
id: '20250511112837'
title: war_council
category: war_council
style: ScorpyunStyle
path: war_council/war_council.md
created: 2025-05-03 11:50
updated: 2025-05-12 18:17:00
status: in_progress
priority: high
summary: Central strategic operations note for the AVM Syndicate. Tracks all fronts of resistance, coordination between agents, and vault geometry updates through live glyph activity.
tags:
  - active_mission
  - vault_dashboard
  - scorpyunstyle
  - war_council
cssclasses:
  - tyrian-purple
  - sacred-tech
linked_notes:
  - sankofa_spine.md
  - session_context.md
  - avm_syndicate_gameplan.md
  - grok_ctx_session_handoff.md
  - anacostia_vault_structure.md
  - vault_path_map.md
---

# 🛡️ War Council

> *“Burn the plantations. Build a fortress.”*

---

## 🧭 Strategic Pillars

| Front                 | Command Note                        |
|----------------------|--------------------------------------|
| Africana Studies      | [[africana_studies]]                 |
| AI Ethics             | [[ai_ethics]]                        |
| Python Projects       | [[projects/python_projects]]         |
| Obsidian Fortress     | [[obsidian_fortress]]                |
| Sacred Texts          | [[sacred_texts]]                     |
| Personal Development  | [[personal_development]]             |
| AVM Syndicate Ops     | [[avm_syndicate_gameplan.md]]        |

---

## 🛰️ Live Orders of Battle

> *All active mission files tagged with `#active_mission` will auto-populate below.*

```dataview
TABLE WITHOUT ID
  file.link AS "Active Operation",
  dateformat(file.mtime, "yyyy-MM-dd") AS "Last Engagement"
FROM #active_mission
SORT file.mtime DESC
LIMIT 7
```

## 🜃 Connected Glyphs

- [[grok_ctx_session_handoff.md]]
- [[anacostia_vault_structure.md]]
- [[sankofa_spine.md]]
- [[vault_path_map.md]]
- [[session_context.md]]
- [[avm_syndicate_gameplan.md]]
