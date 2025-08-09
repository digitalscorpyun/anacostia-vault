---
id: "20250514234000"
title: Terminal Theme – Tyrian Griot
category: system_customization
style: ScorpyunStyle
path: obsidian_fortress/configs/terminal_theme_tyrian_griot.md
created: 2025-05-14
updated: 2025-05-14
status: active
priority: normal
summary: A sacred-tech terminal theme designed for visual resonance with Digitalscorpyun’s identity — fusing Tyrian purple with ancestral gold, optimized for Ubuntu + PowerShell terminals.
longform_summary: The Tyrian Griot terminal theme is a visual ritual layer for all command-line interfaces within the Anacostia Vault. Inspired by Afrofuturist aesthetics and memory-tech symbology, it establishes consistent color, clarity, and narrative tone across Ubuntu (WSL) and Windows shells. This note captures the configuration logic, hexadecimal values, customization scripts, and philosophical underpinnings of the terminal as sacred space.
tags:
  - terminal_theme
  - system_env
  - tyrian_griot
  - customization
  - sacred_tech
cssclasses:
  - tyrian-purple
  - sacred-tech
synapses:
  - session_context.md
  - system_profile.md
  - vs_code_agent_mode_usage.md
key_themes:
  - afrovisual_logic
  - terminal_design
  - sacred_computation
  - code_aesthetic_alignment
bias_analysis: Most default terminal themes cater to high-contrast white-on-black or pastel Linux themes, which ignore cultural context and aesthetic resonance. This scheme centers visual memory and stylistic identity.
grok_ctx_reflection: Color is not cosmetic — it is invocation. Tyrian is memory made visible, and gold is a cipher for ancestral transmission. Together, they bless the shell.
quotes:
  - “I don’t type commands. I light glyphs.”
  - “Let your terminal speak your myth.”
adinkra:
  - Duafe    # Cleanliness and beauty — clarity of output
  - Nkyinkyim # Evolution — adaptive shell scripting
linked_notes:
  - session_context.md
  - system_profile.md
  - vs_code_agent_mode_usage.md
---

# 🎨 Terminal Theme – Tyrian Griot

> _“Every prompt is a portal. Every hex is a hymn.”_

---

## 🌈 Theme Configuration

### 🟣 Background
- **Hex:** `#630330`  
- **Name:** Tyrian Purple  
- **Meaning:** Memory. Royalty. Resistance.

### 🟡 Foreground (Text)
- **Hex:** `#FFAA00`  
- **Name:** Ancestral Gold  
- **Meaning:** Wisdom. Echo. Power.

### ⚪ Accent (Cursor / Emphasis)
- **Hex:** `#D8D8D8`  
- **Purpose:** Visual balance + accessibility (colorblind safe)

### 🟥 Error / Warning Text
- **Hex:** `#FF4C4C`  
- **Meaning:** Ritual breach, invalid invocation

---

## 🧪 Recommended Applications

| Terminal         | Status       | Integration Path                                      |
|------------------|--------------|--------------------------------------------------------|
| Windows Terminal | ✅ Stable     | Settings.json → Add `Tyrian Griot` profile manually   |
| Ubuntu Shell     | ✅ Active     | Custom `~/.bashrc` prompt with ANSI codes             |
| VS Code Terminal | ✅ Enforced   | `settings.json` + Font color override                 |
| Anaconda Prompt  | ✅ Customized | Theme applied via PowerShell `$PROFILE` script        |

---

## 🔧 Sample PowerShell Profile (`$PROFILE`)

```powershell
function Set-TyrianPrompt {
    $esc = [char]27
    function global:prompt {
        "$esc[38;2;255;170;0m🝔 $esc[38;2;216;216;216m🔱 $esc[38;2;99;3;48m🐦‍🔥 PS $($executionContext.SessionState.Path.CurrentLocation)> $esc[0m"
    }
}
Set-TyrianPrompt

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
