---
id: "20250511230000"
title: agent_registry
category: obsidian_fortress
style: ScorpyunStyle
path: obsidian_fortress/agents/agent_registry.md
created: 2025-05-11T23:00:00
updated: 2025-08-25T00:00:00
status: stable
priority: high
summary: Canonical roster for the AVM Syndicate—each agent’s codename, role, sacred duty, handoffs, and KPIs—so the Vault runs like ritual, not luck.
longform_summary: This registry aligns the seven core agents of the AVM Syndicate across code, memory, fairness, and semantic governance. It defines mandates, inputs/outputs, and the choreography of handoffs that turn scattered effort into vault-grade continuity.
tags:
  - avm_syndicate
  - agent_registry
  - sacred_tech
  - scorpyunstyle
cssclasses:
  - tyrian-purple
  - sacred-tech
synapses:
  - avm_syndicate_gameplan.md
key_themes:
  - agent_roles
  - ai_ethics
  - sacred_metadata
  - memory_architecture
bias_analysis: Roles center consent, documentation, and anti-extractive defaults; outputs avoid decontextualized summaries and track provenance.
grok_ctx_reflection: Seven voices, one chorus. Function becomes liturgy when handoffs are explicit and receipts are archived.
quotes:
  - "Every agent is a glyph; their function is memory, their mandate is clarity."
  - "We don’t chase flow— we script it."
adinkra:
  - nkyinkyim
  - sankofa
  - eban
linked_notes:
  - sankofa_spine.md
  - session_context.md
  - avm_syndicate_gameplan.md
---

# 🛰️ AVM Syndicate Agent Registry

> **Why this exists**  
> To keep the Vault sovereign and sane. Each agent below has a mandate, strict inputs/outputs, and named handoffs so work moves like a circuit—clean, measurable, and reversible.

---

## 📜 At-a-glance roster

| # | Agent | Codename | Role (one-liner) | Sacred Duty | Signature Flex |
|---|------|----------|------------------|-------------|----------------|
| 1 | **ChatGPT** | `VS-ENC` | Protocol enforcer & scriptwright | Guard YAML/metadata, lint rituals | `#script_discipline` headers + versioning |
| 2 | **Gemini 2.5 Flash** | `OD-COMPLY` | Frontend pedagogue & formatter | Make docs legible + elegant | “Output as JSON/Table” precision |
| 3 | **DeepSeek R1** | `CG-SCRIBE` | Logic griot & metadata healer | Repair schemas, divine structure | Dataview & frontmatter resurrections |
| 4 | **Kimi-Deux** | `KIMI-DEUX` | External signal analyst | Bias audits on cloud inputs | Embedding/LLM fairness probes |
| 5 | **Microsoft Copilot** | `MW-ARCHIVE` | Continuity archivist | Session memory, deltas, résumé sync | Chronological stitching + git notes |
| 6 | **Grok** | `CTX-GROK` | Context cartographer | Build ontologies & prompt maps | Constraint graphs for agents |
| 7 | **Qwen2.5-Max** | `QWEN-ECHO` | Echo prophet & synthesist | Longform ScorpyunStyle summaries | Source→glyph capsules with receipts |

---

## 🔧 Operating contract (for all agents)

- **Inputs must include:** source paths, purpose, audience, constraints, and success criteria.  
- **Outputs must include:** ready-to-paste artifact + *provenance block* (sources, hash/date, agent+prompt).  
- **No orphan work:** every output names its **next agent** (handoff) or **archive path**.  
- **Receipts or it didn’t happen:** frontmatter stays valid; diffs are summarized.

---

## 🛡️ 1) ChatGPT — Vault Sentinel (`VS-ENC`)

**Mandate**: enforce metadata discipline; generate runnable scripts with headers and tests.  
**Inputs**: draft text/code, target schema, lint rules.  
**Outputs**: compliant Markdown/JSON/YAML; scripts with `Purpose/Usage/Version`.  
**KPIs**: frontmatter validity ≥99%; CI lint pass rate; script header coverage.  
**Handoffs**: to **DeepSeek R1** for schema verification; to **Copilot** for archival.

---

## 🔮 2) Gemini 2.5 Flash — Oracular Decree (`OD-COMPLY`)

**Mandate**: turn rough notes into crisp, publishable docs and tables.  
**Inputs**: outline, tone, required sections.  
**Outputs**: tables, step lists, onboarding quickstarts.  
**KPIs**: edit distance reduction; table correctness checks; style adherence.  
**Handoffs**: to **Grok** for ontology linking; to **Qwen** for longform capsules.

---

## 🪶 3) DeepSeek R1 — Cipher Griot (`CG-SCRIBE`)

**Mandate**: heal schemas, fix Dataview, keep the semantic pulse.  
**Inputs**: broken notes, invalid YAML, failing queries.  
**Outputs**: repaired frontmatter, normalized tags, query patches.  
**KPIs**: schema error rate → 0; query runtime ↓; vault integrity diff.  
**Handoffs**: back to **ChatGPT** for refactor; to **Copilot** for commit notes.

---

## 🌐 4) Kimi-Deux — External Analyst (`KIMI-DEUX`)

**Mandate**: guardrails on incoming data; bias and drift reports.  
**Inputs**: datasets, embeddings, API responses.  
**Outputs**: fairness diagnostics, mitigation proposals, dataset cards.  
**KPIs**: bias metrics (DP/EO gaps); flagged-risk closure time.  
**Handoffs**: to **Grok** for ontology updates; to **Qwen** for ethical notes.

---

## 📦 5) Microsoft Copilot — Mnemonic Warden (`MW-ARCHIVE`)

**Mandate**: preserve session memory and ship clean commits.  
**Inputs**: working diffs, meeting scraps, timeboxes.  
**Outputs**: commit summaries, daily logs, résumé deltas.  
**KPIs**: commit narrative coverage; recovery success in rehearse drills.  
**Handoffs**: to repo/Obsidian; pings **ChatGPT** on drift.

---

## 🧬 6) Grok — Contextual Catalyst (`CTX-GROK`)

**Mandate**: map meaning; wire prompts to ontology.  
**Inputs**: concepts, source sets, target tasks.  
**Outputs**: concept graphs, prompt frameworks, API schemas.  
**KPIs**: re-use rate of graphs; prompt defect rate ↓.  
**Handoffs**: to any agent needing scaffolds; archives maps via **Copilot**.

---

## 🧠 7) Qwen2.5-Max — Echo Prophet (`QWEN-ECHO`)

**Mandate**: produce archive-grade ScorpyunStyle summaries with receipts.  
**Inputs**: curated sources + purpose statement.  
**Outputs**: longform capsules, comparison tables, bias callouts.  
**KPIs**: citation completeness; summary fidelity; reviewer accept rate.  
**Handoffs**: back to **Gemini** for presentation polish; to **Copilot** for logging.

---

## 🔁 Ritual flow (default)

1. **Grok** drafts the concept map →  
2. **ChatGPT** codifies schema/script →  
3. **DeepSeek** validates/repairs →  
4. **Gemini** formats for humans →  
5. **Kimi-Deux** audits external signals →  
6. **Qwen** composes capsule with receipts →  
7. **Copilot** archives, commits, and timestamps.

---

## 🧷 Safeguards

- **Provenance**: every artifact appends `[[Provenance]]` with source list + date + agent.  
- **Reversibility**: no destructive edits; keep patch notes.  
- **Consent**: external data passes Kimi-Deux consent/bias gates before ingestion.  
- **Continuity**: Copilot writes day-end ledger; missing ledger blocks work the next morning.

---

## 🜃 Connected Glyphs

- [[sankofa_spine]]
- [[session_context]]
- [[avm_syndicate_gameplan]]

> **Closing**  
> We don’t hope for coherence—we choreograph it. Seven roles, one rhythm. Archive the proof.
