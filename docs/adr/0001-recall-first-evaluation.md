# ADR-0001: Optimize for Recall (not Accuracy) when selecting models

- **Status:** Accepted
- **Date:** 2026-06-18
- **Deciders:** Churn Guard team

## Context

The Kaggle Telco Customer Churn dataset is **imbalanced**: only **26.54%** of customers churn. A trivial model that predicts "no churn" for everyone scores ~73% accuracy while catching **zero** churners — so **Accuracy is a misleading selection metric** here.

The business goal is retention: we want to *find the customers who are about to leave* so we can act. In that framing:

- A **false negative** (a churner predicted to stay) = a lost customer we never tried to save — the expensive error.
- A **false positive** (a stayer predicted to churn) = some wasted retention spend (a discount or outreach) — comparatively cheap.

The class deliverable is also explicitly business-facing (3 risk factors + 3 retention actions), and the rubric/proposal calls for F1, Recall, and ROC-AUC over raw accuracy.

## Decision

When training and **selecting** models, we will:

1. **Rank models by Recall first**, then F1, then ROC-AUC. We do **not** select on Accuracy.
2. Always produce a **Confusion Matrix** and explicitly analyze **Type-II error** (missed churners), aiming to minimize it.
3. Handle the imbalance during training — stratified train/test split on `Churn_Flag` and `class_weight="balanced"` (or equivalent), considering resampling (e.g. SMOTE) if needed.
4. Apply this consistently across Logistic Regression (baseline) and Random Forest / LightGBM.

## Consequences

**Positive**
- The selected model catches more real churners, which is what the retention strategy depends on.
- Evaluation is honest about imbalance and defensible to the Demo Day judges.

**Negative / trade-offs**
- Higher Recall typically lowers Precision: we will flag some non-churners and may "waste" retention budget on them. We accept this trade-off, but report Precision/F1 so the cost is visible.
- A pure-Recall optimum can be degenerate (predict everyone churns). F1 and ROC-AUC act as guardrails against that.

**Affects:** Notebook 3 (modeling/evaluation) and Notebook 4 (interpretation → retention actions); see [wiki/Architecture.md](../../wiki/Architecture.md) and [docs/milestones/phase-2.md](../milestones/phase-2.md).
