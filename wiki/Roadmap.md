# Roadmap

Timeline for **Churn Guard**, the 새싹반 (AI@Sogang 2기, team 2) mini-project. The team formed on **6/22** and presented at **Demo Day on 7/10**.

> **Status: completed (Demo Day 7/10).** The table below keeps the original plan as history and adds what actually happened. Final numbers are in the [README](../README.md#results).

## Status at a glance
- ✅ Topic chosen (6/27): customer churn prediction and retention strategy
- ✅ Switched from the 2020 Kaggle set (21 columns) to the IBM Telco 2025 extension (7,043 × 33)
- ✅ Zip code joined to US Census ACS 2024 (S1901) household income: 99.94% of zip codes matched
- ✅ LR / Random Forest / LightGBM compared, threshold tuned for recall, SHAP interpretation
- ✅ 3 churn risk factors + 3 retention actions with a cost estimate
- ✅ Demo Day presentation (7 min talk + 5 min Q&A, industry judges)
- ⬜ Local reproducibility: some `examples/` notebooks still use Colab paths, and `pyproject.toml` does not list every dependency (see [Quickstart](../README.md#quickstart))

## Timeline — plan vs. actual

| Window (plan) | Phase | Planned focus | What actually happened |
|---|---|---|---|
| 6/23 – 6/25 | **Phase 1** | EDA, preprocessing, LR baseline | 6/22 team formed · 6/26 four topic proposals + mentor feedback + vote · 6/27 topic confirmed |
| **6/26** | 🚩 Midterm @Day | Share problem, EDA, baseline | Used for topic proposals and the vote, not a baseline review |
| 6/27 – 7/5 | **Phase 2** | RF + LightGBM, tuning, Recall/F1/ROC-AUC | 6/28 kickoff and switch to the 2025 dataset · 6/29 preprocessing/EDA shared · 7/1 midpoint meeting: each member took one segmentation (income / city size / decision tree) and agreed to compare by recall · 7/2 4 feature sets × LR/RF/LightGBM + SHAP |
| 7/6 – 7/8 | **Phase 3** | Feature importance, risk factors, retention actions | 7/8 final merge: member notebooks compared, Lasso and SMOTE experiments shared, deck built (final deck saved 7/9) |
| **7/10** | 🏆 Demo Day | Final presentation (industry judges) | Presented; judge feedback is in the [README](../README.md#demo-day-feedback--next-steps) |

## MVP completion line
- ✅ Logistic Regression baseline
- ✅ Random Forest **and** LightGBM
- ✅ Confusion Matrix / F1 / ROC-AUC
- ✅ Feature Importance and SHAP
- ✅ **3 churn risk factors + 3 retention actions**

## Deliverables
- **Data:** `data/telco_churn_with_income.csv` (income join), `data/retention_action_plan.csv` (per-customer action).
- **Notebooks:** member notebooks in `examples/`, team notebooks in `notebooks/`. See the [README notebook list](../README.md#notebooks).
- **Reports:** `docs/Telco_Churn_Baseline_Report_조정헌.docx`, `docs/Telco_Churn_Project_Report_조정헌.docx`.

## After Demo Day
Next steps come from the judges' feedback: evaluate on AUC/F1 rather than recall alone, avoid SMOTE on encoded categoricals, look at feature interactions and edge cases, and extend the external-data joins.

See [docs/milestones/](../docs/milestones/) for per-phase Definition of Done and the [Project Board](../docs/PROJECT_BOARD.md) for the issue list.
