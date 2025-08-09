---
id: '20250511112837'
title: dataview_query_black_identity_web
category: meta_index
style: ScorpyunStyle
path: ''
created: '2025-05-09'
updated: '2025-05-11'
status: in_progress
priority: normal
summary: Dataview-powered map of vault notes connected to Black identity, culture,
  resistance aesthetics, and narrative sovereignty across the African diaspora.
longform_summary: ''
tags:
- dataview
- black_culture
- identity
- cultural_memory
- vault_ops
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


# 🧭 Black Identity Web – Vault Query Map

> _“Identity is the chorus—culture is the rhythm. We track both in sacred syntax.”_  
> — digitalscorpyun

---

## 🧱 Core Notes Tagged with Black Identity Themes

```dataview
list from ""
where contains(tags, "black_culture")
   or contains(tags, "identity")
   or contains(tags, "cultural_resistance")
   or contains(tags, "black_aesthetics")
sort file.name asc
```

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
