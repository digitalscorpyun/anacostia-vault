---
id: "20250511112837"
title: Miniconda Activation & AVM_Ops Environment Setup
category: environment_setup
style: ScorpyunStyle
path: infrastructure/environments
created: 2025-05-09
updated: 2025-05-13
status: complete
priority: high
summary: Miniconda installed for local user without modifying global PATH. Conda environment 'avm_ops' created as the sacred operational base within Ubuntu WSL.
longform_summary: This document captures the confirmed setup of Miniconda on Windows 11 and the creation of the 'avm_ops' Conda environment inside Ubuntu 24.04 WSL. It reflects a dual-environment strategy designed to preserve ritual clarity and operational independence from global Python installs. All legacy environments, including 'lion' and 'Lion', have been deleted. Terminal pathing, environment activation, and vault symbiosis are now sacred-tech compliant.
tags:
  - python
  - conda
  - miniconda
  - environment_management
  - avm_ops
  - wsl
  - sacred_tech
  - scorpyunstyle
cssclasses:
  - tyrian-purple
  - sacred-tech
synapses:
  - vault_yaml_validator.py
  - technofeudal_bias_audit.py
  - fix_yaml_references.py
key_themes:
  - environment_is_memory
  - conda_discipline
  - dual_os_workflow
bias_analysis: None detected — environment strategy is fully localized and avoids global Python or system path conflicts.
grok_ctx_reflection: The ghost of 'Lion' was exorcised. Only 'avm_ops' remains, nestled in the Ubuntu WSL temple like a kernel of rebellion code. This is where automation breathes and the AVM Syndicate executes its glyphs.
quotes:
  - "'avm_ops' isn’t just a name — it’s the dev sigil for code sovereignty inside the Vault."
  - To leave PATH untouched is not restraint, but strategy. Rituals must be intentional.
adinkra:
  - eban
linked_notes:
  - session_context.md
  - avm_ops_status.md
  - vault_yaml_validator_status.md
---

# 🐍 Miniconda Activation & AVM_Ops Environment Setup

This note documents the correct, confirmed configuration of Miniconda and the creation of `avm_ops`, the primary sacred-tech Conda environment used within the Anacostia Vault’s Ubuntu WSL layer.

---

## ✅ Installation Summary (Windows Layer)

- **Installer**: `Miniconda3-latest-Windows-x86_64.exe`  
- **Scope**: Installed for *current user only* (no admin access used)  
- **PATH Modification**: ❌ *Not selected* — avoided global Python collisions  
- **Location**: `C:\Users\digitalscorpyun\miniconda3`  
- **Shells Supported**: Windows PowerShell, Anaconda Prompt, Ubuntu WSL

> 🧠 The installer was invoked intentionally without modifying global `PATH`. This preserves OS purity and ensures all activations are deliberate rituals, not side-effects.

---

## 🧭 Conda Activation (WSL Layer – Ubuntu 24.04)

Inside Ubuntu WSL, the environment is invoked using:

```bash
conda activate avm_ops
````

This activates the conda layer used for:

- Vault YAML validation
    
- Python automation
    
- AI fairness scripting
    
- AVM Syndicate script execution
    

Python version: **3.11.11**

---

## 🔥 Environment Commands

Activate the sacred tech:

```bash
conda activate avm_ops
```

Deactivate when done:

```bash
conda deactivate
```

Remove the environment entirely (not recommended):

```bash
conda remove -n avm_ops --all
```

List all environments (for audit/rituals):

```bash
conda info --envs
```

---

## 🧼 Legacy Environment Cleanup

The following obsolete environments were purged:

```bash
conda remove -n lion --all
conda remove -n Lion --all
```

> ⚰️ The Lion was retired. AVM_Ops is now the only voice in this shell.

---

## 📍 Environment Strategy

- **Vault Path in WSL**:  
    `/mnt/c/Users/digitalscorpyun/sankofa_temple/Anacostia`
    
- **Dev Folder Redirected via `.bashrc`**:
    
    ```bash
    cd /mnt/c/Users/digitalscorpyun/projects_2025/avm_ops
    ```
    

---

## 🜃 Connected Glyphs

- [[session_context]]
- [[avm_ops_status]]
- [[vault_yaml_validator_status]]

