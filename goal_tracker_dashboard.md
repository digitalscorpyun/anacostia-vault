---
id: '20250511112837'
title: goal_tracker_dashboard
category: dashboards
style: ScorpyunStyle
path: ''
created: 2025-05-09
updated: '2025-05-11'
status: in_progress
priority: normal
summary: 'Dataview-powered dashboard for tracking personal development goals by category,
  status, and identity alignment.

  '
longform_summary: ''
tags:
- goal_tracking
- dashboards
- personal_development
- dataview
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


# 📊 Goal Tracker Dashboard – ScorpyunStyle™

> *"The grind becomes ritual when each goal feeds the soul, not the algorithm."*  
> — digitalscorpyun

This dashboard dynamically surfaces all active and in-progress goals from across your vault using `#goal_setting`. Filter by category, status, and more.

---

## ✅ Active Goals

```dataview
table 
  file.link as "Goal Note", 
  category, 
  status, 
  deadline, 
  identity as "Identity Link", 
  milestones
from "06_personal_development"
where contains(tags, "goal_setting") and status != "complete"
sort deadline asc
````

---

## 🕯️ Recently Completed Goals

```dataview
table 
  file.link as "Goal Note", 
  category, 
  deadline
from "06_personal_development"
where contains(tags, "goal_setting") and status = "complete"
sort deadline desc
limit 10
```

---

## 🔮 Goal Density by Category

```dataview
table category, length(rows) as "Count"
from "06_personal_development"
where contains(tags, "goal_setting")
group by category
```

---

**Pro Tip:** For best results, use the goal template block from `personal_development_goal_setting.md` and ensure each goal note is stored under `06_personal_development`.

Want a script suggestion to auto-generate goal notes from a prompt or form (`generate_goal_note.py`)?