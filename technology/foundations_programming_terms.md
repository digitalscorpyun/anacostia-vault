---
id: "20250511112837"
title: foundations_programming_terms
category: technical_glossary
style: ScorpyunStyle
path: avm_archivist/terms/foundations_programming_terms.md
created: 2025-05-11
updated: 2025-05-14
status: active
priority: normal
summary: A foundational glossary of core programming concepts with crosslinks to key Python projects and algorithmic justice workflows in the Anacostia Vault.
longform_summary: |
  This note defines essential programming terms (e.g., syntax, bug, logic error) used throughout the Anacostia Vault. Each entry includes a clear definition, examples, and contextual backlinks to reinforce learning, reduce duplication, and assist new readers of the vault’s AI fairness and automation scripts.
tags:
  - programming
  - glossary
  - python_basics
  - script_discipline
  - vault_onboarding
cssclasses:
  - tyrian-purple
  - sacred-tech
synapses:
  - ai-ml-basics.md
  - the_lion_of_anacostia_bias_detection.md
  - python-chapter4-exercises.md
key_themes:
  - code_as_language
  - error_types
  - programming_literacy
bias_analysis: |
  This glossary resists the assumption that technical fluency is neutral; it surfaces how programming instruction often omits cultural context and how syntax can encode assumptions into scripts and agents alike.
grok_ctx_reflection: |
  This note is a ritual anchor for newcomers and collaborators—a decoder ring for sacred-tech scripting. GROK-CTX maps it as a shared glyph base for AVM agents learning to parse the syntax of resistance.
quotes:
  - Syntax is not neutral. It is structured expectation, rendered executable.
  - A logic error is not just a flaw in code—it’s a mirror of your mental model.
adinkra:
  - duafe
  - eban
linked_notes:
  - ai-ml-basics.md
  - the_lion_of_anacostia_bias_detection.md
  - python-chapter4-exercises.md
  - vault_yaml_validator_status.md
---

# 🧠 Foundations: Key Programming Terms

> _“Even in logic, there is culture. Even in syntax, there is silence.”_

## 🧰 General Programming Terms

### 📌 Program / Code / Source Code
- **Definition**: A written set of instructions executed by a computer.
- **Example**: A Python script that audits YAML metadata across your vault.
- **Backlinks**: [[ai-ml-basics.md]], [[python-chapter4-exercises.md]]

---

### 📌 Machine Code
- **Definition**: Low-level code directly processed by a CPU.
- **Example**: Bytecode compiled from Python `.pyc` files.
- **Backlinks**: [[ai-ml-basics.md]]

---

### 📌 Statement
- **Definition**: A single line or expression in code that performs an action.
- **Example**: `for i in range(10): print(i)`
- **Backlinks**: [[python-chapter4-exercises.md]]

---

### 📌 Syntax
- **Definition**: The structured rules of a programming language.
- **Example**: Python requires colons after `if` or `for` statements.
- **Backlinks**: [[ai-ml-basics.md]], [[the_lion_of_anacostia_bias_detection.md]]

---

### 📌 Compiler
- **Definition**: A tool that translates source code into machine code at once.
- **Example**: GCC compiling C++ source code.
- **Backlinks**: [[ai-ml-basics.md]]

---

### 📌 Interpreter
- **Definition**: A program that translates and runs code line-by-line.
- **Example**: The Python interpreter used in Jupyter or VS Code terminals.
- **Backlinks**: [[python-chapter4-exercises.md]]

---

### 📌 Execution
- **Definition**: The act of running a program on a computer.
- **Example**: Launching `bias_flag.py` in your AVM environment.
- **Backlinks**: [[ai-ml-basics.md]], [[python-chapter4-exercises.md]]

---

## ❌ Error Classifications

### 📌 Syntax Error
- **Definition**: Code fails to run due to formatting violations.
- **Example**: Missing colon: `if x == 3` → will throw an error.
- **Backlinks**: [[the_lion_of_anacostia_bias_detection.md]]

---

### 📌 Logic Error
- **Definition**: The code runs, but the output is incorrect due to flawed logic.
- **Example**: Calculating bias percentage incorrectly in a fairness audit.
- **Backlinks**: [[the_lion_of_anacostia_bias_detection.md]], [[python-chapter4-exercises.md]]

---

### 📌 Runtime Error
- **Definition**: An error that crashes the program during execution.
- **Example**: Dividing by zero in a calculation function.
- **Backlinks**: [[ai-ml-basics.md]], [[python-chapter4-exercises.md]]

---

### 📌 Bug
- **Definition**: Any mistake or flaw in code behavior or logic.
- **Example**: Incorrect variable reference in `technofeudal_bias_audit.py`.
- **Backlinks**: [[the_lion_of_anacostia_bias_detection.md]]

---

## 🌀 Related Concepts to Add Later:
- Variables
- Functions
- Loops
- Conditionals
- Datatypes (int, str, bool)
- Comments
- Modules
- Classes / Objects
- IDEs (VS Code, Jupyter)

---

**Vault Ritual Tip**: Use this glossary as an onboarding anchor for collaborators. Add terms in new notes and backlink them here with `[[foundations_programming_terms.md]]` to strengthen the semantic spine of your tech documentation.

---

> _“Before we code resistance, we must name our tools.”_  
> ― VS-ENC, Vault Sentinel  

## 🜃 Connected Glyphs

- [[ai-ml-basics]]
- [[the_lion_of_anacostia_bias_detection]]
- [[python-chapter4-exercises]]
- [[vault_yaml_validator_status_1]]
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
