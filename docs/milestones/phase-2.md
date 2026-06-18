# Phase 2 — Advanced Modeling & Evaluation

**Milestone:** [#2](https://github.com/PJH720/churn-guard/milestone/2) · **Due:** 2026-07-05 · **Starts after** Midterm @Day (6/26)

## Goal
Beat the baseline with tuned tree ensembles and **select a final model on business-aligned metrics** (catch churners → minimize Type-II error).

## Scope
Midterm feedback integration · Random Forest + LightGBM · Grid/Randomized Search + cross-validation · Recall/F1/ROC-AUC comparison across all three models. Maps to bootcamp **Ch05 Random Forest** & **Ch06 LightGBM**.

## Issues
- [#14 Midterm Feedback & Feature Refinement](https://github.com/PJH720/churn-guard/issues/14) — `type: data`, `priority: medium`
- [#15 Model Training & Hyperparameter Tuning (RF & LightGBM)](https://github.com/PJH720/churn-guard/issues/15) — `type: modeling`
- [#16 Comprehensive Model Evaluation](https://github.com/PJH720/churn-guard/issues/16) — `type: modeling`

## Definition of Done
- [ ] Midterm feedback documented and addressed (incl. class-imbalance strategy).
- [ ] RF + LightGBM trained and tuned with CV; optimal params recorded.
- [ ] Confusion matrix, classification report, and ROC/AUC for LR vs RF vs LightGBM.
- [ ] Final model selected by **Recall on the churn class**, with written rationale.

## Dependencies / risks
- Requires Phase 1's `telco_churn_cleaned.csv` + finalized train/test split.
- Overfitting on trees — rely on CV + a held-out test set.
