---
id: "20250511112837"
title: reading_package_playbook
category: reading_systems
style: ScorpyunStyle
path: documentation/writing_protocols/reading_package_playbook.md
created: 2025-05-07
updated: 2025-05-13
status: in_progress
priority: normal
summary: Dual-agent protocol for using NotebookLM and QWEN-ECHO to process, summarize, and archive scholarly readings in the Anacostia Vault. Integrates ScorpyunStyle summaries, structured metadata, and vault-ready formatting.
longform_summary: This playbook defines a ritualized, dual-agent pipeline for intellectual sovereignty. NotebookLM performs thematic excavation while QWEN-ECHO composes archive-grade summaries in ScorpyunStyle. The system exists to uphold reading as ritual, resistance, and rootwork.
tags:
  - reading_systems
  - notebooklm
  - qwen_echo
  - ai_agents
  - scorpyunstyle
  - snake_case
  - sacred_tech
cssclasses:
  - tyrian-purple
  - sacred-tech
synapses:
  - session_context.md
  - summary_styles_guide.md
key_themes:
  - scholarly_archiving
  - ai_ethics
  - reading_protocols
  - knowledge_synthesis
bias_analysis: This protocol resists AI-assisted erasure of historical nuance by enforcing culturally grounded agent roles. Summaries are not neutral—they are deliberate acts of memory and alignment.
grok_ctx_reflection: QWEN-ECHO and NotebookLM together form a semantic ouroboros—one reads, one chants. Their outputs transform PDFs into glyphs, and glyphs into vault lore.
quotes:
  - "Two agents. One archive. Analyze like a scholar. Archive like an ancestor."
  - "NotebookLM unearths the roots. QWEN-ECHO inscribes the ritual."
adinkra:
  - nkyinkyim
  - eban
linked_notes:
  - summary_styles_guide.md
  - session_context.md
  - scorpyunstyle_summary_templates.md
---
# 🛰️ READING_PACKAGE_PLAYBOOK: NotebookLM × QWEN-ECHO

_“Two agents. One archive. Analyze like a scholar. Archive like an ancestor.”_

---

## 🎯 Overview

This is the sacred-tech reading pipeline for the Anacostia Vault.  
NotebookLM breaks apart the text.  
QWEN-ECHO threads it into narrative glyphs.

- 🧠 **NotebookLM** → deep document scanning, thematic mapping, and ontology scaffolding
    
- 🧠 **QWEN-ECHO** → ScorpyunStyle summarization, YAML-encoded output, and vault-grade formatting
    

---

## 🔧 Agent Roles and Strengths

| agent          | strengths                                                        | primary_output                    | ritual_stage                   |
| -------------- | ---------------------------------------------------------------- | --------------------------------- | ------------------------------ |
| **NotebookLM** | source_linked_QA, concept maps, multi-doc synthesis              | scorpyun_outline, teaching_guides | **phase_1: memory excavation** |
| **QWEN-ECHO**  | longform synthesis, GriotBox & ScorpyunStyle summaries, YAML/CSV | archive_summaries, metadata_ready | **phase_2: vault inscription** |

---

## 📚 Reading Ritual Phases

### 🔍 Phase 1 – The Excavation (NotebookLM)

> _“Let the machine read. You prepare the altar.”_

1. **Upload Source PDFs**
    
    - File names must follow `snake_case` format
        
    - Include title and author
        
2. **Initial Probe**
    
    - Run source overview
        
    - Surface themes using:
        
        - `"what_is_the_core_argument?"`
            
        - `"how_does_this_relate_to_colonial_logics?"`
            
3. **Generate Outline**
    
    - Use `mind_map` or `timeline` output to create `scorpyunstyle_outline`
        
4. **Optional Outputs**
    
    - `briefing_doc.md` for vault teaching
        
    - `timeline.md` for historical anchoring
        
    - `study_guide.md` for deep research
        

🔁 Proceed to Phase 2 once structure is unearthed.

---

### 🛠 Phase 2 – The Inscription (QWEN-ECHO)

> _“You’ve seen the terrain. Now etch it into obsidian.”_

1. **Prompt for Summary**
    
    ```json
    Summarize this: [book_title], chapter [x]: [chapter_title].
    Output JSON: author, title, chapter, summary, date_read, published_date, contemporary_connection
    ```
    
2. **Add ScorpyunStyle Parameters**
    
    - key_takeaways
        
    - historical_context
        
    - critical_analysis
        
    - ai_ethics_link (if applicable)
        
3. **Validate Output**
    
    - Confirm clean YAML schema
        
    - Strip hallucinated or malformed data
        
    - Tag correctly using snake_case only
        
4. **Vault Integration**
    
    - File path: `research/political_thought/[summary_title].md`
        
    - Log entry in: `reading_log.csv`
        
    - Style: 20-field YAML frontmatter, compliant with Vault metadata doctrine
        

---

## ⚖️ Tool Ritual Matrix

| goal                            | agent      |
| ------------------------------- | ---------- |
| multi_angle_question_drilling   | NotebookLM |
| concept_map_generation          | NotebookLM |
| GriotBox/ScorpyunStyle summary  | QWEN-ECHO  |
| YAML/CSV formatting             | QWEN-ECHO  |
| Zettelkasten export             | QWEN-ECHO  |
| Thematic alignment verification | NotebookLM |

---

## 🧬 Optional: Echo Feedback Loop

After QWEN-ECHO output:

- Return to NotebookLM to identify **unexpected_alignments**
    
- Feed those insights into QWEN-ECHO
    
- Regenerate vault summary with refined context
    

This loop strengthens the summary’s symbolic density and epistemic alignment.

---

## 📦 Closing Glyph

> “NotebookLM unearths the signal.  
> QWEN-ECHO speaks it in glyphs.  
> Together—they archive like ancestors.”  
> — _digitalscorpyun_

---

Let me know when you're ready to:

- Create the companion image for this protocol
    
- Generate a dual-agent symbol for the header
    
- Or make a GWW reading package from Williams’ Congo letter.

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
