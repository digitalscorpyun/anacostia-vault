---
id: '<% tp.date.now("YYYYMMDDHHmmss") %>'
title: "<% tp.file.title %>"
category: "vault_ops"
style: "ScorpyunStyle"
path: "obsidian_fortress/projects"
created: "<% tp.date.now('YYYY-MM-DD HH:mm') %>"
updated: "<% tp.date.now('YYYY-MM-DD HH:mm') %>"
status: "<% tp.system.suggester(['idea', 'in_progress', 'complete'], ['in_progress']) %>"
priority: "<% tp.system.suggester(['high', 'medium', 'low'], ['medium']) %>"

summary: "<% tp.system.prompt('Short summary (1 sentence max)') %>"
longform_summary: "<% tp.system.prompt('Full project purpose and goals') %>"

tags: [vault_ops, sacred_tech, ai_ethics, digitalscorpyun]
cssclasses: [tyrian-purple, sacred-tech]

synapses:
  - ""
  - ""

key_themes:
  - ""

bias_analysis: ""
grok_ctx_reflection: ""
quotes:
  - ""

adinkra:
  - "🦢 sankofa"

linked_notes:
  - [[digitalscorpyun_manifesto_and_syllabus]]
  - [[00_to_do_list]]
---

# <% tp.file.title %>

## 🧱 Project Overview
<%= tp.frontmatter.longform_summary || "Write a detailed breakdown of this refactor." %>

---

## 🧰 Subtasks (Sprint Style)
- [ ] Subtask 1  
- [ ] Subtask 2  
- [ ] Subtask 3  
- [ ] Document YAML, glyphs, or agent prompt logic  
- [ ] Link relevant notes

---

## 🧠 Reflections & Rituals
Use this to track any mindset, energy, or symbolic alignment work.

---

## 🔗 Related Notes
- [[war_council/anacostia_vault_structure]]
- [[vault_structure_emitter]]

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
