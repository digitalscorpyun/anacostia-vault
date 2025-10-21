---
id: 20250923_071500
title: summary_styles_guide
category: obsidian_fortress
style: AuditScroll
path: reading_journal/summary_styles_guide.md
created: 2025-09-23T07:15:00-07:00
updated: 2025-10-19T15:00:00-07:00
review_date: 2025-12-01T18:00:00-07:00
status: active
priority: critical
summary: Transmission protocols for fast, disciplined summaries—SankofaCut, UBW, ScorpyunStyle, and GriotBox—plus validation checks and style index.
longform_summary: |
  This guide codifies Anacostia’s core summary protocols so every excerpt, brief, and social drop lands with structure and receipts.
  It defines when to use each style, the exact fields/sections to include, and provides copy-ready mini-templates and examples.
  The validation checklist enforces YAML and encoding hygiene across the Vault.
tags:
  - summary_protocols
  - scorpyunstyle
  - sankofacut
  - ubw
  - griotbox
  - vault_ops
cssclasses:
  - tyrian-purple
  - sacred-tech
synapses:
  - session_context
  - reading_agent_prompt_template
  - vault_standard
  - run_inject_links
key_themes:
  - knowledge_standardization
  - receipts_first
  - fast_synthesis
  - vault_hygiene
bias_analysis: |
  These protocols privilege clarity and evidence density over neutral tone. They are intentionally prescriptive to resist drift
  and flattening by external algorithms. Counterbalance is maintained through explicit “Counterpoints” sections where relevant.
grok_ctx_reflection: |
  Form is a shield. Rhythm is a key. Protocols let memory travel intact across tools, time, and tempers.
quotes:
  - Receipts before rhetoric.
  - Structure is not the enemy of freedom; it is its ritual.
adinkra:
  - Nkyinkyim
  - Eban
linked_notes:
  - session_context
  - summary_styles_gallery
  - reading/active
  - reading/summaries
---

# Summary Styles Guide  
**Transmission protocols** for signal amplification and memory preservation  

---

## Core Protocols

### SankofaCut *(Thesis-First Micro-Brief)*  
**For:** High-velocity synthesis with explicit tension  
**Structure:**
```markdown
**Thesis:** <claim (≤15 words)>
- <evidence bullet>
- <evidence bullet>
**Tension:** <X> // <Y>
**So-what:** <1-line implication>
**Sting:** <one-line punch>
**Reflection (micro):** <1–3 sentences>
````

**Example:**

```markdown
**Thesis:** Boycotts without labor and law are sugar-rush politics.
- Historical wins paired boycotts with unions, lawsuits, regulation.
- Pure consumer shaming rarely moved boards or budgets.
**Tension:** Public heat // Private leverage
**So-what:** Aim at contracts, courtrooms, and councils—not checkout lines.
```

---

### UBW _(Unified Black Wisdom)_

**For:** Lineage-to-resistance narratives (systems, eras, doctrines)  
**Sections:**

1. **Origins** — roots, founding logic, initial mechanisms
    
2. **Modifications/Moments** — reforms, backlashes, inflection points
    
3. **Current State** — how it operates now + leverage points  
    **Tip:** Close each section with 1–2 receipts (dates/clauses/cases).
    

---

### ScorpyunStyle

**For:** Poetic-critical analysis of texts/media/events  
**Flow:**

- **Key Takeaways** → **Context** → **Counterpoints** → **Why It Matters** → _(Poetic Close)_
    

**Micro-template:**

```markdown
**Key Takeaways:** <3 bullets, receipts-first>
**Context:** <who/when/where with dates>
**Counterpoints:** <steelman opposing claims>
**Why It Matters:** <institutional or policy stakes>
*Poetic Close:* <1–2 lines, sting or cadence>
```

---

### GriotBox _(Dense Glyphs)_

**For:** Social drops / ritual pauses / caption overlays  
**Form:** One to three lines, compressed voltage.  
**Example:**

> When algorithms forget, we remember in triple time.

---

## Social Protocol — BlueSky (ScorpyunStyle, two hashtags)

**Tone:** ScorpyunStyle (poetic-critical, receipts-first)  
**Structure (≤280 chars):**

> <statement — no intro fluff>
> 
> #<primary_theme> #<context_or_series>

**Template:**

```text
<one or two receipts + sting in a single, tight sentence or two>.
#<primary_theme> #<context_or_series>
```

**Notes:**

- Exactly **two hashtags**; prioritize discoverability + series continuity.
    
- Keep names/stylizations per Vault conventions (e.g., tRUmp).
    
- Preserve cadence: receipts → implication → sting.
    

---

## Style Index Table

|Style|Use Case|
|---|---|
|`IntelBrief`|Tactical timelines + incident maps|
|`CodeRitual`|Annotated script companions|
|`AuditScroll`|Compliance / validation outputs|

> **Guidance:** Prefer `IntelBrief` for conflicts and operations; `CodeRitual` for scripts and CLI runs; `AuditScroll` for YAML sweeps, link fixes, and protocol updates.

---

## Validation Checklist

- UTF-8 encoding
    
- LF line endings in YAML
    
- No smart quotes in frontmatter
    
- Timestamps ISO-8601 compliant
    
- No `.md` in wiki-style links
    
- 20-field YAML present where required
    

**Adinkra Seal:**

> _Nkyinkyim twists—the protocol bends but never breaks._

---

## Quick Reference Snippets

**Dataview – Recent ScorpyunStyle notes (14 days):**

```dataview
TABLE file.mtime as Updated, path
FROM ""
WHERE style = "ScorpyunStyle" AND file.mtime >= date(today) - dur(14 days)
SORT file.mtime desc
```

**Dataview – All active GriotBoxes:**

```dataview
LIST
FROM "" 
WHERE style = "GriotBox" AND status = "active"
```

---

## Connected Glyphs

- [[session_context]]
    
- [[summary_styles_gallery]]
    
- [[reading/active]]
    
- [[reading/summaries]]