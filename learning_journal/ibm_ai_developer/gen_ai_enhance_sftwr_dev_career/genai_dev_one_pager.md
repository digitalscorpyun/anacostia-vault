# Generative AI in Software Dev — One‑Pager (Exam + Practice)

## Diagramming
- Output formats: **Mermaid**, **PlantUML**, **C4-style** (via text), **Graphviz DOT**.
- Use cases: system/sequence/state diagrams, alt designs, synthetic test data, requirement summaries.

## Benefits
- Faster iterations, cost reduction.
- Creativity/coverage (alt designs, edge cases).
- Starter designs for non-experts.

## Challenges
- **Bias/inaccuracy**, hallucinations.
- Ethical risks (misinfo, privacy).
- IP ambiguity & licensing.
- Security: data leakage, adversarial inputs.

## IP & Licensing
- Define **ownership** in contracts.
- Track provenance (datasets, prompts, model + version).
- Respect licenses for models/data.
- Patent **novel applications**, not base models.

## Security
- Data minimization; **encrypt** in transit/at rest.
- Access control + monitoring; secret scanning (e.g., GitGuardian).
- Adversarial/red-team testing.
- Incident response runbook.

## Compliance & Ethics
- **Consent** + transparency notices.
- **Privacy by design**; anonymize/pseudonymize.
- Bias assessment & mitigation; document limits.
- Explainability where feasible; audit trails.

## Accuracy/Bias Workflow
1) Diverse datasets → clear metrics.  
2) Eval (holdout set, user tests).  
3) Iterate (retrain/prompt-guard).  
4) Feedback loop + logs.

## Quick MCQ Hints
- Email security: focus on **detect/prevent malicious content** (not encryption).  
- EdTech: value is **personalized learning** (more than doc automation).

## Ship Checklist (1 minute)
- [ ] Owner + license OK  
- [ ] Consent/privacy-by-design set  
- [ ] Secrets scanned; repos clean  
- [ ] Bias/quality metrics defined  
- [ ] Model/prompt/versioned with changelog  
- [ ] IR plan + logging on

---
**VS Code tips**: open Markdown, press **Ctrl+Shift+V** to preview. Mermaid renders in preview & on GitHub.
