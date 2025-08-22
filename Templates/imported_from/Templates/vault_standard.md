---
id: <% tp.date.now("YYYYMMDDHHmmss") %>
title: <% tp.file.title %>
category: <% tp.system.prompt("Category") %>
style: ScorpyunStyle
path: <% tp.system.prompt("Folder path") %>
created: <% tp.date.now("YYYY-MM-DD HH:mm") %>
updated: <% tp.date.now("YYYY-MM-DD HH:mm") %>
status: in_progress
priority: medium
summary: ""
longform_summary: ""
tags: []
cssclasses: []
synapses: ["", "", ""]
key_themes: ["", "", ""]
bias_analysis: ""
grok_ctx_reflection: ""
quotes: ["", "", ""]
adinkra: ["sankofa"]
linked_notes:
  - "[[sankofa_spine]]"
  - "[[digitalscorpyun_manifesto_and_syllabus]]"
---

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
