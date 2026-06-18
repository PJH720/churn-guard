# Roadmap

Timeline for **Churn Guard** — 새싹반 2-week mini-project. Official work period **6/23 → 7/8**, Midterm @Day **6/26**, **Demo Day 7/10**.

## Status at a glance
- ✅ Notebook 1 (EDA + cleaning + feature engineering) built
- ✅ Repo scaffolding: issue forms, label taxonomy, 3 milestones + 9 phase issues
- ⬜ Notebooks 2–4 (insights, modeling, recommendations) not started
- ⬜ `requirements.txt` + local `file_path` fix ([#2](https://github.com/PJH720/churn-guard/issues/2), [#3](https://github.com/PJH720/churn-guard/issues/3))

## Timeline

| Window | Phase | Focus | Milestone |
|---|---|---|---|
| 6/23 – 6/25 | **Phase 1** | EDA, preprocessing, LR baseline | [#1](https://github.com/PJH720/churn-guard/milestone/1) (due 6/25) |
| **6/26** | 🚩 Midterm @Day | Share problem, EDA, baseline; collect feedback | — |
| 6/27 – 7/5 | **Phase 2** | RF + LightGBM, tuning, Recall/F1/ROC-AUC | [#2](https://github.com/PJH720/churn-guard/milestone/2) (due 7/5) |
| 7/6 – 7/8 | **Phase 3** | Feature importance, risk factors, retention actions | [#3](https://github.com/PJH720/churn-guard/milestone/3) (due 7/8) |
| **7/10** | 🏆 Demo Day | Final presentation + awards (industry judges) | — |

## MVP completion line (minimum to ship)
- Logistic Regression baseline
- Random Forest **or** LightGBM (≥1 tree model)
- Confusion Matrix / F1 / ROC-AUC
- Feature Importance
- **3 churn risk factors + 3 retention actions**

## Deliverables by phase
- **Phase 1:** EDA insight set, LR baseline metrics, `telco_churn_cleaned.csv`.
- **Phase 2:** 3-model comparison table, tuned final model.
- **Phase 3:** Risk-group definition + retention strategy, Demo Day deck.

See [docs/milestones/](../docs/milestones/) for per-phase Definition of Done, and the [Project Board](../docs/PROJECT_BOARD.md) for the issue list.
