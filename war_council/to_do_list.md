---
id: '20250511112837'
title: To Do List
category: to_do
style: ScorpyunStyle
path: war_council/to_do_list.md
created: 2025-05-06 15:49
updated: 2025-05-14
status: in_progress
priority: critical
summary: Master task list covering vault maintenance, AI fairness research, Python automation, and personal development goals.
longform_summary: Strategic operational map for maintaining the Anacostia Vault, advancing Python scripting, documenting AI fairness methodologies, and refining personal development workflows under sacred-tech alignment.
tags:
  - to_do
  - vault_ops
  - ai_fairness
  - python
  - obsidian
  - scorpyunstyle
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

# ✅ To Do List – Anacostia Vault & AI Fairness Research

## 🧠 Vault Maintenance & Research

- [ ] 🔁 Prefix Removal Refactor (Files & Folders)
  - [x] Backup Vault → `Anacostia_Vault_20250511_backup.zip`, push to GitHub.
  - [x] Run `undo_rename_files.py` (`rename` mode) and log results.
  - [x] Run `fix_yaml_references.py` to resolve YAML and wikilink mismatches.
  - [x] Execute `rename_files_no_prefixes.py` to fully remove numeric prefixes.
  - [ ] Run `validate_backlinks_script.py` for orphan audit.
  - [ ] Update:
    - `war_council/prefix_map.md`
    - `war_council/vault_index.md`
    - `sankofa_spine.md`
    - `session_context.md`
  - [ ] Validate structure via Graph View & `metadata_protocol.md`.

- [ ] Finalize and review `ubuntu_env_refinery.md`  
- [ ] Schedule recurring execution of `vault_structure_emitter.py` and snapshot commits  
- [ ] Audit Graph View for orphaned/weakly linked notes  
- [ ] Refine tag usage (`#bias_detection`, `#africana_studies`, etc.)  
- [ ] Ensure backlink coherence across:
  - `roadmap_anacostia_vault.md`
  - `ethics_case_studies.md`

- [ ] Deep Research Thread – Congo + George Washington Williams
  - [ ] `george_washington_williams_congo_letter.md`
  - [ ] `congo_resource_colonialism_2025.md`
  - [ ] Backlink to `africana_studies_colonial_resistance.md` & `algorithmic_colonialism.md`
  - [ ] Store under `africana_studies/history/congo_threads/`

## 🤖 Python & Automation

- [ ] Debug & enhance `fetch_emails.py`
- [ ] Refactor and test `technofeudal_bias_audit.py` → Add voter data → link `voting_rights.md`
- [ ] Develop additional scripts for:
  - Ethics case tracking
  - Logging and notifications
- [ ] Validate Google Cloud and API key usage
- [ ] Create `api_key_audit.py` in `~/scripts/vault_ops/`

## 📚 Study & Certification

- [ ] Complete final IBM AI Developer module → Log in `personal_development_digitalscorpyun.md`
- [ ] Expand:
  - `ai_ml_mathematical_modeling.md`
  - `structure_note_african_diaspora_themes.md`
- [ ] Finish AI fairness case studies → log into `ethics_case_studies.md`
- [ ] Link Harlem Renaissance design ethos → `software_design_document.md`

## ⚖️ AI Fairness & Ethics

- [ ] Update `the_lion_of_anacostia_bias_detection.md`
- [ ] Add algebraic fairness analysis methods
- [ ] Evaluate AIF360 Toolkit (healthcare + voting)
- [ ] Finalize ethics case study template (Afrofuturist framing)
- [ ] Add:
  - `palestine_discussion.md`
  - Gerrymandering note: `voting_rights_and_black_political_representation.md`
- [ ] Python simulation: Model Afrofuturist futures

## 🧩 Templates, Fixes, and Bugs

- [ ] 🛠️ `default_note_template.md` Fixes
  - [ ] Refactor `style:` to safely inject from dropdown using Templater
  - [ ] Test all 5 styles (ScorpyunStyle, UBW, GriotBox, etc.)
  - [ ] Verify YAML renders cleanly without multiline prompts
- [ ] Validate `africana_studies_template.md`
- [ ] Fix Templater logic in `ai_ml_template.md`
- [ ] Create:
  - `foundations_programming_terms.md`
  - Case study templates
- [ ] Log bugs into `debug_log.md` (Note Generator + Templater quirks)

## 🍎 Life Tasks

- [ ] May groceries list → prioritize non-perishable/aid
- [ ] Birdfeeder (blue jays 🐦)
- [ ] Garden installation (communal/ritual space)
- [ ] **Return *Before Elvis* to Library by 2025-05-16** 📚
