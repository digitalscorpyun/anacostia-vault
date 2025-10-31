---
id: '20250511112837'
title: How to Customize PowerShell Prompt – ScorpyunStyle
category: vault_docs
style: ScorpyunStyle
path: ''
created: 2025-05-05
updated: '2025-05-11'
status: in_progress
priority: normal
summary: ''
longform_summary: ''
tags:
- powershell
- terminal_customization
- sacred_tech
- tyrian_purple
- obsidian_ops
- script_discipline
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



# 🖥️ How to Customize Your PowerShell Prompt – ScorpyunStyle™

## 🎯 Purpose

Transform the standard PowerShell prompt into a sacred-tech interface that reflects the **Anacostia Vault aesthetic** — clear, high-contrast, and symbolic of the Algorithmic Griot’s mission.

---

## 🎨 Color Theme

- **Background:** `#630330` (Tyrian Purple)
- **Foreground/Text:** `#FFAA00` (Ancestral Gold)

You can set this in **Windows Terminal** (not in `$PROFILE`):

1. Open *Windows Terminal* settings (CTRL+,)
2. Under `profiles → PowerShell → appearance`, set:

   ```json
   "colorScheme": "ScorpyunStyle"

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
