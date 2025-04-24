---
category: Vault Guidelines
created: '2025-04-09'
last-updated: '2025-04-09'
priority: High
status: Active
summary: "ScorpyunStyle\u2122 is the guiding framework that defines file naming, tag\n\
  \ formats, backlink rules, and summary guidelines for all notes in the Anacostia\n\
  \ vault. Its purpose is to ensure that every link connects to an existing file\u2014\
  \nnever creating a new note in error\u2014and to maintain a consistent, automatable,\n\
  \ and fully integrated knowledge environment."
tags:
- vault_structure
- naming_conventions
- scorpyunstyle
- consistency
title: "ScorpyunStyle\u2122"
---
# ScorpyunStyle™

ScorpyunStyle™ is the guiding framework for all notes in the Anacostia vault. It standardizes file names, tag formats, and backlinks to keep your vault consistent, automatable, and fully integrated. Every internal link must match an existing file name exactly—so that clicking a link opens the correct note, not a new one.

---

## File Naming Conventions

- **Format:** Use kebab-case (all lowercase, words separated by hyphens)  
- **Examples:**  
  - `ai-fairness-tools`  
  - `anacostia-vault-roadmap`  
- **Rationale:**  
  Eliminates spaces and mixed casing issues to ensure compatibility with automation scripts and Obsidian plugins.

---

## Tag Naming Conventions

- **Format:** Use underscore_format  
- **Examples:**  
  - `ai_ethics`  
  - `historical_justice`  
  - `programming_languages`  
- **Rationale:**  
  Underscores enhance searchability and organization while avoiding syntax conflicts in Obsidian.

---

## Backlink Naming Conventions

- **Rule:** Use the exact file names (in kebab-case) that already exist in the vault.  
- **Examples:**  
  - `[[00-index]]`  
  - `[[ai-ml-overview]]`  
  - `[[anacostia-vault-roadmap]]`  
  - [[bias-detection]]  
- **Rationale:**  
  Ensures that clicking a backlink opens the intended, pre-existing note rather than creating a new one.

---

## ScorpyunSummary Guidelines

### What is a ScorpyunSummary?

A ScorpyunSummary is a structured, in-depth summary that extracts key insights from an article, paper, or report. It is concise, analytical, and focuses on topics such as AI, Africana studies, social justice, and political analysis.

### Structure

1. **Key Takeaways:**  
   - Bullet-point highlights of the main ideas.
2. **Context & Background:**  
   - Explain the topic’s historical, political, and social relevance.
3. **Main Points & Analysis:**  
   - Break down core components with supporting data.
4. **Competing Perspectives:**  
   - Summarize opposing viewpoints or critiques.
5. **Industry & Social Relevance:**  
   - Discuss the topic’s impact on AI, technology, culture, and policy.
6. **Conclusion:**  
   - Provide final thoughts and implications for the future.

**Benefits:**  
- Extracts crucial details quickly.
- Provides actionable and concise analysis.
- Avoids fluff in favor of real, useful insights.

---

## The Lion of Anacostia Framework

### Overview

The Lion of Anacostia is the vault’s framework for AI ethics and bias detection research. It integrates machine learning, Africana studies, and algorithmic justice into a cohesive research approach.

### Core Elements

- **Bias Detection:**  
  - Implements fairness metrics, mathematical models, and systematic audits.
- **Decolonial AI:**  
  - Explores the historical roots and epistemic injustices in AI systems.
- **Obsidian Integration:**  
  - Creates an automated workflow by linking diverse research insights.
- **Applied Research:**  
  - Features case studies in criminal justice AI, healthcare algorithms, and financial technology.

**Related Notes:**  
- [[the-lion-of-anacostia-bias-detection]]  
- [[anacostia-hub-notes]]  
- [[bias-mitigation]]  
- [[structure-note-ai-ethics-framework]]

---

## Vault Roadmap Overview

Your vault roadmap is a living guide that integrates core research, automation, and Africana epistemology into one coherent system.

### Key Navigation

- **[[00-index]]** – Central starting point.
- **[[to-do-list]]** – Tracks tasks and action items.
- **[[ai-ml-overview]]** – Technical guide for AI/ML topics.
- **[[africana-studies-overview]]** – Provides historical and ethical context.
- **[[anacostia-vault-roadmap]]** – The live roadmap for continuous updates.

### Additional Areas

- **AI Fairness Research:**  
  - Includes notes like [[the-lion-of-anacostia-bias-detection]], [[bias-mitigation-strategies]], and [[ethics-case-studies]].
- **Automation & Technical Depth:**  
  - Incorporates tools such as [[bias-flag-script]] and [[ai-ml-mathematical-modeling]].
- **Graph View & Maintenance:**  
  - Use scripts (e.g., `graph_view_optimizer`, `validate_backlinks_script`) to maintain full connectivity.

---

## Immediate Action Steps

1. **Review & Integrate:**  
   - Verify and integrate any orphaned nodes into [[00-index]] and [[to-do-list]].
2. **Verify Automation:**  
   - Test Python scripts (e.g., [[bias-flag-script]]) to ensure all backlinks reference existing notes.
3. **Finalize Roadmap:**  
   - Update and commit the latest version of the [[anacostia-vault-roadmap]].

---

## Next Steps

1. **Implement Version Control:**  
   - Use Git for regular backups and tracking changes.
2. **Schedule Regular Reviews:**  
   - Conduct weekly/monthly audits to update naming conventions and backlink structures.
3. **Enhance Vault Functionality:**  
   - Integrate dynamic DataView queries and custom CSS to create a cohesive, visually appealing environment.

---

This document defines ScorpyunStyle™ for your Anacostia vault: files in kebab-case, tags in underscore_format, and backlinks that match existing filenames exactly—ensuring smooth automation and precise navigation.

---

Feel free to refine any section further. Let me know if you’d like additional details or adjustments!

