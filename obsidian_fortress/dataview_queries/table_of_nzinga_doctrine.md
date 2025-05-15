---
id: '20250511112837'
title: dataview_table_of_nzinga_doctrine
category: meta_index
style: ScorpyunStyle
path: ''
created: '2025-05-09'
updated: '2025-05-11'
status: in_progress
priority: normal
summary: A dynamic table listing all notes aligned with Nzinga’s strategic framework
  for AI ethics, governance, and resistance.
longform_summary: ''
tags:
- nzinga
- ai_ethics
- doctrine_table
- vault_ops
cssclasses:
- sacred-tech
synapses: []
key_themes: []
bias_analysis: ''
grok_ctx_reflection: ''
quotes: []
adinkra: []
linked_notes: []
---


```dataview
table title as "Doctrine Node", concept_link as "Strategic Link", summary
from "ai_ethics"
where contains(tags, "nzinga")
sort file.name asc
