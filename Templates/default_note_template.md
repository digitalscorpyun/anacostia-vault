---
id: "<% tp.date.now('YYYYMMDDHHmmss') %>"
title: "<% tp.file.title %>"
category: ""
style: "<%* 
const options = ['ScorpyunStyle', 'UBW', 'GriotBox', 'NarrativeThread', 'FormalSummary'];
let choice = await tp.system.suggester(options, options);
tR = choice || 'ScorpyunStyle'; %>"
path: "<% tp.file.path(true) %>"
created: <% tp.date.now("YYYY-MM-DD HH:mm") %>
updated: <% tp.date.now("YYYY-MM-DD") %>
status: in_progress
priority: normal
summary: ""
longform_summary: ""
tags: []
cssclasses:
  - tyrian-purple
  - sacred-tech
synapses: []
key_themes: []
bias_analysis: ""
grok_ctx_reflection: ""
quotes: []
adinkra: ["🧠 Nkyinkyim"]
linked_notes: ["sankofa_spine"]
---


# <% tp.file.title %>

## 🎯 Purpose  
*A one‑sentence purpose statement for this note.*  

---

## 📝 ScorpyunStyle Analysis

1. **Key Takeaways** –  
2. **Historical & Cultural Context** –  
3. **Critical Analysis** –  
4. **Contemporary Connection** –  
5. **Relevance to the Vault** –  
6. **Conclusion or Reflection** –  

---

## 🜃 Connected Glyphs

- [[sankofa_spine]]
