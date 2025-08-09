---
id: "20250511112837"
title: summary_styles_guide
category: documentation
style: ScorpyunStyle
path: documentation/writing_protocols/summary_styles_guide.md
created: 2025-05-03 17:15
updated: 2025-05-18
status: stable
priority: high
summary: |
  Defines and differentiates the primary summary and style formats used across the Anacostia Vault: UBW, ScorpyunStyle™, GriotBox, and extended format tags such as IntelBrief and CodeRitual.
longform_summary: |
  This guide codifies digitalscorpyun’s vault-native transmission modes—UBW, ScorpyunStyle™, and GriotBox—each designed for a distinct narrative function within the Anacostia system. It also defines additional scroll `style:` types like AuditScroll and FieldReport to standardize formatting and improve clarity across diverse file types.
tags:
  - summary_formats
  - scorpyunstyle
  - ubw
  - griotbox
  - sacred_tech
  - writing_protocols
cssclasses:
  - tyrian-purple
  - sacred-tech
synapses: 
  - session_context.md
  - digitalscorpyun_manifesto_and_syllabus.md
key_themes:
  - afroalgorithmic_ethics
  - digital_resistance
  - narrative_structure
  - knowledge_sovereignty
bias_analysis: This note biases structure over spontaneity—designed to enforce intentionality in scroll writing and resist algorithmic flattening of meaning.
grok_ctx_reflection: |
  To summarize a system is to encode it. Each summary type functions as a glyphstream protocol—some poetic, some tactical, all designed to preserve memory against imperial formatting.
quotes:
  - "Each summary is a glyph. Each glyph is a chant. Each chant is a map."
  - "UBW isn't just structure—it's memory with motive."
adinkra: 
  - Nkyinkyim
  - Eban
linked_notes:
  - session_context.md
  - digitalscorpyun_manifesto_and_syllabus.md
---

# 🧠 Summary Styles Guide

These formats are not styles—they’re **transmission protocols**. Choose the structure that amplifies the signal, resists flattening, and honors the memory work.

---

## 🔷 UBW – *Unified Black Wisdom Summary*

**UBW** = structured synthesis from historical lineage to algorithmic resistance.  
Use when context is heavy, and the scroll must expose buried power.

### 🔹 Structure:
- **Origins**  
- **Mods (Modifications, Moments, or Mutations)**  
- **Current State**

### 🔹 Use For:
- Colonial systems, global technopower, state violence
- Vault knowledge where **lineage and impact** must be interwoven  
- Deep AI critique and Africana synthesis

---

## 🔥 ScorpyunStyle™

Digitalscorpyun’s glyphwork signature. Lyrical, historical, ethical.  
It carries narrative weight with rhythm and resistance.

### 🔹 Structure:
- Key Takeaways  
- Context  
- Main Arguments  
- Counterpoints  
- Why It Matters  
- (Optional) Poetic Close

### 🔹 Use For:
- Reading logs, deep essays, longform reflections  
- Bias studies, AI fairness analysis  
- Vault entries blending critique + soul

---

## 📦 GriotBox – *Mini Glyphs with Maximum Density*

Glyphs born for fast drop. Condensed voltage.

### 🔹 Structure:
- 1–3 line poetic burst  
- Metaphor, inversion, or signal-flip  
- Designed to trigger attention, memory, or ritual pause

### 🔹 Use For:
- Social drops (X, Threads, Bluesky)  
- Caption overlays, quote blocks  
- Preambles in code or scrolls  
- Compressed commentary inside dataviews

---

## 🧮 Extended Style Index

Use these values in the `style:` field when structuring special-purpose scrolls.

| Style Value       | Meaning / Best Use Case                                      |
|-------------------|--------------------------------------------------------------|
| `ScorpyunStyle`   | Poetic narrative + vault ritual form (default for glyphwork) |
| `IntelBrief`      | Tactical, factual, conflict timelines                        |
| `DocuStyle`       | Longform objective summary, archival reference               |
| `AuditScroll`     | YAML compliance, CG‑SCRIBE outputs, script audits            |
| `CodeRitual`      | Script companions + logic-annotated markdown (Python, PS1)   |
| `TheoryFrame`     | Abstract frameworks, academic philosophical synthesis        |
| `FieldReport`     | First-person or field-based ethnographic documentation       |

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
