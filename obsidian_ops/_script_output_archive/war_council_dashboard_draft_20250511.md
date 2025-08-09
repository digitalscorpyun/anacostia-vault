---
review_date: 2025-05-17
id: '20250511165400'
title: war_council_dashboard_draft_20250511
category: archive
style: ScorpyunStyle
path: archive/war_council_dashboard_draft_20250511.md
created: 2025-05-11 16:54
updated: 2025-05-12
status: archived
priority: low
summary: Deprecated war council dashboard draft with early DataView logic and partial strategic pillar mapping. Superseded by `war_council.md`.
tags:
  - archive
  - deprecated
  - war_council
cssclasses:
  - tyrian-purple
linked_notes:
  - war_council.md
  - python_artillery
  - africana_studies
  - sacred_texts
  - ai_ethics
  - obsidian_fortress
---

# 🛡️ [ARCHIVED] War Council – Operational Dashboard (2025-05-11 Draft)

> This dashboard was an early scaffolding of the **War Council** note.  
> Replaced by [[war_council.md]] with improved `Live Orders of Battle`, `Connected Glyphs`, and canonical path compliance.

---

## 🧭 Early Strategic Pillars

| Front               | Index Note              |
|---------------------|--------------------------|
| Africana Studies     | [[africana_studies]]     |
| AI Ethics            | [[ai_ethics]]            |
| Python Artillery     | [[python_artillery]]     |
| Obsidian Fortress    | [[obsidian_fortress]]    |
| Sacred Texts         | [[sacred_texts]]         |

---

## ❌ Deprecated DataView

```dataview
TABLE WITHOUT ID
  file.link AS "Operation",
  dateformat(file.mtime, "yyyy-MM-dd") AS "Last Updated"
FROM #active_mission
SORT file.mtime DESC
LIMIT 7


# 🛡️ War Council

## Strategic Pillars
| Front               | Index Note              |
|---------------------|--------------------------|
| Africana Studies     | [[africana_studies]]     |
| AI Ethics            | [[ai_ethics]]            |
| Python Artillery     | [[python_artillery]]     |
| Obsidian Fortress    | [[obsidian_fortress]]    |
| Sacred Texts         | [[sacred_texts]]         |

## Active Missions

```dataview
TABLE WITHOUT ID
  file.link AS "Operation",
  dateformat(file.mtime, "yyyy-MM-dd") AS "Last Updated"
FROM #active_mission
SORT file.mtime DESC
LIMIT 7```

## 🜃 Connected Glyphs
- [[note_one]]
- [[note_two]]
- [[note_three]]
## 🄃 Connected Glyphs

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
