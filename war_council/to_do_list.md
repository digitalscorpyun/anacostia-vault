---
review_date: 2025-05-17
id: "20250511112837"
title: to_do_list
category: vault_ops
style: ScorpyunStyle
path: war_council/to_do_list.md
created: 2025-05-06
updated: 2025-05-16
status: active
priority: critical
summary: Master task registry for ScorpyunOps—tracks vault integrity, automation rituals, fairness protocols, and sacred-tech progression.
longform_summary: This living glyphstream anchors active development within the Anacostia Vault. Every task encodes ritual, responsibility, and rebellion—from Obsidian discipline to Python liberation, AI ethics to personal sovereignty.
tags:
  - to_do
  - vault_ops
  - ai_fairness
  - python
  - automation
  - obsidian
  - sacred_tech
  - scorpyunstyle
cssclasses:
  - tyrian-purple
  - sacred-tech
synapses:
  - session_context
  - ubuntu_env_refinery
  - roadmap_anacostia_vault
  - digitalscorpyun_manifesto_and_syllabus
  - ethics_case_studies
key_themes:
  - automation
  - fairness
  - sacred_code
  - afrikan_memory
bias_analysis: This tracker prioritizes system sovereignty and ethical AI above speed or capitalist output. All task structures re-center ancestral rhythm and anti-colonial logic.
grok_ctx_reflection: Task completion is not productivity—it’s protection. Every item here guards a protocol, a memory, or a threshold in the Vault.
quotes:
  - "Structure is the syntax of sovereignty."
  - "You don’t check off tasks—you enact rituals."
adinkra:
  - Eban
  - Duafe
linked_notes:
  - validate_backlinks
  - vault_yaml_validator_status
  - ethics_case_studies
  - ai_ml_overview
  - the_lion_of_anacostia_bias_detection
---

# ✅ To Do List – Anacostia Vault Ops & Fairness Deployment

---

## 🧠 VAULT MAINTENANCE

- [ ] Normalize tag schema across all vault notes  
- [ ] Remove numeric prefixes across vault  
  - [x] Run `undo_rename_files.py` (rename mode)  
  - [x] Execute `rename_files_no_prefixes.py`  
  - [x] Fix YAML links → `fix_yaml_references.py`  
  - [x] Validate orphan links → [[validate_backlinks]]  
  - [x] Sync: `prefix_map.md`, `vault_index.md`, `session_context.md`  
  - [ ] Audit `graph_view` + metadata integrity in `metadata_protocol.md`
- [x] Finalize `ubuntu_env_refinery.md`  
- [ ] Add cronjob or alias to emit weekly vault map  
- [ ] Improve backlink quality for:
  - [[roadmap_anacostia_vault]]
  - [[ethics_case_studies]]

---

## 🤖 PYTHON & AUTOMATION

- [ ] Fix encoding in `fetch_emails.py` (Gmail-only filter)  
- [ ] Add voter bias data to [[technofeudal_bias_audit]]  
- [ ] Log all simulation outputs to [[voting_rights]]  
- [ ] Deploy `api_key_audit.py` into `avm_ops/`  
- [ ] Draft ethics alert script (auto case flag system)  
- [ ] Add `.env` sync handler → shared `env_config.py`

---

## 📚 STUDY & CERTIFICATION

- [ ] Finish IBM AI Dev Cert (Courses 6–10)  
- [ ] Expand and revise:
  - [[ai_ml_mathematical_modeling]]  
  - [[structure_note_african_diaspora_themes]]  
- [ ] Log reading reflections + notes to [[digitalscorpyun_manifesto_and_syllabus]]  
- [ ] Document Harlem Renaissance design → `software_design_document.md`  

---

## ⚖️ AI FAIRNESS & ETHICS

- [ ] Integrate algebraic bias methods in `the_lion_of_anacostia_bias_detection.md`  
- [ ] AIF360 toolkit test suite → healthcare + voter data  
- [ ] Finalize `ethics_case_template.md` (with Afrofuturist framing)  
- [ ] Add:
  - `palestine_discussion.md`  
  - `voting_rights_and_black_political_representation.md`  
- [ ] Prototype: Afrofuturist predictive simulation model (Python)

---

## 🧩 TEMPLATES & DEBUG LOGS

- [ ] Refactor `default_note_template.md`  
  - [ ] YAML cleanup + `style:` dropdown fix  
  - [ ] Check ScorpyunStyle / GriotBox / UBW inheritance  
- [ ] Fix:
  - `africana_studies_template.md`  
  - `ai_ml_template.md` (Templater parsing bug)  
- [ ] Create:
  - `foundations_programming_terms.md`  
  - `case_study_template_afrofuturist.md`  
- [ ] Log bugs into `debug_log.md`

---

## 📦 CONGO DEEP RESEARCH THREAD

- [ ] Draft → [[george_washington_williams_congo_letter]]  
- [ ] Synthesize → [[congo_resource_colonialism_2025]]  
- [ ] Crosslink: [[africana_studies_colonial_resistance]], [[algorithmic_colonialism]]  
- [ ] Store all under: `africana_studies/history/congo_threads/`

---

## 🍎 PERSONAL & RITUAL TASKS

- [ ] 🛒 Build May grocery list (shelf-stable + communal stock)  
- [ ] 🐦 Refill blue jay feeder (signal of temple renewal)  
- [ ] 🌱 Draft ritual garden blueprint → eco-rebellion layer  

---

> **🝔 “To list is to locate power. Every checkbox is a cipher—complete the ritual.”**  
> — *digitalscorpyun, Anacostia Operations Codex*

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
