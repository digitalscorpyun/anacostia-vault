---
id: "20250516140518"
title: active_reading_template
category: template_documentation
style: ScorpyunStyle
path: Templates/active_reading_template.md
created: 2025-05-16 14:05
updated: 2025-05-16
status: in_progress
priority: normal
summary: Structured template for deep active reading sessions.
longform_summary: This template guides annotation, marginalia, and critical response during reading. Designed to track quotes, themes, and interpretive context for texts processed through the Anacostia Vault.
tags:
  - reading
  - active_reading
  - sacred_tech
cssclasses:
  - tyrian-purple
  - sacred-tech
synapses: 
key_themes: 
bias_analysis: ""
grok_ctx_reflection: ""
quotes: 
adinkra: 
linked_notes:
---

## 🔍 Summary / First Impressions  
> _Capture initial reactions, questions, emotional resonance._

---

## 🧠 Key Quotes & Marginalia  
> _Use callouts for emphasis, and bracket page numbers or timestamps._

> [!quote]+ Quote
> “[p.23] Capital no longer wages war through factories. It wins through platforms.”

---

## 🧪 Conceptual Threads  
> _Identify theoretical motifs, repeated language, or emerging logics._

---

## ⚖️ Tensions & Contradictions  
> _Where does the text break, contradict, or destabilize its own claim?_

---

## 🧭 ScorpyunStyle Reading Glyphs  
> _Personal interpretations, mythic coding, ancestral cross-referencing._

---

## 🜃 Connected Glyphs

- [[session_context]]
- [[digitalscorpyun_manifesto_and_syllabus]]
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
