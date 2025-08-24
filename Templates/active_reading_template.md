<%*
const raw = tp.file.title ?? "untitled";
const isDaily = /^\d{4}-\d{2}-\d{2}$/.test(raw);   // don't rename daily notes
const d = tp.date.now("YYYYMMDD"), hm = tp.date.now("HHmm");
const slug = raw.replace(/[^\w\s-]/g,"").trim().replace(/\s+/g,"-").toLowerCase();
const folder = (typeof tp.file.folder === "function") ? tp.file.folder() : (tp.file.folder || "");
function existsInFolder(name){const p=(folder?`${folder}/`:"")+`${name}.md`;return app.vault.getAbstractFileByPath(p)!=null;}
if (!isDaily) { let t=`${d}_${slug}`, u=t, i=1; while(existsInFolder(u)) u=`${t}-${i++}`; if (tp.file.title!==u) await tp.file.rename(u); }
let currPath=(typeof tp.file.path==="function")?tp.file.path(true):(tp.file.path||"");
const currPathNoExt=String(currPath).replace(/\.md$/i,"");
%>
---
id: <% d %><% hm %>_<% slug %>
title: "<% raw %>"
category: reading_active
style: ScorpyunStyle
path: "<% currPathNoExt %>"
created: "<% tp.date.now("YYYY-MM-DDTHH:mm:ss") %>"
updated: "<% tp.date.now("YYYY-MM-DDTHH:mm:ss") %>"
status: in_progress
priority: normal
summary: Structured template for deep active reading sessions.
tags: [reading, active_reading, sacred_tech]
cssclasses: [tyrian-purple, sacred-tech]
synapses: []
key_themes: []
bias_analysis: ""
grok_ctx_reflection: ""
quotes: []
adinkra: Eban
linked_notes: []
---

## 🔍 Summary / First Impressions
<% tp.file.cursor() %>

## 🧠 Key Quotes & Marginalia
- …

## 🧪 Conceptual Threads
- …

## ⚖️ Tensions & Contradictions
- …

## Links
- [[ ]]
