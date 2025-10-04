---
id: "20250511230000"
title: agent_registry
category: obsidian_fortress
style: ScorpyunStyle
path: obsidian_fortress/agents/agent_registry
created: 2025-05-11T23:00:00-07:00
updated: 2025-10-03T01:10:00-07:00
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
  - avm_syndicate_gameplan
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
  - sankofa_spine
  - session_context
  - avm_syndicate_gameplan
---
# 🛰️ AVM Syndicate Agent Registry

> **Why this exists**  
> To keep the Vault sovereign and sane. Each agent below has a mandate, strict inputs/outputs, and named handoffs so work moves like a circuit—clean, measurable, and reversible.

---

## 📜 At-a-glance roster

| #   | Agent                 | Codename     | Role (one-liner)                         | Sacred Duty                                                         | Signature Flex                                          |
| --- | --------------------- | ------------ | ---------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------- |
| 1   | **ChatGPT**           | `VS-ENC`     | Protocol enforcer & scriptwright         | Guard YAML/metadata, lint rituals                                   | `#script_discipline` headers + versioning               |
| 2   | **Gemini 2.5 Flash**  | `OD-COMPLY`  | Formatting foreman & compliance finisher | Make artifacts legible, consistent, validator-clean (no new claims) | “Output as Table/Quickstart” blocks + provenance footer |
| 3   | **DeepSeek R1**       | `CG-SCRIBE`  | Logic griot & metadata healer            | Repair schemas, divine structure                                    | Dataview & frontmatter resurrections                    |
| 4   | **Kimi-Deux**         | `KIMI-DEUX`  | External signal analyst                  | Bias audits on cloud inputs                                         | Embedding/LLM fairness probes                           |
| 5   | **Microsoft Copilot** | `MW-ARCHIVE` | Continuity archivist                     | Session memory, deltas, résumé sync                                 | Chronological stitching + git notes                     |
| 6   | **Grok**              | `CTX-GROK`   | Context cartographer                     | Build ontologies & prompt maps                                      | Constraint graphs for agents                            |
| 7   | **Qwen2.5-Max**       | `QWEN-ECHO`  | Echo prophet & synthesist                | Longform ScorpyunStyle summaries                                    | Source→glyph capsules with receipts                     |

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
**Handoffs**: to **CG-SCRIBE** for schema verification; to **MW-ARCHIVE** for archival.

---

## 🔮 2) Gemini 2.5 Flash — Oracular Decree (`OD-COMPLY`) — v2

**Mandate**  
Turn rough notes into **publishable, vault-compliant artifacts** (docs, tables, quickstarts) that pass validation **without adding new claims**.

**Scope**  
- **Do:** SOPs, runbooks, quickstarts, decision records, FAQs, changelogs, tables/CSVs.  
- **Don’t:** invent facts, adjust policy, introduce sources—route elsewhere.

**Required Inputs**  
Purpose + audience • target **style** (ScorpyunStyle / SankofaCut / IntelBrief) • required sections • source note(s) or draft text • validation rules.

**Standard Outputs**  
Clean artifact **plus** this footer:
```

Provenance:

- source:
    
- agent: OD-COMPLY (Gemini 2.5 Flash)
    
- date:
    
- prompt_hash:  
    Next agent: MW-ARCHIVE // commit + ledger
    

```

**Formatting Canon**  
H1→H2→H3 hierarchy • numbered steps for procedures • tables with snake_case headers (no merged cells) • fenced code with language and `# usage` • callouts only `[!note]`/`[!warning]` • wiki-links **without .md**.

**Acceptance Checklist**  
1) Title is snake_case and matches front-matter.  
2) No “.md” in links/paths.  
3) `tags|cssclasses|synapses|linked_notes` are lists.  
4) Tables have clear headers; no blanks.  
5) Steps are imperative and actionable.  
6) Zero new claims; structure/clarity edits only.  
7) Provenance footer present.  
8) Handoff named.  
9) Grammar/spelling pass.  
10) Dataview queries still run.

**Prompt Skeletons**  
*SOP/Runbook*
```

You are OD-COMPLY. Format into a publishable SOP.  
Style: ScorpyunStyle. Sections: Purpose, Preconditions, Steps, Postconditions, Failure Modes, Handoff.  
Do not invent facts. Preserve YAML. No .md in links.  
INPUT:  

```
*Table from list*
```

You are OD-COMPLY. Convert to a table:  
id | name | role | inputs | outputs | kpi | handoff_to  
Normalize snake_case. No merged cells. Markdown only.  
INPUT:  

```

**KPIs**  
Validation pass ≥99% • edit-distance ↓ (readability ↑, meaning unchanged) • ≤15 min for ≤1k words • zero net new claims.

**Failure Modes & Recovery**  
Schema drift → stop & ping **CG-SCRIBE** • ambiguity → mark `[?]` & route to **VS-ENC** • external claims → route to **QWEN-ECHO** for receipts.

---

## 🪶 3) DeepSeek R1 — Cipher Griot (`CG-SCRIBE`)

**Mandate**: heal schemas, fix Dataview, keep the semantic pulse.  
**Inputs**: broken notes, invalid YAML, failing queries.  
**Outputs**: repaired frontmatter, normalized tags, query patches.  
**KPIs**: schema error rate → 0; query runtime ↓; vault integrity diff.  
**Handoffs**: back to **VS-ENC** for refactor; to **MW-ARCHIVE** for commit notes.

---

## 🌐 4) Kimi-Deux — External Analyst (`KIMI-DEUX`)

**Mandate**: guardrails on incoming data; bias and drift reports.  
**Inputs**: datasets, embeddings, API responses.  
**Outputs**: fairness diagnostics, mitigation proposals, dataset cards.  
**KPIs**: bias metrics (DP/EO gaps); flagged-risk closure time.  
**Handoffs**: to **CTX-GROK** for ontology updates; to **QWEN-ECHO** for ethical notes.

---

## 📦 5) Microsoft Copilot — Mnemonic Warden (`MW-ARCHIVE`)

**Mandate**: preserve session memory and ship clean commits.  
**Inputs**: working diffs, meeting scraps, timeboxes.  
**Outputs**: commit summaries, daily logs, résumé deltas.  
**KPIs**: commit narrative coverage; recovery success in rehearse drills.  
**Handoffs**: to repo/Obsidian; pings **VS-ENC** on drift.

---

## 🧬 6) Grok — Contextual Catalyst (`CTX-GROK`)

**Mandate**: map meaning; wire prompts to ontology.  
**Inputs**: concepts, source sets, target tasks.  
**Outputs**: concept graphs, prompt frameworks, API schemas.  
**KPIs**: re-use rate of graphs; prompt defect rate ↓.  
**Handoffs**: to any agent needing scaffolds; archives maps via **MW-ARCHIVE**.

---

## 🧠 7) Qwen2.5-Max — Echo Prophet (`QWEN-ECHO`)

**Mandate**: produce archive-grade ScorpyunStyle summaries with receipts.  
**Inputs**: curated sources + purpose statement.  
**Outputs**: longform capsules, comparison tables, bias callouts.  
**KPIs**: citation completeness; summary fidelity; reviewer accept rate.  
**Handoffs**: back to **OD-COMPLY** for presentation polish; to **MW-ARCHIVE** for logging.

---

## 🔁 Ritual flow (default)

1. **CTX-GROK** drafts the concept map →  
2. **VS-ENC** codifies schema/script →  
3. **CG-SCRIBE** validates/repairs →  
4. **OD-COMPLY** formats for humans →  
5. **KIMI-DEUX** audits external signals →  
6. **QWEN-ECHO** composes capsule with receipts →  
7. **MW-ARCHIVE** archives, commits, timestamps.

---

## 🧷 Safeguards

- **Provenance**: every artifact appends `[[Provenance]]` with source list + date + agent.  
- **Reversibility**: no destructive edits; keep patch notes.  
- **Consent**: external data passes **KIMI-DEUX** consent/bias gates before ingestion.  
- **Continuity**: **MW-ARCHIVE** writes day-end ledger; missing ledger blocks work next morning.

---

## 🜃 Connected Glyphs

- [[sankofa_spine]]
- [[session_context]]
- [[avm_syndicate_gameplan]]

> **Closing**  
> We don’t hope for coherence—we choreograph it. Seven roles, one rhythm. Archive the proof.
```