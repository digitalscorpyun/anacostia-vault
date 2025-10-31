---
id: 20251027_084700
title: transformer_glossary_cheat_sheet
category: ai_engineering
style: AuditScroll
path: reading_journal/ai/transformers_glossary.md
created: 2025-10-27T08:47:00-07:00
updated: 2025-10-27T08:47:00-07:00
status: active
priority: high
summary: Plain-English cheat sheet for core Transformer/MT terms—definitions, one-liner, and sources.
tags: [transformers, attention, glossary, mt, bleu, optimization]
cssclasses: [tyrian-purple, sacred-tech]
---

# Transformer Glossary — Plain English

1. **Multi-head** — Several attention “heads” run in parallel; each looks at the input differently, then results are combined (many spotlights, one scene).

2. **Self-attention** — Each word looks at all words (including itself) to decide who matters when updating its meaning, via query/key/value similarity (dot products). (IBM)

3. **MT** — *Machine Translation* (e.g., English → German).

4. **WMT’14** — The 2014 *Workshop on Machine Translation* benchmark/dataset (commonly En↔De).

5. **En-De 28.4** — English→German result with BLEU score **28.4** on a standard benchmark.

6. **BLEU** — *Bilingual Evaluation Understudy*; compares machine output to human references via n-gram overlap. Higher ≈ better.

7. **En-Fr 41.8** — English→French result with BLEU **41.8** (higher than 28.4 ⇒ stronger).

8. **SOTA** — *State Of The Art* (best known performance).

9. **Constituency parsing** — Builds a tree of sentence parts (NP/VP, etc.) showing grammatical structure.

10. **Dot product** — Multiply-and-sum of two vectors; measures alignment/similarity. In attention, higher = pay more attention.

11. **FFNs** — *Feed-Forward Networks*; per-token MLP layers after attention (no loops/memory).

12. **Adam** — Training optimizer (*Adaptive Moment Estimation*) that adapts learning rates per weight from gradient stats.

13. **GRUs** — *Gated Recurrent Units*; RNNs with gates (update/reset) to keep/forget info (simpler than LSTMs).

14. **LSTMs** — *Long Short-Term Memory* RNNs with input/output/forget gates for long-range sequence dependencies.

15. **N = 6 encoder/decoder layer** — Six stacked encoder blocks and six stacked decoder blocks (depth configuration).

16. **LR warm-up** — Start training with a tiny learning rate and ramp it up over initial steps to stabilize early updates.

---

### One-liner
Attention (often multi-head) + per-token FFNs, trained with Adam and LR warm-up, pushed MT to SOTA on WMT (BLEU), while older RNNs (LSTMs/GRUs) and tasks like constituency parsing provide the backdrop.

---

### Sources
- IBM: *What is self-attention?*  
- GeeksforGeeks: *Constituency Parsing*; *GRU Networks*  
- University of Notre Dame (Chiang): *Feedforward Neural Networks*  
- Analytics Vidhya: *What is Adam Optimizer?*  
- Baeldung: *Learning Rate Warm-up*  
- Wikipedia: *Transformer (deep learning architecture)*
```