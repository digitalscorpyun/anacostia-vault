---
title: "Module 2 — Generative AI for Software Dev Workflows (Cheat Sheet)"
aliases: ["GenAI SW Dev Workflows Cheat Sheet"]
tags: [ibm, course, genai, devsecops, cheat-sheet]
source: "cognitiveclass.ai"
author: "Ritika Joshi"
vault: "Anacostia"
created: 2025-08-25
---

> [!summary] Goal
Quick reference for GenAI tooling, prompts, and snippets used in Module 2.

## Estimated time
~30 minutes

## Tooling map
### CI/CD with AI
- Jenkins • IBM Watson Studio • Codefresh • Atlassian • GitLab CI/CD  
- PagerDuty AIOps • CircleCI • Travis CI • Harness • Snyk • Dynatrace Davis AI

### Software security (secure coding)
- Qwiet AI preZero • Snyk Code • GitHub Advanced Security  
- Veracode Fix • Endor Labs • Microsoft Security Copilot • BurpGPT • EscalateGPT

### Documentation
- Doxygen • NaturalDocs

### Code reviews
- DeepCode • CodeClimate

### Innovation / content tools
- Lumen5 • Deep Nostalgia • Gen-1 • Krisp • Legal Robot • DALL·E 2 • Castle  
- Stable Diffusion 2 • Soundraw • LALAL.ai • Cleanup.Pictures • Looka • Fireflies • Murf

---

## Prompts & setup

### Dev environment
- Install VS Code: <https://code.visualstudio.com/>
- Get OpenAI key: <https://platform.openai.com/signup/>

### Build a basic ChatGPT-backed service
```bash
# Node.js: https://nodejs.org/
npm install express openai
node server.js
